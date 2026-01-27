# 🚀 Quick Start Guide - Self-Check Feature

## 3 Dakikada Self-Check'i Kullanmaya Başlayın!

### Adım 1: Kurulum

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Playwright browser'ları kur
playwright install chromium
```

### Adım 2: İlk Self-Check

```bash
# Basit kullanım
python self_check.py
```

**Çıktı:**
```
================================================================================
🛠️  SYSTEM HEALTH CHECK - AUTO TEST ABILITY
================================================================================

⏳ Python Version......................... ✅ OK
⏳ System Info............................ ✅ OK
⏳ Playwright Library..................... ✅ OK
⏳ Chromium Browser....................... ✅ OK
⏳ Directory Structure..................... ✅ OK
⏳ File Permissions....................... ✅ OK

✅ Başarılı: 6/6
```

### Adım 3: Ana Programı Çalıştır

```bash
python bot_detection_analyzer.py
```

Program size self-check yapmak isteyip istemediğinizi soracak!

---

## Hızlı Komutlar

| Komut | Açıklama |
|-------|----------|
| `python self_check.py` | Tam kontrol (önerilen) |
| `python self_check.py --quick` | Hızlı kontrol |
| `python self_check.py -s` | Rapor kaydet |
| `python self_check.py -q -s` | Hızlı + rapor |

---

## Sorun Giderme

### ❌ "Playwright not found"

```bash
pip install playwright
playwright install chromium
```

### ❌ "Python version too old"

Python 3.8 veya üstü gerekli. Güncelleme:
```bash
# Linux/Mac
sudo apt update && sudo apt install python3.11

# Windows - python.org'dan indirin
```

### ❌ "Permission denied"

Klasör izinlerini düzeltin:
```bash
chmod -R 755 assets/
```

### ⚠️ "Network test failed"

Network testleri opsiyoneldir, atlayabilirsiniz:
```bash
python self_check.py --no-network
```

---

## Programatik Kullanım (5 Satır!)

```python
from bot_detection_analyzer import SystemHealthChecker

checker = SystemHealthChecker()
if checker.run_all_checks():
    print("✅ Hazır!")
else:
    print(f"❌ Hatalar: {checker.errors}")
```

---

## Self-Check Ne Kontrol Eder?

✅ Python versiyonu (min. 3.8)  
✅ Playwright kurulumu  
✅ Browser (Chromium) kurulumu  
✅ Klasör yapısı  
✅ Yazma izinleri  
✅ Bellek durumu  
✅ Disk alanı  
✅ Network bağlantısı  
✅ JavaScript injection  

---

## Sonraki Adımlar

1. ✅ Self-check'i çalıştırdınız
2. 📖 Ana README.md'yi okuyun
3. 🚀 Bot Detection Analyzer'ı çalıştırın
4. 📚 examples_self_check.py'deki örneklere bakın

---

**🎉 Hazırsınız! İyi testler!**
