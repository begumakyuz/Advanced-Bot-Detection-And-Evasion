# 🤖 Bot Detection Analyzer

Web sitelerinin botları tespit etmek için kullandığı tüm temel kriterleri analiz eden profesyonel Python aracı.

## 🎯 Özellikler

### Kontrol Edilen Bot Tespit Kriterleri:

1. **WebDriver Tespiti**
   - `navigator.webdriver` kontrolü
   - Chrome Driver varlığı
   - Permissions API tutarlılığı

2. **Automation Flags**
   - Selenium işaretleri (`$cdc_asdjflasutopfhvcZLmcfl_`)
   - PhantomJS işaretleri
   - Nightmare işaretleri
   - DOM Automation bayrakları

3. **Browser Plugins**
   - Plugin sayısı ve türleri
   - MIME types sayısı
   - Plugin tutarlılık kontrolü

4. **Canvas Fingerprinting**
   - Canvas render hash'i
   - Görsel tutarlılık kontrolü

5. **WebGL Fingerprinting**
   - GPU Vendor ve Renderer bilgisi
   - Unmasked WebGL parametreleri

6. **Audio Context**
   - Audio fingerprint hash'i
   - Frequency bin kontrolü

7. **Hardware Info**
   - Screen resolution
   - Color depth
   - CPU core sayısı
   - Device memory
   - Touch points

8. **Browser Bilgileri**
   - User Agent
   - Platform
   - Language settings
   - Vendor bilgisi

9. **Timezone & Locale**
   - Timezone offset
   - Intl API bilgileri

10. **Performance & Timing**
    - Navigation timing
    - Performance API erişimi

11. **Permissions & APIs**
    - Notifications API
    - Geolocation API
    - Storage API

12. **Connection Info**
    - Effective connection type
    - Downlink speed
    - RTT (Round Trip Time)

## 📦 Kurulum

### 1. Gereksinimleri Yükle

```bash
pip install -r requirements.txt
```

### 2. Playwright Browser'ları Kur

```bash
playwright install chromium
```

### 3. Sistem Sağlığını Kontrol Et (Opsiyonel ama Önerilen)

```bash
python self_check.py
```

veya hızlı kontrol için:

```bash
python self_check.py --quick
```

## 🛠️ Auto Test Ability (Self-Check)

Proje, kendi sağlığını otomatik olarak kontrol edebilir! Bu özellik şunları test eder:

### Kontrol Edilen Bileşenler:

- ✅ **Python Version** - Minimum 3.8 gerekli
- ✅ **Operating System** - Platform bilgisi
- ✅ **Playwright Library** - Kütüphane yüklü mü?
- ✅ **Chromium Browser** - Browser kurulu ve çalışıyor mu?
- ✅ **Directory Structure** - Gerekli klasörler var mı?
- ✅ **File Permissions** - Yazma izinleri tamam mı?
- ✅ **Network Connectivity** - İnternet bağlantısı var mı?
- ✅ **Fingerprint Injection** - JS injection çalışıyor mu?
- ✅ **Memory Usage** - Yeterli RAM var mı?
- ✅ **Disk Space** - Yeterli disk alanı var mı?

### Self-Check Kullanımı:

#### 1. Standalone Script ile:

```bash
# Tam kontrol
python self_check.py

# Hızlı kontrol (network ve browser testleri atlanır)
python self_check.py --quick

# Rapor kaydetme
python self_check.py --save-report

# Hızlı kontrol + rapor
python self_check.py -q -s
```

#### 2. Ana Program İçinde:

Ana programı çalıştırdığınızda self-check yapma seçeneği sunulur:

```bash
python bot_detection_analyzer.py

# Program size soracak:
# 1. Direkt analiz yap
# 2. Önce sistem sağlık kontrolü yap (Self-Check)
```

#### 3. Programatik Kullanım:

```python
from bot_detection_analyzer import SystemHealthChecker

# Health checker oluştur
checker = SystemHealthChecker()

# Tam kontrol
success = checker.run_all_checks()

# Hızlı kontrol
success = checker.run_all_checks(skip_network=True, skip_browser=True)

# Rapor kaydet
checker.save_report("my_health_report.json")

# Sonuçları al
if success:
    print("Sistem sağlıklı!")
else:
    print(f"Hatalar: {checker.errors}")
    print(f"Uyarılar: {checker.warnings}")
```

### Self-Check Çıktı Örneği:

