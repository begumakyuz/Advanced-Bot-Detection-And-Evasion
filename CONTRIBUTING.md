# Contributing to Bot Detection Analyzer

🎉 Katkılarınızı bekliyoruz!

## 🚀 Hızlı Başlangıç

1. **Fork & Clone**
```bash
   git clone https://github.com/YOUR_USERNAME/Advanced-Bot-Detection-And-Evasion.git
   cd Advanced-Bot-Detection-And-Evasion
```

2. **Development Environment**
```bash
   pip install -r requirements.txt
   playwright install chromium
   python self_check.py
```

3. **Branch Oluştur**
```bash
   git checkout -b feature/amazing-feature
```

4. **Değişiklikleri Yap**
   - Kod yazarken PEP 8 standartlarına uy
   - Self-check'i çalıştır: `python self_check.py`
   - Test ekle: `tests/test_your_feature.py`

5. **Test Et**
```bash
   pytest tests/
```

6. **Commit & Push**
```bash
   git commit -m "feat: Add amazing feature"
   git push origin feature/amazing-feature
```

7. **Pull Request Aç**

## 📝 Commit Mesaj Formatı

- `feat:` Yeni özellik
- `fix:` Bug fix
- `docs:` Dokümantasyon
- `test:` Test ekleme/düzeltme
- `refactor:` Kod iyileştirme
- `style:` Formatting değişiklikleri

## 🧪 Test Gereksinimleri

- Tüm yeni özellikler için test yazılmalı
- Test coverage %80'in üzerinde olmalı
- Self-check başarılı olmalı

## 🤝 Code Review

- En az 1 onay gerekli
- CI/CD testleri geçmeli
- Kod PEP 8 uyumlu olmalı
