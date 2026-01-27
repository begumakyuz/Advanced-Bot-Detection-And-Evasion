# 🏗️ Proje Mimarisi ve Mantıksal Akış (Architecture)

Bu döküman, **Advanced Bot Detection And Evasion** projesinin teknik mimarisini, modüler yapısını ve siber güvenlik analiz mantığını açıklar.

## 1. Genel Sistem Mimarisi

Proje, "Modüler Güvenlik Analizi" prensibiyle tasarlanmıştır ve üç ana katmandan oluşur:

* **Sağlık ve Kontrol Katmanı (SystemHealthChecker):** Projenin çalışma ortamını (OS, Python, Browser) denetleyen "Self-Check" mekanizmasıdır.
* **Analiz ve Parmak İzi Katmanı (BotDetectionAnalyzer):** 15'ten fazla siber güvenlik kriterini (Canvas, WebGL, Audio vb.) test eden ana motordur.
* **Raporlama ve Veri Katmanı:** Analiz sonuçlarını hem görsel (Screenshot) hem de teknik (JSON/TXT) raporlara dönüştürür.

---

## 2. Mantıksal Akış Şeması (Workflow)

Proje çalıştırıldığında şu süreçleri takip eder:

1. **Initialize:** `project_info.json` üzerinden meta veriler okunur.
2. **Self-Check:** Sistem bileşenleri doğrulanır. Hata varsa kullanıcı uyarılır.
3. **Browser Orchestration:** Playwright üzerinden seçilen moda (Normal/Stealth) göre izole bir tarayıcı ortamı oluşturulur.
4. **Injection & Collection:** JavaScript tabanlı "Fingerprint Collector" hedef siteye enjekte edilir.
5. **Risk Scoring:** Toplanan veriler ağırlıklı bir algoritma ile puanlanır.

---

## 3. Risk Skorlama Algoritması (Risk Scoring)

Projenin en kritik güvenlik mantığı, tespit edilen tutarsızlıkları puanlamasıdır. Toplam skor  şu şekilde hesaplanır:

* : Kriterin ağırlığı (Örn: WebDriver tespiti = 3 puan)
* : Kriterin varlığı (0 veya 1)

### Puanlama Tablosu:

| Kriter | Puan (Ağırlık) | Neden Önemli? |
| --- | --- | --- |
| **WebDriver** | 3 Puan | Tarayıcının otomasyon tarafından yönetildiğinin en net kanıtıdır. |
| **Automation Flags** | 2 Puan | Selenium veya Puppeteer'a özgü sızıntıları yakalar. |
| **0 Plugins** | 2 Puan | Standart bir kullanıcı tarayıcısında eklenti olmaması şüphelidir. |
| **Hardware Anomaly** | 1 Puan | CPU core sayısının 1 olması gibi sunucu/bot belirtilerini yakalar. |

---

## 4. Anti-Detection (Evasion) Teknikleri

"Stealth Mode" aktif edildiğinde proje şu savunma yöntemlerini uygular:

* **Runtime Masking:** `navigator.webdriver` özelliği `undefined` olarak ezilir.
* **Context Spoofing:** Chrome Runtime ve Permissions API'leri standart bir kullanıcı gibi simüle edilir.
* **Blink Features:** Tarayıcı başlatılırken otomasyon bayrakları (`AutomationControlled`) devre dışı bırakılır.

---

## 5. Klasör Yapısı ve Standartlar

Proje, "Açık Kaynak İşletim Sistemi Projesi" yönergelerine tam uyumlu olarak organize edilmiştir:

* `src/`: Kaynak kodlar.
* `tests/`: Otomatik test senaryoları (Pytest).
* `specs/`: Proje teknik gereksinimleri (`project_info.json`).
* `researchs/`: AI destekli araştırma çıktıları.

---


