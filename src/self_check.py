#!/usr/bin/env python3
"""
Self-Check Script for Bot Detection Analyzer
============================================
Bu script, ana programı çalıştırmadan önce sistem sağlığını kontrol eder.

Kullanım:
    python self_check.py                    # Tam kontrol
    python self_check.py --quick            # Hızlı kontrol
    python self_check.py --save-report      # Rapor kaydet
"""

import sys
import argparse
from pathlib import Path

# Ana script'i import et
try:
    from bot_detection_analyzer import SystemHealthChecker
except ImportError:
    print("❌ bot_detection_analyzer.py bulunamadı!")
    print("Bu script'i bot_detection_analyzer.py ile aynı klasörde çalıştırın.")
    sys.exit(1)


def parse_arguments():
    """Komut satırı argümanlarını parse et"""
    parser = argparse.ArgumentParser(
        description='Bot Detection Analyzer için sistem sağlık kontrolü',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  python self_check.py                  # Tam kontrol
  python self_check.py --quick          # Hızlı kontrol (network/browser atla)
  python self_check.py --save-report    # Raporu JSON olarak kaydet
  python self_check.py -q -s            # Hızlı kontrol + rapor kaydet
        """
    )
    
    parser.add_argument(
        '-q', '--quick',
        action='store_true',
        help='Hızlı kontrol (network ve browser testlerini atla)'
    )
    
    parser.add_argument(
        '-s', '--save-report',
        action='store_true',
        help='Kontrol raporunu JSON dosyası olarak kaydet'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='assets/health_check_report.json',
        help='Rapor dosyasının yolu (varsayılan: assets/health_check_report.json)'
    )
    
    parser.add_argument(
        '--no-network',
        action='store_true',
        help='Network testlerini atla'
    )
    
    parser.add_argument(
        '--no-browser',
        action='store_true',
        help='Browser testlerini atla'
    )
    
    return parser.parse_args()


def main():
    """Ana fonksiyon"""
    args = parse_arguments()
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║          🛠️  SYSTEM HEALTH CHECK 🛠️                      ║
    ║                                                           ║
    ║         Bot Detection Analyzer Self-Check Tool           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # SystemHealthChecker oluştur
    checker = SystemHealthChecker()
    
    # Kontrol parametreleri
    skip_network = args.quick or args.no_network
    skip_browser = args.quick or args.no_browser
    
    if args.quick:
        print("⚡ HIZLI KONTROL MODU (Network ve Browser testleri atlanıyor)\n")
    
    # Tüm kontrolleri çalıştır
    success = checker.run_all_checks(
        skip_network=skip_network,
        skip_browser=skip_browser
    )
    
    # Rapor kaydetme
    if args.save_report:
        checker.save_report(args.output)
    
    # Çıkış kodu
    if success:
        print("\n✅ Sistem sağlıklı! Bot Detection Analyzer çalıştırılabilir.\n")
        sys.exit(0)
    else:
        print("\n❌ Kritik hatalar var! Lütfen önce bunları düzeltin.\n")
        print("💡 Öneriler:")
        print("   1. requirements.txt'i yükleyin: pip install -r requirements.txt")
        print("   2. Playwright browser'ları kurun: playwright install chromium")
        print("   3. Python versiyonunuzu kontrol edin (min. 3.8)")
        print()
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Kullanıcı tarafından iptal edildi.")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
