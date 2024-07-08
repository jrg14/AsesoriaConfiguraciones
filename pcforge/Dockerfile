# Dockerfile
FROM python:3.11-alpine

WORKDIR /pcforge
COPY . /pcforge
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "PCForge.wsgi:application"]