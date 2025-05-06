# 1) Base image
FROM ubuntu:latest

# 2) Install python3, venv, pip
RUN apt-get update \
 && apt-get install -y python3 python3-venv python3-pip \
 && rm -rf /var/lib/apt/lists/*

# 3) Create and activate a virtualenv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 4) Set working dir
WORKDIR /app

# 5) Copy & install Python deps inside venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy rest of your code
COPY . .

# 7) Default command
CMD ["python", "main.py"]
