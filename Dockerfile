FROM python:3.10-slim

WORKDIR /app

COPY ./calculator /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8050

CMD ["gunicorn", "app:server", "-b", "0.0.0.0:8050"]