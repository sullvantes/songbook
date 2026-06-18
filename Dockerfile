ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

# SQLite export for first-deploy import into Fly Postgres (see scripts/fly_release.sh).
RUN test -f /code/data/sqlite_backup.json || echo "Note: data/sqlite_backup.json not in image; deploy import will be skipped."

EXPOSE 8000

CMD ["gunicorn","--bind",":8000","--workers","2","songbook.wsgi"]
