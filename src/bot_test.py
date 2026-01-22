import asyncio
from playwright.async_api import async_playwright

async def run_bot_test():
    async with async_playwright() as p:
        # Tarayıcıyı başlatıyoruz
        browser = await p.chromium.launch(headless=False)
        
        # Gerçek bir kullanıcı profili oluşturuyoruz
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=1,
        )
        
        page = await context.new_page()

        # --- MANUEL EVASION (KAÇINMA) BAŞLIYOR ---
        # Bu script, tarayıcı sayfayı yüklemeden hemen önce çalışır ve izleri siler.
        await page.add_init_script("""
            // 1. WebDriver bayrağını tamamen siler
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            
            // 2. Chrome nesnesini varmış gibi gösterir (Headless Chrome'da bu boştur)
            window.chrome = { runtime: {} };
            
            // 3. Donanım özelliklerini gerçekçi değerlerle değiştirir
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });
            Object.defineProperty(navigator, 'languages', { get: () => ['tr-TR', 'tr', 'en-US'] });
            
            // 4. Eklentiler varmış gibi yapar
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
        """)
        # --- MANUEL EVASION BİTTİ ---

        print("Bot test sitesine gidiliyor... Bu sefer hata vermeyecek.")
        try:
            # Test sitesine git
            await page.goto("https://bot.sannysoft.com/", wait_until="domcontentloaded")
            
            print("Sayfa açıldı! Sonuçları incelemek için 20 saniye süren var.")
            await asyncio.sleep(20)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
        finally:
            await browser.close()
            print("Tarayıcı kapatıldı.")

if __name__ == "__main__":
    asyncio.run(run_bot_test())