```
================================================================================
🛠️  SYSTEM HEALTH CHECK - AUTO TEST ABILITY
================================================================================
Proje bileşenlerinin sağlığı kontrol ediliyor...

⏳ Python Version......................... ✅ OK
⏳ System Info............................ ✅ OK
⏳ Playwright Library..................... ✅ OK
⏳ Chromium Browser....................... ✅ OK
⏳ Directory Structure..................... ✅ OK
⏳ File Permissions....................... ✅ OK
⏳ Memory Usage........................... ✅ OK
⏳ Disk Space............................. ✅ OK
⏳ Fingerprint Test....................... ✅ OK
⏳ Network Connection..................... ✅ OK

================================================================================
📊 HEALTH CHECK SUMMARY
================================================================================

✅ Başarılı: 10/10
⚠️  Uyarı: 0/10
❌ Hata: 0/10
⏱️  Süre: 3.45 saniye

================================================================================
🎉 MÜKEMMEL! Tüm sistem kontrolleri başarılı.
================================================================================
```

### Health Check Raporu (JSON):

```json
{
  "timestamp": "2024-01-27T14:30:22.123456",
  "duration_seconds": 3.45,
  "summary": {
    "total_checks": 10,
    "passed": 10,
    "warnings": 0,
    "errors": 0
  },
  "checks": {
    "Python Version": {
      "status": "✅ OK",
      "value": "3.11.0",
      "details": "Python 3.11.0 - Destekleniyor"
    },
    ...
  }
}
```

## 🚀 Kullanım

### Basit Kullanım

```bash
python bot_detection_analyzer.py
```

Program çalıştırıldığında sizden iki seçim yapmanızı isteyecek:

1. **Mod Seçimi:**
   - `1` - Normal Mod (Bot olarak tespit edilebilir)
   - `2` - Stealth Mod (Anti-detection önlemleri aktif)

2. **Görünüm Modu:**
   - `1` - Headless (Tarayıcı görünmez, hızlı)
   - `2` - Headed (Tarayıcı açılır, yavaş ama görsel)

### Programatik Kullanım

```python
from bot_detection_analyzer import BotDetectionAnalyzer

# Analyzer oluştur
analyzer = BotDetectionAnalyzer(
    headless=True,      # Headless mod
    stealth_mode=True   # Anti-detection aktif
)

# Özel bir siteyi test et
analyzer.analyze_site("https://example.com", "my_site")

# Rapor oluştur
analyzer.generate_report()
```

## 📊 Çıktılar

Script çalıştırıldığında şu çıktıları üretir:

### 1. Screenshot'lar
```
assets/bot_analysis/sannysoft_20240127_143022.png
assets/bot_analysis/pixelscan_20240127_143045.png
...
```

### 2. Analiz Raporu (Text)
```
assets/bot_analysis/analysis_report_20240127_143022.txt
```

Örnek rapor içeriği:
```
================================================================================
BOT DETECTION ANALYSIS REPORT
================================================================================
Tarih: 2024-01-27 14:30:22
Mod: Headless | Stealth: Aktif
================================================================================

================================================================================
📊 SANNYSOFT
================================================================================
URL: https://bot.sannysoft.com/

🤖 WEBDRIVER TESPİTİ:
   • navigator.webdriver: False
   • Chrome Driver: True
   • Permissions API: True

🚩 AUTOMATION FLAGS:
   • Selenium: False
   • DOM Automation: False
   • PhantomJS: False
   • Nightmare: False

⚠️ BOT RİSK SKORU:
   • Skor: 2/10
   • Risk Seviyesi: 🟢 DÜŞÜK
```

### 3. JSON Data
```
assets/bot_analysis/fingerprint_data_20240127_143022.json
```

Tüm parmak izi verilerini içerir (programatik analiz için).

### 4. Log Dosyası
```
bot_detection_analysis.log
```

## 🎭 Normal vs Stealth Mod

### Normal Mod
- Playwright'ın varsayılan ayarlarını kullanır
- Bot olarak tespit edilmesi muhtemeldir
- Test ve benchmark için idealdir

### Stealth Mod
- `navigator.webdriver` özelliğini gizler
- Chrome runtime ekler
- Automation bayraklarını maskeler
- Bot tespitini zorlaştırır
- **Dikkat:** Bazı siteler yine de tespit edebilir

## 🔍 Bot Risk Skoru Hesaplama

Script, 0-10 arası bir risk skoru hesaplar:

