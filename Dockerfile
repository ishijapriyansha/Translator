FROM python:3.10-slim

# Set environment variables to prevent .pyc files and enable buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Run migrations and collect static files (optional but recommended)
# CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn Translator.wsgi:application --bind 0.0.0.0:8000"]

# Final run command
CMD ["gunicorn", "translate_app.wsgi:application", "--bind", "0.0.0.0:8000"]
