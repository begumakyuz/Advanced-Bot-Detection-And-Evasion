"""
Bot Detection Analyzer
======================
Web sitelerinin bot tespiti için kullandığı tüm temel kriterleri analiz eden profesyonel araç.

Kontrol Edilen Kriterler:
- WebDriver varlığı
- Browser Plugin'leri
- Canvas Fingerprinting
- WebGL Fingerprinting
- Audio Context
- Screen Resolution & Color Depth
- Hardware Concurrency
- Timezone & Language
- User Agent
- Mouse ve Touch Events
- Automation Flags
"""

import logging
import json
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Profesyonel Loglama Yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_detection_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class BotDetectionAnalyzer:
    """Web sitelerinin bot tespit mekanizmalarını analiz eden sınıf"""
    
    def __init__(self, headless: bool = True, stealth_mode: bool = False):
        """
        Args:
            headless: Tarayıcıyı gizli modda çalıştır
            stealth_mode: Anti-detection önlemleri aktif et
        """
        self.headless = headless
        self.stealth_mode = stealth_mode
        self.results = {}
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Çıktı klasörünü oluştur
        self.output_dir = Path("assets/bot_analysis")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def inject_fingerprint_collector(self, page):
        """Tarayıcı parmak izi verilerini toplayan JavaScript kodunu enjekte et"""
        
        fingerprint_script = """
        () => {
            const fingerprint = {
                // 1. WebDriver Tespiti
                webdriver: {
                    present: navigator.webdriver,
                    chromeDriver: window.chrome?.runtime !== undefined,
                    permissions: navigator.permissions?.query !== undefined
                },
                
                // 2. Automation Flags
                automation: {
                    selenium: window.document.$cdc_asdjflasutopfhvcZLmcfl_ !== undefined,
                    domAutomation: window.domAutomation !== undefined,
                    phantom: window._phantom !== undefined || window.callPhantom !== undefined,
                    nightmare: window.__nightmare !== undefined
                },
                
                // 3. Browser Plugins & MIME Types
                plugins: {
                    count: navigator.plugins.length,
                    list: Array.from(navigator.plugins).map(p => ({
                        name: p.name,
                        description: p.description
                    })),
                    mimeTypes: navigator.mimeTypes.length
                },
                
                // 4. Canvas Fingerprinting
                canvas: (() => {
                    try {
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');
                        ctx.textBaseline = 'top';
                        ctx.font = '14px Arial';
                        ctx.fillStyle = '#f60';
                        ctx.fillRect(125, 1, 62, 20);
                        ctx.fillStyle = '#069';
                        ctx.fillText('Bot Detection Test 🤖', 2, 15);
                        return canvas.toDataURL().slice(-50);
                    } catch(e) {
                        return 'error';
                    }
                })(),
                
                // 5. WebGL Fingerprinting
                webgl: (() => {
                    try {
                        const canvas = document.createElement('canvas');
                        const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
                        if (!gl) return null;
                        
                        const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                        return {
                            vendor: gl.getParameter(gl.VENDOR),
                            renderer: gl.getParameter(gl.RENDERER),
                            unmaskedVendor: debugInfo ? gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL) : null,
                            unmaskedRenderer: debugInfo ? gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL) : null
                        };
                    } catch(e) {
                        return 'error';
                    }
                })(),
                
                // 6. Audio Context
                audio: (() => {
                    try {
                        const AudioContext = window.AudioContext || window.webkitAudioContext;
                        if (!AudioContext) return null;
                        
                        const context = new AudioContext();
                        const oscillator = context.createOscillator();
                        const analyser = context.createAnalyser();
                        const gainNode = context.createGain();
                        const scriptProcessor = context.createScriptProcessor(4096, 1, 1);
                        
                        gainNode.gain.value = 0;
                        oscillator.connect(analyser);
                        analyser.connect(scriptProcessor);
                        scriptProcessor.connect(gainNode);
                        gainNode.connect(context.destination);
                        
                        oscillator.start(0);
                        const fingerprint = analyser.frequencyBinCount.toString();
                        
                        context.close();
                        return fingerprint;
                    } catch(e) {
                        return 'error';
                    }
                })(),
                
                // 7. Screen & Hardware Info
                hardware: {
                    screenResolution: `${screen.width}x${screen.height}`,
                    availableResolution: `${screen.availWidth}x${screen.availHeight}`,
                    colorDepth: screen.colorDepth,
                    pixelDepth: screen.pixelDepth,
                    hardwareConcurrency: navigator.hardwareConcurrency,
                    deviceMemory: navigator.deviceMemory,
                    maxTouchPoints: navigator.maxTouchPoints
                },
                
                // 8. Browser Info
                browser: {
                    userAgent: navigator.userAgent,
                    language: navigator.language,
                    languages: navigator.languages,
                    platform: navigator.platform,
                    vendor: navigator.vendor,
                    cookieEnabled: navigator.cookieEnabled,
                    doNotTrack: navigator.doNotTrack,
                    productSub: navigator.productSub,
                    appVersion: navigator.appVersion
                },
                
                // 9. Timezone & Location
                timezone: {
                    offset: new Date().getTimezoneOffset(),
                    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
                    locale: Intl.DateTimeFormat().resolvedOptions().locale
                },
                
                // 10. Window Properties
                window: {
                    innerWidth: window.innerWidth,
                    innerHeight: window.innerHeight,
                    outerWidth: window.outerWidth,
                    outerHeight: window.outerHeight,
                    devicePixelRatio: window.devicePixelRatio
                },
                
                // 11. Performance & Timing
                performance: {
                    timeOrigin: performance.timeOrigin,
                    timing: performance.timing ? {
                        navigationStart: performance.timing.navigationStart,
                        loadEventEnd: performance.timing.loadEventEnd
                    } : null
                },
                
                // 12. Permissions
                permissions: {
                    notificationsAPI: 'Notification' in window,
                    geolocationAPI: 'geolocation' in navigator,
                    storageAPI: 'storage' in navigator
                },
                
                // 13. CSS Media Queries
                mediaQueries: {
                    anyHover: window.matchMedia('(any-hover: hover)').matches,
                    anyPointer: window.matchMedia('(any-pointer: fine)').matches,
                    prefersColorScheme: window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
                },
                
                // 14. Battery API
                battery: 'getBattery' in navigator,
                
                // 15. Connection Info
                connection: navigator.connection ? {
                    effectiveType: navigator.connection.effectiveType,
                    downlink: navigator.connection.downlink,
                    rtt: navigator.connection.rtt,
                    saveData: navigator.connection.saveData
                } : null
            };
            
            return fingerprint;
        }
        """
        
        return page.evaluate(fingerprint_script)
    
    def analyze_site(self, url: str, site_name: str):
        """Belirli bir test sitesini analiz et"""
        
        logger.info(f"🔍 {site_name} analiz ediliyor...")
        
        try:
            with sync_playwright() as p:
                # Tarayıcı başlatma seçenekleri
                launch_options = {
                    'headless': self.headless,
                    'args': []
                }
                
                if self.stealth_mode:
                    # Anti-detection argümanları
                    launch_options['args'].extend([
                        '--disable-blink-features=AutomationControlled',
                        '--disable-dev-shm-usage',
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-web-security',
                        '--disable-features=IsolateOrigins,site-per-process'
                    ])
                
                browser = p.chromium.launch(**launch_options)
                
                # Context oluştur
                context = browser.new_context(
                    viewport={'width': 1920, 'height': 1080},
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    locale='tr-TR',
                    timezone_id='Europe/Istanbul'
                )
                
                if self.stealth_mode:
                    # WebDriver özelliğini gizle
                    context.add_init_script("""
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                        });
                        
                        // Chrome runtime'ı ekle
                        window.chrome = {
                            runtime: {}
                        };
                        
                        // Permissions API'yi düzelt
                        const originalQuery = window.navigator.permissions.query;
                        window.navigator.permissions.query = (parameters) => (
                            parameters.name === 'notifications' ?
                                Promise.resolve({ state: Notification.permission }) :
                                originalQuery(parameters)
                        );
                    """)
                
                page = context.new_page()
                
                # Siteye git
                page.goto(url, wait_until='networkidle', timeout=30000)
                page.wait_for_timeout(3000)  # Sayfanın tam yüklenmesi için bekle
                
                # Ekran görüntüsü al
                screenshot_path = self.output_dir / f"{site_name}_{self.timestamp}.png"
                page.screenshot(path=str(screenshot_path), full_page=True)
                logger.info(f"📸 Screenshot kaydedildi: {screenshot_path}")
                
                # Parmak izi verilerini topla
                fingerprint_data = self.inject_fingerprint_collector(page)
                
                # Sonuçları kaydet
                self.results[site_name] = {
                    'url': url,
                    'timestamp': datetime.now().isoformat(),
                    'screenshot': str(screenshot_path),
                    'fingerprint': fingerprint_data
                }
                
                browser.close()
                logger.info(f"✅ {site_name} analizi tamamlandı")
                
        except PlaywrightTimeout:
            logger.error(f"❌ {site_name} - Timeout hatası (sayfa yüklenmedi)")
        except Exception as e:
            logger.error(f"❌ {site_name} - Hata: {str(e)}")
    
    def generate_report(self):
        """Detaylı analiz raporu oluştur"""
        
        report_lines = [
            "=" * 80,
            "BOT DETECTION ANALYSIS REPORT",
            "=" * 80,
            f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Mod: {'Headless' if self.headless else 'Headed'} | Stealth: {'Aktif' if self.stealth_mode else 'Pasif'}",
            "=" * 80,
            ""
        ]
        
        for site_name, data in self.results.items():
            fp = data['fingerprint']
            
            report_lines.extend([
                f"\n{'=' * 80}",
                f"📊 {site_name.upper()}",
                f"{'=' * 80}",
                f"URL: {data['url']}",
                ""
            ])
            
            # 1. WebDriver Tespiti
            report_lines.extend([
                "🤖 WEBDRIVER TESPİTİ:",
                f"   • navigator.webdriver: {fp['webdriver']['present']}",
                f"   • Chrome Driver: {fp['webdriver']['chromeDriver']}",
                f"   • Permissions API: {fp['webdriver']['permissions']}",
                ""
            ])
            
            # 2. Automation Flags
            report_lines.extend([
                "🚩 AUTOMATION FLAGS:",
                f"   • Selenium: {fp['automation']['selenium']}",
                f"   • DOM Automation: {fp['automation']['domAutomation']}",
                f"   • PhantomJS: {fp['automation']['phantom']}",
                f"   • Nightmare: {fp['automation']['nightmare']}",
                ""
            ])
            
            # 3. Plugins
            report_lines.extend([
                "🔌 BROWSER PLUGINS:",
                f"   • Plugin Sayısı: {fp['plugins']['count']}",
                f"   • MIME Types: {fp['plugins']['mimeTypes']}",
                ""
            ])
            
            # 4. Hardware Info
            report_lines.extend([
                "💻 HARDWARE INFO:",
                f"   • Screen: {fp['hardware']['screenResolution']}",
                f"   • Color Depth: {fp['hardware']['colorDepth']}-bit",
                f"   • CPU Cores: {fp['hardware']['hardwareConcurrency']}",
                f"   • Device Memory: {fp['hardware']['deviceMemory']} GB" if fp['hardware']['deviceMemory'] else "   • Device Memory: N/A",
                f"   • Touch Points: {fp['hardware']['maxTouchPoints']}",
                ""
            ])
            
            # 5. Browser Info
            report_lines.extend([
                "🌐 BROWSER INFO:",
                f"   • Platform: {fp['browser']['platform']}",
                f"   • Language: {fp['browser']['language']}",
                f"   • Vendor: {fp['browser']['vendor']}",
                f"   • Cookies: {fp['browser']['cookieEnabled']}",
                ""
            ])
            
            # 6. Canvas & WebGL
            report_lines.extend([
                "🎨 CANVAS & WEBGL:",
                f"   • Canvas Hash: {fp['canvas'][:30]}..." if fp['canvas'] != 'error' else "   • Canvas: Error",
                f"   • WebGL Vendor: {fp['webgl']['vendor']}" if fp['webgl'] and fp['webgl'] != 'error' else "   • WebGL: Error",
                ""
            ])
            
            # 7. Risk Skorlama
            risk_score = self.calculate_risk_score(fp)
            risk_level = "🔴 YÜKSEK" if risk_score >= 7 else "🟡 ORTA" if risk_score >= 4 else "🟢 DÜŞÜK"
            
            report_lines.extend([
                "⚠️ BOT RİSK SKORU:",
                f"   • Skor: {risk_score}/10",
                f"   • Risk Seviyesi: {risk_level}",
                ""
            ])
        
        # Raporu kaydet
        report_text = "\n".join(report_lines)
        report_path = self.output_dir / f"analysis_report_{self.timestamp}.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        # JSON formatında da kaydet
        json_path = self.output_dir / f"fingerprint_data_{self.timestamp}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        logger.info(f"📄 Rapor kaydedildi: {report_path}")
        logger.info(f"📄 JSON data kaydedildi: {json_path}")
        
        # Terminal'e yazdır
        print("\n" + report_text)
    
    def calculate_risk_score(self, fingerprint: dict) -> int:
        """Bot tespit riski skorunu hesapla (0-10)"""
        
        risk = 0
        
        # WebDriver var mı?
        if fingerprint['webdriver']['present']:
            risk += 3
        
        # Automation flag var mı?
        if any(fingerprint['automation'].values()):
            risk += 2
        
        # Plugin sayısı çok mu az?
        if fingerprint['plugins']['count'] == 0:
            risk += 2
        
        # Hardware concurrency mantıklı mı?
        if fingerprint['hardware']['hardwareConcurrency'] is None or fingerprint['hardware']['hardwareConcurrency'] < 2:
            risk += 1
        
        # Touch points var mı?
        if fingerprint['hardware']['maxTouchPoints'] == 0:
            risk += 1
        
        # Canvas hash alınabildi mi?
        if fingerprint['canvas'] == 'error':
            risk += 1
        
        return min(risk, 10)  # Max 10