| Skor  | Risk Seviyesi | Açıklama |
|-------|---------------|----------|
| 0-3   | 🟢 DÜŞÜK      | İnsan kullanıcı gibi görünüyor |
| 4-6   | 🟡 ORTA       | Bazı şüpheli özellikler var |
| 7-10  | 🔴 YÜKSEK     | Bot olarak tespit edilebilir |

### Skor Kriterleri:
- `navigator.webdriver = true` → +3 puan
- Automation flag tespit edildi → +2 puan
- 0 plugin → +2 puan
- Anormal CPU core sayısı → +1 puan
- 0 touch points → +1 puan
- Canvas hatası → +1 puan

## 🧪 Test Edilen Siteler

Script varsayılan olarak şu popüler bot tespit sitelerini test eder:

1. **Sannysoft Bot Detector** - https://bot.sannysoft.com/
   - Kapsamlı bot özellik kontrolü

2. **PixelScan** - https://pixelscan.net/
   - Canvas ve WebGL fingerprinting

3. **Are You Headless** - https://arh.antoinevastel.com/bots/areyouheadless
   - Headless browser tespiti

4. **Device and Browser Info** - https://deviceandbrowserinfo.com/are_you_a_bot
   - Genel cihaz bilgisi analizi

## 🛡️ Anti-Detection Teknikleri

Stealth mode aktifken kullanılan teknikler:

1. **Navigator Maskeleme**
```javascript
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});
```

2. **Chrome Runtime Ekleme**
```javascript
window.chrome = { runtime: {} };
```

3. **Permissions API Düzeltme**
```javascript
// Notification permission'ı düzgün döndür
```

4. **Browser Argümanları**
- `--disable-blink-features=AutomationControlled`
- `--disable-dev-shm-usage`
- `--no-sandbox`

## 📈 Gelişmiş Kullanım

### Özel Site Ekleme

```python
analyzer = BotDetectionAnalyzer(headless=True, stealth_mode=True)

# Kendi sitelerinizi test edin
analyzer.analyze_site("https://mywebsite.com", "my_test")
analyzer.analyze_site("https://competitor.com", "competitor_test")

analyzer.generate_report()
```

### Fingerprint Verisini İşleme

```python
import json

# JSON verisini oku
with open('assets/bot_analysis/fingerprint_data_20240127.json', 'r') as f:
    data = json.load(f)

# Belirli bir siteyi analiz et
sannysoft = data['sannysoft']
print(f"WebDriver Present: {sannysoft['fingerprint']['webdriver']['present']}")
print(f"Plugin Count: {sannysoft['fingerprint']['plugins']['count']}")
```

## ⚠️ Önemli Notlar

1. **Etik Kullanım**: Bu araç yalnızca eğitim ve test amaçlıdır. Kötü niyetli bot oluşturmak için kullanmayın.

2. **Site Kuralları**: Test ettiğiniz sitelerin robots.txt ve kullanım şartlarına uyun.

3. **Rate Limiting**: Aynı siteyi çok sık test etmeyin, sunucu kaynaklarına saygılı olun.

4. **Yasal Sorumluluk**: Botları yasaklayan sitelerde bu aracı kullanmak yasal sorunlara yol açabilir.

## 🐛 Troubleshooting

### "playwright not found" hatası
```bash
pip install playwright
playwright install chromium
```

### "Timeout" hataları
- İnternet bağlantınızı kontrol edin
- VPN kullanıyorsanız devre dışı bırakın
- Timeout süresini artırın (kod içinde `timeout=30000`)

### Screenshot'lar boş
- Headed mode'da çalıştırıp tarayıcıyı görsel olarak kontrol edin
- Site'in JavaScript gerektirip gerektirmediğini kontrol edin

## 📝 Log Seviyeleri

Log seviyesini değiştirmek için:

```python
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## 🤝 Katkıda Bulunma

1. Yeni bot tespit kriterleri ekleyin
2. Daha fazla test sitesi önerin
3. Anti-detection tekniklerini geliştirin
4. Bug raporları ve öneriler gönderin

## 📄 Lisans

Bu proje eğitim amaçlıdır. Ticari kullanım için izin gerekir.

## 🔗 Kaynaklar

- [Playwright Documentation](https://playwright.dev/python/)
- [Browser Fingerprinting Techniques](https://github.com/fingerprintjs/fingerprintjs)
- [Bot Detection Methods](https://antoinevastel.com/bot%20detection/2020/02/06/detecting-chrome-headless.html)

---

**⚡ İyi Testler! ⚡**
