FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir antlr4-python3-runtime==4.13.2

COPY src/ src/

ENTRYPOINT ["python3", "src/main.py"]