def main():
    """Ana çalıştırma fonksiyonu"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║         🤖 BOT DETECTION ANALYZER v2.0 🤖                ║
    ║                                                           ║
    ║  Web sitelerinin bot tespit mekanizmalarını analiz eder  ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Kullanıcıdan mod seçimi
    print("\n🎛️  MOD SEÇİMİ:")
    print("1. Normal Mod (Tespit edilebilir)")
    print("2. Stealth Mod (Anti-detection aktif)")
    
    mode = input("\nSeçiminiz (1/2) [varsayılan: 1]: ").strip() or "1"
    stealth_mode = mode == "2"
    
    # Headless seçimi
    print("\n👁️  GÖRÜNÜM MODU:")
    print("1. Headless (Gizli, hızlı)")
    print("2. Headed (Tarayıcı görünür)")
    
    view_mode = input("\nSeçiminiz (1/2) [varsayılan: 1]: ").strip() or "1"
    headless = view_mode == "1"
    
    # Analyzer oluştur
    analyzer = BotDetectionAnalyzer(headless=headless, stealth_mode=stealth_mode)
    
    # Test siteleri
    test_sites = [
        ("https://bot.sannysoft.com/", "sannysoft"),
        ("https://pixelscan.net/", "pixelscan"),
        ("https://arh.antoinevastel.com/bots/areyouheadless", "areyouheadless"),
        ("https://deviceandbrowserinfo.com/are_you_a_bot", "deviceinfo")
    ]
    
    print(f"\n🚀 Analiz başlatılıyor...")
    print(f"📁 Çıktı klasörü: {analyzer.output_dir}")
    print(f"🎭 Mod: {'Stealth' if stealth_mode else 'Normal'}")
    print(f"👁️  Görünüm: {'Headless' if headless else 'Headed'}\n")
    
    # Her siteyi analiz et
    for url, name in test_sites:
        try:
            analyzer.analyze_site(url, name)
        except KeyboardInterrupt:
            logger.warning("\n⚠️  Kullanıcı tarafından durduruldu")
            break
        except Exception as e:
            logger.error(f"❌ Beklenmeyen hata: {e}")
            continue
    
    # Rapor oluştur
    if analyzer.results:
        print("\n" + "=" * 80)
        analyzer.generate_report()
        print("=" * 80)
        print(f"\n✅ Analiz tamamlandı! Sonuçlar '{analyzer.output_dir}' klasöründe.")
    else:
        print("\n❌ Hiçbir site başarıyla analiz edilemedi.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program sonlandırıldı.")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
