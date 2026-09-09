# Generated migration for SubQuestion and SubQuestionTestCase models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_studentquestionhint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('select', 'SELECT'), ('insert', 'INSERT'), ('update', 'UPDATE')], help_text='Type of sub-question: SELECT, INSERT, or UPDATE', max_length=10)),
                ('title', models.CharField(max_length=160)),
                ('slug', models.SlugField(max_length=180)),
                ('description', models.TextField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=16)),
                ('csv_level', models.PositiveSmallIntegerField(default=1)),
                ('level_range', models.CharField(blank=True, max_length=32)),
                ('sample_input', models.TextField(blank=True)),
                ('sample_output', models.TextField(blank=True)),
                ('starter_code', models.TextField(blank=True)),
                ('language_id', models.PositiveIntegerField(help_text='Language id. 50 is C (GCC).', default=50)),
                ('time_limit', models.FloatField(default=2.0)),
                ('memory_limit_kb', models.PositiveIntegerField(default=128000)),
                ('allow_multiple_languages', models.BooleanField(default=False)),
                ('starter_codes', models.JSONField(blank=True, default=dict)),
                ('is_mandatory', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('proctoring_enabled', models.BooleanField(default=True, help_text='Enable or disable proctoring monitoring for this sub-question.')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user')),
                ('main_question', models.ForeignKey(help_text='The main question this sub-question belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='subquestions', to='core.question')),
            ],
            options={
                'ordering': ['main_question__order', 'type'],
                'unique_together': {('main_question', 'type')},
            },
        ),
        migrations.CreateModel(
            name='SubQuestionTestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdin', models.TextField(blank=True)),
                ('expected_output', models.TextField()),
                ('is_sample', models.BooleanField(default=False)),
                ('order', models.PositiveSmallIntegerField(default=1)),
                ('subquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_cases', to='core.subquestion')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.AddField(
            model_name='submission',
            name='subquestion',
            field=models.ForeignKey(blank=True, help_text='The sub-question this submission is for (if applicable)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='core.subquestion'),
        ),
    ]