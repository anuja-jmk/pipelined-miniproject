FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r calculator/requirements.txt

EXPOSE 8050

CMD ["gunicorn", "calculator.app:server", "-b", "0.0.0.0:8050"]