FROM python:3.10-slim

# Install tzdata for timezone support
RUN apt-get update && apt-get install -y tzdata

# Set timezone to Europe/Helsinki
ENV TZ=Europe/Helsinki

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "app.py"]
