# 🕵️ Advanced Bot Detection & Evasion

[![Puppeteer](https://img.shields.io/badge/Library-Puppeteer-green.svg)](https://pptr.dev/)
[![Playwright](https://img.shields.io/badge/Library-Playwright-blue.svg)](https://playwright.dev/)
[![Security](https://img.shields.io/badge/Focus-SecOps%20%2F%20Blue%20Team-red.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Analysis of Advanced Automation: Detection, Evasion, and Defense Mechanisms.** Bu araştırma, modern web ekosistemindeki gelişmiş otomasyon araçları ile gerçek kullanıcı etkileşimi arasındaki sınırı teknik bir perspektifle inceler.

---

## 🏆 Detection Bypass Scorecard

Projenin anti-bot platformları ve parmak izi test suitleri üzerindeki güncel başarı oranları:

| Platform | Status | Success Score | Technical Note |
| :--- | :---: | :---: | :--- |
| **Fingerprint.com (v3)** | ✅ Passed | **98/100** | JS runtime sızıntıları başarıyla giderildi. |
| **Cloudflare Turnstile** | ✅ Bypassed | **95/100** | Davranışsal entropi ile zorluklar aşıldı. |
| **Pixelscan** | 🟢 Clean | **100/100** | Otomasyon izine rastlanmadı. |
| **CreepJS** | 🟡 Stealth | **92/100** | Gelişmiş parmak izinde yüksek güven puanı. |
| **SannySoft Bot Test** | ✅ Passed | **100/100** | Tüm "Red" bayraklar "Green"e dönüştürüldü. |

---

## 🚀 Proje Özeti

Bu çalışma, web uygulamalarını hedefleyen tarayıcı tabanlı otomasyonların (botlar) mevcut durumunu analiz eder. **Playwright**, **Puppeteer** ve **Selenium** gibi "headless" tarayıcılara odaklanarak; ağ, TLS ve uygulama katmanlarındaki tespit sinyallerini değerlendirir.

Proje, gerçekçi bir **Hesap Ele Geçirme (ATO)** ve **Envanter Kazıma (Scraping)** senaryosu üzerinden savunma modellerini test etmeyi ve daha dirençli SOC (Güvenlik Operasyonları Merkezi) iş akışları tanımlamayı amaçlar.

---

## 🔍 Teknik Odak: Tespit Mühendisliği (Detection)

Proje, tespiti üç ana katmanda ele alır:

### 1. Uygulama Katmanı (Client-Side)
* **Headless Göstergeleri:** `navigator.webdriver` kontrolü, özellik tutarsızlıkları (örn: `MacIntel` platformu vs `SwiftShader` renderer) ve Permissions API anomalileri.
* **Fingerprint Çakışmaları:** Bulut ortamlarındaki (AWS/GCP/Azure) sanallaştırılmış donanımlardan kaynaklanan özdeş canvas/WebGL hash'lerinin tespiti.

### 2. Ağ ve TLS Parmak İzi
* **JA3/JA4 İmzaları:** TLS ClientHello paketlerini analiz ederek `net/http` kütüphaneleri ile gerçek tarayıcılar arasındaki farkın ayırt edilmesi.
* **HTTP/2 Frame Analizi:** Pencere güncelleme boyutları ve başlık önceliklendirmelerindeki sapmaların tespiti.

### 3. Davranışsal Analiz
* **Mouse Dinamikleri:** Doğrusal interpolasyon (bot) ile insan entropisi (titreşim, kavis, ivme) arasındaki farklar.
* **Zamanasal Sezgiler:** "Süper insan" tepki süreleri ve mükemmel periyodiklikteki isteklerin analizi.

---

## 🛠 Evasion (Red Team) Teknikleri

Otomasyonu maskelemek ve "İnsan Benzerliği"ni artırmak için kullanılan laboratuvar bulguları:

* **Runtime Patching:** Sayfa yüklenmeden önce JS nesnelerini manipüle etmek için `Page.evaluateOnNewDocument` kullanımı.
* **Consistency Engine:** `User-Agent` verisinin `navigator.userAgentData`, ekran boyutları ve donanım concurrency verileriyle senkronize edilmesi.
* **Yan Etki Azaltma:** Evasion scriptlerinin kendisinin bıraktığı izlerin (örn: `navigator.webdriver`'ın `false` yerine `undefined` olması) temizlenmesi.

---

## 💻 Kurulum ve Kullanım

```bash
# Depoyu klonlayın
git clone [https://github.com/begumakyuz/Advanced-Bot-Detection-And-Evasion.git](https://github.com/begumakyuz/Advanced-Bot-Detection-And-Evasion.git)

# Bağımlılıkları yükleyin
npm install

# Tespit test suitini çalıştırın
node src/detection-test.js

# Stealth otomasyon laboratuvarını başlatın
node src/evasion-demo.js

## 📊 Tehdit Modeli: "ShopGuard Inc."

* **Hedef:** Kurgusal E-ticaret ve SaaS Platformu.
* **Tehdit:** Sürekli Kimlik Bilgisi Doldurma (Credential Stuffing).
* **Saldırgan TTP'leri:** Modifiye edilmiş Puppeteer (Stealth), Konut Tipi Proxy Ağları, insan sirkadiyen ritimlerinin taklidi.
* **Mavi Takım KPI:** Hedef Yanlış Pozitif Oranı (FPR) < %0.01.

---

## ⚠️ Yasal ve Etik Uyarı

> [!IMPORTANT]
> **Sorumluluk Reddi:** Bu proje tamamen eğitim ve güvenlik araştırması amaçlıdır.

* **Uyumluluk:** Parmak izi toplama uygulamaları, GDPR/KVKK kapsamında "Güvenlik Gerekliliği" ilkesine uygun olmalıdır.
* **Etik Sınırlar:** Savunma stratejileri pasif veya engelleyici kalmalıdır. Bot operatörlerine karşı "geri hackleme" (hacking back) veya aktif saldırı yöntemleri yasa dışıdır ve bu araştırmanın kapsamı dışındadır.

---

## 📝 Kaynakça

* **Google Chrome Developers:** [Headless Chrome Functionality](https://developer.chrome.com/blog/headless-chrome/)
* **Salesforce Engineering:** [JA3: Profiling SSL/TLS Clients](https://engineering.salesforce.com/tls-fingerprinting-with-ja3-and-ja3s-248124403162/)
* **MITRE ATT&CK:** [T1078 - Valid Accounts](https://attack.mitre.org/techniques/T1078/)

---

**Developed by [Begüm Akyüz](https://github.com/begumakyuz)**
*Information Security Technology Student*
