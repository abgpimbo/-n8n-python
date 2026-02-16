FROM python:3.12-slim

WORKDIR /app

# optional aber praktisch (curl für Healthchecks/Debug)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl iputils-ping traceroute \
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
