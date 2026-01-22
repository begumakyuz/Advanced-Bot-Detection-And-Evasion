# Bot Detection & Evasion Study (Playwright)

Bu proje, modern web sitelerinin bot trafiğini nasıl tespit ettiğini analiz etmek ve bu tespit mekanizmalarını aşma (evasion) tekniklerini araştırmak amacıyla geliştirilmiştir. 

## 🛡️ Proje Amacı
Web otomasyon araçlarının (Playwright, Puppeteer, Selenium) bıraktığı dijital izleri (fingerprint) manipüle ederek, botların gerçek bir kullanıcı gibi görünmesini sağlamak.

## ✨ Özellikler
- **Headless Detection Bypass:** Tarayıcının "headless" modda olduğunu ele veren `navigator.webdriver` bayrağının gizlenmesi.
- **Fingerprint Manipülasyonu:** `hardwareConcurrency`, `languages` ve `plugins` gibi donanım/yazılım verilerinin manuel enjeksiyonu.
- **User-Agent Spoofing:** Gerçekçi tarayıcı kimlikleri kullanarak tespit riskinin azaltılması.
- **JavaScript Injection:** Sayfa yüklenmeden önce çalışan özel scriptler ile tarayıcı özelliklerinin değiştirilmesi.

## 🛠️ Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)
   cd proje-adi
