#!/usr/bin/env python3
"""
Self-Check Kullanım Örnekleri
============================
Bu dosya, SystemHealthChecker sınıfının nasıl kullanılacağını gösterir.
"""

from bot_detection_analyzer import SystemHealthChecker
import json


def example_1_basic_check():
    """Örnek 1: Temel kontrol"""
    print("=" * 80)
    print("ÖRNEK 1: TEMEL KONTROL")
    print("=" * 80)
    
    checker = SystemHealthChecker()
    success = checker.run_all_checks()
    
    if success:
        print("\n✅ Sistem hazır!")
    else:
        print("\n❌ Sorunlar var!")
        print(f"Hatalar: {checker.errors}")


def example_2_quick_check():
    """Örnek 2: Hızlı kontrol (network ve browser testleri atla)"""
    print("\n" + "=" * 80)
    print("ÖRNEK 2: HIZLI KONTROL")
    print("=" * 80)
    
    checker = SystemHealthChecker()
    success = checker.run_all_checks(skip_network=True, skip_browser=True)
    
    print(f"\nSonuç: {'✅ Başarılı' if success else '❌ Başarısız'}")


def example_3_with_report():
    """Örnek 3: Rapor kaydetme"""
    print("\n" + "=" * 80)
    print("ÖRNEK 3: RAPOR KAYDETME")
    print("=" * 80)
    
    checker = SystemHealthChecker()
    checker.run_all_checks()
    
    # Raporu kaydet
    report_path = "assets/my_health_report.json"
    checker.save_report(report_path)
    
    # Raporu oku ve göster
    with open(report_path, 'r') as f:
        report = json.load(f)
    
    print(f"\n📄 Rapor özeti:")
    print(f"   • Toplam test: {report['summary']['total_checks']}")
    print(f"   • Başarılı: {report['summary']['passed']}")
    print(f"   • Uyarı: {report['summary']['warnings']}")
    print(f"   • Hata: {report['summary']['errors']}")


def example_4_custom_checks():
    """Örnek 4: Özel kontroller"""
    print("\n" + "=" * 80)
    print("ÖRNEK 4: ÖZEL KONTROLLER")
    print("=" * 80)
    
    checker = SystemHealthChecker()
    
    # Sadece belirli kontrolleri çalıştır
    print("\n🔍 Python versiyonu kontrol ediliyor...")
    checker.check_python_version()
    
    print("\n🔍 Playwright kontrol ediliyor...")
    checker.check_playwright_installation()
    
    print("\n🔍 Dosya sistemi kontrol ediliyor...")
    checker.check_directory_structure()
    
    # Sonuçları göster
    checker.print_summary()


def example_5_error_handling():
    """Örnek 5: Hata yönetimi"""
    print("\n" + "=" * 80)
    print("ÖRNEK 5: HATA YÖNETİMİ")
    print("=" * 80)
    
    checker = SystemHealthChecker()
    
    try:
        success = checker.run_all_checks()
        
        if not success:
            print("\n⚠️  Hatalar tespit edildi:")
            for i, error in enumerate(checker.errors, 1):
                print(f"   {i}. {error}")
            
            print("\n💡 Önerilen çözümler:")
            if "Playwright" in str(checker.errors):
                print("   → pip install playwright && playwright install chromium")
            if "Python" in str(checker.errors):
                print("   → Python 3.8+ sürümüne yükseltin")
            if "izni" in str(checker.errors):
                print("   → Klasör yazma izinlerini kontrol edin")
    
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")


def example_6_conditional_execution():
    """Örnek 6: Koşullu çalıştırma"""
    print("\n" + "=" * 80)
    print("ÖRNEK 6: KOŞULLU ÇALIŞTIRMA")
    print("=" * 80)
    
    # Önce health check yap
    checker = SystemHealthChecker()
    success = checker.run_all_checks(skip_network=True, skip_browser=True)
    
    # Sadece başarılıysa devam et
    if success:
        print("\n✅ Sistem sağlıklı! Ana program çalıştırılabilir.")
        print("🚀 Bot Detection Analyzer başlatılıyor...")
        # Burada ana programınızı çalıştırabilirsiniz
    else:
        print("\n❌ Sistem hazır değil! Lütfen önce sorunları çözün.")
        print(f"📋 Hata sayısı: {len(checker.errors)}")
        print(f"⚠️  Uyarı sayısı: {len(checker.warnings)}")


def main():
    """Tüm örnekleri çalıştır"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║        📚 SELF-CHECK KULLANIM ÖRNEKLERİ 📚              ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    examples = [
        ("Temel Kontrol", example_1_basic_check),
        ("Hızlı Kontrol", example_2_quick_check),
        ("Rapor Kaydetme", example_3_with_report),
        ("Özel Kontroller", example_4_custom_checks),
        ("Hata Yönetimi", example_5_error_handling),
        ("Koşullu Çalıştırma", example_6_conditional_execution)
    ]
    
    print("\nHangi örneği çalıştırmak istersiniz?")
    for i, (name, _) in enumerate(examples, 1):
        print(f"{i}. {name}")
    print("0. Tüm örnekleri çalıştır")
    
    try:
        choice = input("\nSeçiminiz (0-6): ").strip()
        
        if choice == "0":
            for name, func in examples:
                input(f"\n▶️  {name} örneği çalıştırılacak. Enter'a basın...")
                func()
        elif choice.isdigit() and 1 <= int(choice) <= len(examples):
            name, func = examples[int(choice) - 1]
            print(f"\n▶️  {name} örneği çalıştırılıyor...\n")
            func()
        else:
            print("❌ Geçersiz seçim!")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"\n❌ Hata: {e}")


if __name__ == "__main__":
    main()
