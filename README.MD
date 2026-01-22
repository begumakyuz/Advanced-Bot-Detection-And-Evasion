# Advanced Bot Detection and Evasion Study

Bu çalışma, açık kaynaklı web otomasyon araçlarının (Playwright) web siteleri tarafından nasıl tespit edildiğini analiz etmek ve bu tespit mekanizmalarını aşmak (evasion) için geliştirilmiş teknikleri içermektedir.

## 🛡️ Proje Amacı
Web sitelerinin bot trafiğini (Playwright, Puppeteer, Selenium) tespit etme yöntemlerini analiz eden ve bu tespitleri tarayıcı parmak izi (fingerprinting) verilerini manipüle ederek atlatma tekniklerini araştıran bir çalışmadır.

## ✨ Teknik Özellikler & Gereksinim Karşılaması
Bu proje, "Açık Kaynak İşletim Sistemi Projesi" yönergesinde belirtilen tüm teknik gereksinimleri karşılar:

* **Auto Control Ability:** `check_system.py` betiği, sistemin çalışabilirliğini ve hedef siteye erişimi otomatik olarak denetler.
* **Auto Test Ability (Self-Check):** Proje, kendi kütüphane bağımlılıklarını ve tarayıcı motorlarını test edebilen bir öz-denetim mekanizmasına sahiptir.
* **Metadata Standard:** Proje bilgileri `project_info.json` dosyasında standartlaştırılmıştır.

## 🛠️ Kurulum ve Çalıştırma

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/begumakyuz/Advanced-Bot-Detection-And-Evasion.git](https://github.com/begumakyuz/Advanced-Bot-Detection-And-Evasion.git)
   cd Advanced-Bot-Detection-And-Evasion

python -m venv venv
# Windows için:
.\venv\Scripts\activate


pip install playwright
playwright install chromium


🚀 Kullanım

Sistemin hazır olup olmadığını test etmek için (Auto-Test):
Bash

python check_system.py

Ana bot ve evasion simülasyonunu çalıştırmak için:
Bash

python bot_test.py

🔬 Evasion Teknikleri

    Fingerprint Manipulation: hardwareConcurrency, languages ve plugins verilerinin enjeksiyonu.

    WebDriver Masking: navigator.webdriver bayrağının undefined olarak set edilmesi.

    User-Agent Spoofing: Gerçek kullanıcı tarayıcı kimliklerinin taklit edilmesi.

Author: Begüm Akyüz
