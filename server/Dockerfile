FROM python:3.10-slim
WORKDIR /app
COPY .. /app
RUN pip install --upgrade pip && pip install fastapi uvicorn pydantic
EXPOSE 8000
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
