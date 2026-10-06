FROM python:3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_DEFAULT_TIMEOUT=300
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends --fix-missing \
       build-essential \
       libpq-dev \
       libcairo2 \
       libpango-1.0-0 \
       libpangocairo-1.0-0 \
       libgdk-pixbuf-2.0-0 \
       libffi-dev \
       shared-mime-info \
       ca-certificates \
       curl \
       gnupg \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && chmod a+r /etc/apt/keyrings/docker.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(. /etc/os-release && echo $VERSION_CODENAME) stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends --fix-missing docker-ce-cli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Install core dependencies first (smaller packages)
RUN pip install --no-cache-dir --timeout=300 \
    Django==5.0.6 \
    djangorestframework==3.15.1 \
    psycopg[binary]==3.3.4 \
    redis==5.0.4 \
    celery==5.4.0 \
    django-celery-beat==2.7.0 \
    requests==2.32.3 \
    qrcode[pil]==7.4.2 \
    pydyf==0.11.0 \
    cairosvg==2.9.0 \
    gunicorn==22.0.0 \
    whitenoise==6.6.0 \
    python-dotenv==1.0.1 \
    pypdf==4.2.0

# Install torch separately with longer timeout (large package ~800MB)
RUN pip install --no-cache-dir --timeout=600 --index-url https://download.pytorch.org/whl/cpu torch==2.4.1

# Install remaining ML dependencies
RUN pip install --no-cache-dir --timeout=1000 \
    chromadb==0.5.20 \
    sentence-transformers==3.3.1

COPY . .

# Create scripts directory if it doesn't exist
RUN mkdir -p /app/scripts

# Copy and make entrypoint executable
COPY scripts/entrypoint.sh /app/scripts/
RUN chmod +x /app/scripts/entrypoint.sh

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
