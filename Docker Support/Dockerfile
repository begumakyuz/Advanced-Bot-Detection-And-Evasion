FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps chromium

# Copy project files
COPY . .

# Create output directory
RUN mkdir -p assets/bot_analysis

# Run self-check on build
RUN python self_check.py --quick || echo "Self-check failed"

CMD ["python", "bot_detection_analyzer.py"]
