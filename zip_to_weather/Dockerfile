FROM python:3.8-slim

WORKDIR /app

COPY app.py .

EXPOSE 8080

RUN pip install flask

ENV python app.py

CMD ["python", "app.py"]