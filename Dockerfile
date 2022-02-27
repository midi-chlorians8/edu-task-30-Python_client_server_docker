FROM python:3.9-slim
WORKDIR /app
COPY hello-word.py .
CMD [ "python3",  "hello-word.py"]