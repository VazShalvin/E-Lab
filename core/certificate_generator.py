"""
Certificate generation from the SVG template.
Converts SVG → PDF directly via cairosvg (no intermediate PNG step).
"""
import logging
import re
from io import BytesIO

import cairosvg

from django.conf import settings

logger = logging.getLogger(__name__)

# SVG placeholder → safe fallback text used when the real value is unavailable.
_FALLBACKS = {
    "{NAME}": "STUDENT NAME",
    "{USN}": "NNM000000",
    "{course name}": "CCE e-Lab Programming Course",
    "{dd/mm/yyyy}": "01/01/2025",
    "{FACULTY_NAME}": "FACULTY COORDINATOR",
    "{fac_grade}": "Course Faculty",
}


def _substitute_placeholders(svg_content: str, student, course_name: str, issued_date: str, faculty_name: str) -> str:
    """Replace every known placeholder in the SVG with the real value,
    falling back to a sensible default when the value is empty."""

    def replace(key: str, value: str) -> str:
        if not value or not value.strip():
            value = _FALLBACKS.get(key, key)
        return svg_content.replace(key, str(value).upper() if key in ("{NAME}", "{USN}", "{FACULTY_NAME}") else str(value))

    svg_content = replace("{NAME}", student.display_name)
    svg_content = replace("{USN}", student.usn or student.username)
    svg_content = replace("{course name}", course_name)
    svg_content = replace("{dd/mm/yyyy}", issued_date)
    svg_content = replace("{FACULTY_NAME}", faculty_name)
    svg_content = replace("{fac_grade}", "Course Faculty")
    return svg_content


def generate_certificate_pdf(student, percentage, semester, issued_date, verify_url):
    """
    Generate a certificate PDF from the SVG template with substituted student data.
    Uses cairosvg.svg2pdf() directly — no intermediate PNG, no manual pypdf
    stream construction. Returns PDF bytes.
    """
    svg_path = str(settings.BASE_DIR / "templates" / "certificates" / "hi.svg")

    try:
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_content = f.read()
    except FileNotFoundError:
        logger.error(f"Certificate SVG template not found: {svg_path}")
        raise

    # Resolve dynamic values
    course_name = _resolve_course_name(student)
    faculty_name = _resolve_faculty_name(student)

    svg_content = _substitute_placeholders(svg_content, student, course_name, issued_date, faculty_name)

    # cairosvg can output PDF directly — no PNG round-trip needed.
    # A4 landscape dimensions: 842.25 x 595.5 points (same as the SVG viewBox).
    try:
        pdf_data = cairosvg.svg2pdf(
            bytestring=svg_content.encode("utf-8"),
            # Force A4-landscape output so the PDF page matches the SVG viewBox.
            output_width=842.25,
            output_height=595.5,
            # Render at 150 DPI for good print quality without huge files.
            scale=1.0,
        )
    except Exception as exc:
        logger.error(f"cairosvg PDF generation failed: {exc}", exc_info=True)
        raise

    return pdf_data


def _resolve_course_name(student) -> str:
    """Return the primary course name for the student's certificate."""
    from core.models import Course, Module, Submission

    completed_modules = (
        Module.objects.filter(
            questions__submissions__student=student,
            questions__submissions__status=Submission.Status.ACCEPTED,
            is_active=True,
        )
        .distinct()
    )
    if not completed_modules.exists():
        return "CCE e-Lab Programming Course"

    course_names = (
        Course.objects.filter(modules__in=completed_modules)
        .values_list("name", flat=True)
        .distinct()
    )
    names = list(course_names)
    return ", ".join(names) if names else "CCE e-Lab Programming Course"


def _resolve_faculty_name(student) -> str:
    """Return the faculty coordinator name, or a fallback."""
    from core.models import User

    coordinator = _get_faculty_coordinator(student)
    if coordinator:
        return coordinator.display_name or coordinator.username
    return "FACULTY COORDINATOR"


def _get_faculty_coordinator(student):
    """Get the faculty coordinator for a student based on completed modules."""
    from core.models import Course, Module, Submission, User as UserModel
    from django.db.models import Count, Q

    completed_modules = Module.objects.filter(
        questions__submissions__student=student,
        questions__submissions__status=Submission.Status.ACCEPTED,
        is_active=True,
    ).distinct()

    if not completed_modules.exists():
        return None

    courses = Course.objects.filter(modules__in=completed_modules).annotate(
        completion_count=Count(
            "modules__questions__submissions",
            filter=Q(
                modules__questions__submissions__student=student,
                modules__questions__submissions__status=Submission.Status.ACCEPTED,
            ),
            distinct=True,
        )
    ).order_by("-completion_count")

    top_course = courses.first()
    if top_course:
        return top_course.managing_faculty.first()
    return None
