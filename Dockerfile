FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python", "./app.py"]
CMD []

