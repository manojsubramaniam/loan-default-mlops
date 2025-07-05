# Dockerfile

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Default CMD is FastAPI (overridden in docker-compose for trainer)
CMD ["uvicorn", "src.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
