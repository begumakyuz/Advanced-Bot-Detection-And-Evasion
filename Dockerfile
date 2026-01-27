FROM python:3.11-slim

WORKDIR /app

# Sistem bağımlılıkları ve Playwright için gerekli kütüphaneler
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright tarayıcılarını kur
RUN playwright install chromium

# Tüm projeyi kopyala
COPY . .

# Çıktı klasörlerini oluştur (Yönergeye uygun)
RUN mkdir -p assets/bot_analysis

# Kodu çalıştır (src/ klasörü içindeki dosyayı çağırdığımızdan emin olalım)
CMD ["python", "src/bot_detection_analyzer.py"]
