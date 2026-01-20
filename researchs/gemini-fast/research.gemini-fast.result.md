Advanced Bot Detection & Evasion – An Educational & Defensive PerspectiveThe digital economy is increasingly reliant on the integrity of automated interactions. As organizations migrate to high-traffic e-commerce and Software-as-a-Service (SaaS) models, the distinction between a legitimate human user and a sophisticated automated agent has become a central challenge for cybersecurity researchers. This report examines the technical foundations of bot detection and evasion, analyzing the mechanisms from first principles through advanced protocol-level fingerprinting and behavioral biometrics. By contextualizing these technologies within a real-world scenario of a platform facing credential stuffing, account takeover (ATO), and competitive scraping, this analysis provides a comprehensive educational framework for understanding the ongoing arms race in web security.The Evolution of Automated Threats and Detection PrinciplesThe transition from simple, repetitive scripts to human-emulating artificial intelligence has redefined the perimeter of modern web applications. In a high-traffic e-commerce environment, malicious bots account for a significant portion of traffic, often exceeding human visitors during peak sales events.1 These agents are not merely tools for data collection but are specialized instruments for financial fraud, inventory hoarding, and account compromise. To defend against these threats, the industry has moved from reactive IP-based blocking to proactive, multi-layered detection strategies that interrogate the entire stack, from the network packet to the user’s physical interaction with the device.2Working Principles of Bot DetectionBot detection operates on the fundamental principle of anomaly identification. A system establishes a baseline of "normal" behavior—characterized by human timing, physical device characteristics, and standard browser signatures—and flags any request that deviates from this model.4 This is essentially a distributed, real-time Turing Test. Detection mechanisms are broadly categorized into client-side and server-side methodologies. Client-side detection uses JavaScript to collect environmental data directly from the user's browser, such as hardware specifications and behavioral metrics.6 Server-side detection analyzes the characteristics of the incoming request at the infrastructure level, focusing on network headers, IP reputation, and TLS handshake signatures.7Industry Best Practices for High-Traffic DefenseFor platforms experiencing heavy traffic, reliance on a single detection method is insufficient. Best practices dictate a "defense-in-depth" architecture. This includes placing bot management at the edge (CDN/WAF) to filter high-volume, low-sophistication traffic before it reaches the application origin.2 Organizations must also implement "Adaptive Rate Limiting," which throttles requests based on a combination of IP history and device fingerprinting rather than simple request counts.4 Furthermore, the industry is moving away from traditional CAPTCHAs, which introduce friction for legitimate users, in favor of "Invisible Challenges" like Proof-of-Work (PoW) or behavioral analysis.4Alternatives: Open-Source and CommercialThe market for bot detection is split between enterprise-grade managed services and flexible open-source projects.Solution TypeExamplesKey CharacteristicsCommercialCloudflare, DataDome, Akamai, Human SecurityManaged ML models, global threat intelligence, low implementation effort.1Open-SourceSafeLine WAF, BotD, Fail2Ban, open-appsecFull data control, customizable rules, cost-effective for smaller scales.10FrameworksFingerprintJS, MultiLoginSpecialized libraries for identity and fingerprinting.12Configuration Parameters and Security ConsiderationsWhen configuring a detection system, the primary parameter is the "Bot Score," a numerical value (typically 1-99) indicating the likelihood of automation. A score of 1 represents a definite bot (e.g., a known malicious scraper), while a score of 99 indicates a highly certain human.5 Secondary parameters include the "Challenge Sensitivity," which determines when a user is prompted with an invisible JS challenge. A major security consideration is "False Positive Management." Aggressive detection can block legitimate users, leading to brand abandonment and lost revenue, particularly in e-commerce.3 Consequently, systems must include a "Feedback Loop" to report misclassifications and retrain machine learning models.5First Principles: The Architectural Split of DetectionThe fundamental choice in bot defense is between client-side interrogation and server-side observation. This split dictates the visibility, performance, and resilience of the security posture.Client-Side Interrogation: The Anatomy of the FingerprintClient-side detection relies on the execution of JavaScript to "interrogate" the browser environment. This process, known as fingerprinting, collects dozens of attributes to create a stable identifier for the device.12Working Principles of FingerprintingFingerprinting uses the browser's APIs to reveal the underlying hardware and software configuration. A "Passive Fingerprint" includes headers like the User-Agent and Accept-Language, while an "Active Fingerprint" requires the browser to perform a specific task, such as rendering a hidden image.16 The resulting pixel data is hashed to produce a unique signature. Because different graphics drivers and CPUs render pixels with subtle, sub-pixel variations, the hash becomes a proxy for the hardware itself.12Best Practices and Security ConsiderationsTo ensure the resilience of a fingerprint, developers must avoid "brittle" signals that change frequently, such as the exact browser version or battery level, as these create noise in detection.12 Security is maintained through "Obfuscation" and "Payload Encryption," preventing attackers from modifying the collected data before it is sent to the server.12 In the context of a SaaS platform, a persistent fingerprint allows for the detection of "Session Hijacking," where an attacker steals a cookie but cannot replicate the physical hardware fingerprint associated with the original session.4Server-Side Observation: Protocol-Level IntegrityServer-side detection is invisible to the user and resilient to client-side script blocking. It analyzes the "Web Logs" and protocol signatures that are generated by every HTTP request.7Working Principles: Repetition and LogicAdvanced server-side systems analyze user movement data to detect repeated paths. In the context of e-commerce, a human user’s path through a site is non-linear and variable, while a scraper often follows a fixed script (e.g., Homepage -> Category -> Product -> Scrape -> Back).18 By extracting "waypoints" from coordinates or URL patterns, server-side algorithms can identify movement clusters that indicate script-based control.19Configuration and AlternativesCommon configuration parameters include "IP Reputation Thresholds" and "Geo-location Blocking." Open-source tools like Fail2Ban are commonly used at this layer to block IPs that exhibit brute-force patterns in server logs.10 For high-traffic SaaS platforms, server-side detection is the only viable method for protecting APIs, as APIs do not execute the JavaScript required for client-side detection.7Technical Scope: Headless Indicators and Behavioral BiometricsAs bot developers transitioned to using real browser engines like Chromium to bypass simple detection, security researchers developed techniques to identify when a browser is running in a "headless" or automated mode.Headless Indicators and WebDriver TracesA headless browser is a browser environment without a graphical user interface (GUI), used primarily for testing and automation. While legitimate, their use in production traffic is a high-probability indicator of bot activity.21Working Principles of Headless DetectionSeveral technical markers reveal a headless state:Navigator.webdriver: In most automated environments, this property is set to true by default.16Missing Touch APIs: Real browsers on mobile or touch-enabled laptops expose touchstart and touchmove events. Headless browsers often lack these implementations.23Permissions Mismatch: A headless browser may report that it has "Granted" permission for Notifications without ever prompting a user, a logical impossibility in a standard browser.22Inconsistent Hardware: A browser claiming to be an iPhone (via User-Agent) that reports having 16 CPU cores (via navigator.hardwareConcurrency) is flagged as a forged environment.12Industry Best Practices and SecurityThe primary best practice is "Consistency Validation." Rather than looking for a single flag, systems cross-reference all collected attributes to find "lies" in the environment.12 For security, detection scripts should include "Honeypot Functions"—hidden properties that only a bot's global search of the window object would trigger.23Behavioral Biometrics: The Entropy of Human InteractionBehavioral biometrics shifts the focus from what the device is to how it is being used. This method analyzes the fine-grained timing and physical patterns of a session.4Working Principles of Behavioral AnalysisHuman interaction is characterized by high entropy. Mouse movements are rarely straight lines; they involve acceleration, deceleration, micro-jitters, and occasional overshooting of targets.23 Bots, conversely, move in perfectly linear paths or "teleport" the cursor to the center of an element.4 Timing is another key indicator. A human requires time to read a page before clicking, whereas a bot might submit a form within milliseconds of page load—a pattern known as "Instant Page Interaction".23Alternatives and ConfigurationCommercial solutions like Kasada or Human Security specialize in these high-resolution behavioral signals.17 Configuration parameters often involve "Dwell Time" thresholds and "Interaction Density" metrics. A security consideration here is the protection of user privacy; behavioral data should be processed into an anonymous risk score rather than stored as raw keystroke logs to comply with GDPR and KVKK regulations.25Network Layer Scope: TLS and HTTP/2 FingerprintingIn the most sophisticated e-commerce attacks, bots bypass the application layer entirely and interact directly with APIs. In these scenarios, the only available signals are those found at the network and transport layers.TLS Fingerprinting: JA3 and the JA4 EvolutionTransport Layer Security (TLS) is the protocol used to encrypt web traffic. Every HTTPS connection begins with a "Client Hello" message, which serves as a unique signature of the client's underlying cryptographic library.8Working Principles: The JA3 LegacyJA3 fingerprints a client by extracting five specific fields from the TLS handshake: the version, accepted cipher suites, list of extensions, elliptic curves, and curve formats.28 These values are hashed using MD5. Because different libraries (e.g., OpenSSL vs. Windows SChannel) have different default configurations, the JA3 hash can distinguish a Python script from a Chrome browser with high accuracy.8The JA4 Standard and Best PracticesThe industry is currently transitioning to JA4, which addresses the limitations of JA3. JA3 is sensitive to the order of extensions, which some modern browsers randomize to break fingerprinting. JA4 introduces "Normalization," sorting the fields before hashing to ensure stability.28 JA4 also incorporates "ALPN" (Application-Layer Protocol Negotiation) and "SNI" (Server Name Indication) behavior into its signature, creating a much richer profile.27MetricJA3JA4Format32-character MD5 hashMulti-part, human-readable string.28Cipher OrderSensitive (Brittle)Normalized (Stable).28VisibilityOpaqueTransparent (Counts extensions/ciphers).27ScopeTLS Layer onlyMulti-layer (TCP, TLS, HTTP/2).27HTTP/2 and SETTINGS Frame AnalysisThe shift from HTTP/1.1 to HTTP/2 introduced new fingerprinting surfaces. The HTTP/2 connection starts with a SETTINGS frame where the client defines its capabilities, such as HEADER_TABLE_SIZE and MAX_CONCURRENT_STREAMS.30Working PrinciplesEach browser engine (Chromium, Gecko, WebKit) uses a distinct set of default HTTP/2 settings. For instance, Chrome might suggest an initial window size of 6MB, while a botting library like Go-HTTP might use a much smaller default. Mismatches between the User-Agent (claiming to be Chrome) and the HTTP/2 SETTINGS frame are a primary method for detecting "API-based" bots that do not use a full browser engine.1Configuration and SecurityFor high-traffic SaaS platforms, configuring the WAF to validate HTTP/2 frame consistency is a critical defense against "Hyper-volumetric" DDoS attacks and large-scale credential stuffing.30 Security teams should monitor for "Header Ordering" anomalies, as real browsers follow a strict order (e.g., :method, :authority, :scheme, :path) that simple scripts often fail to replicate.23Browser Automation Tools and the Evasion ArchitectureTo defend against bots, researchers must understand the tools used to create them. Selenium, Puppeteer, and Playwright are the core technologies used for both legitimate testing and malicious automation.Comparative Framework AnalysisThe choice of framework impacts both the performance and the "stealthiness" of the automated agent.FrameworkMechanismLanguage SupportStealth PotentialSeleniumWebDriver over HTTPJava, Python, C#, JSLow (Heavy signatures).32PuppeteerCDP over WebSocketsNode.js (Official)Medium (Requires plugins).34PlaywrightCDP / Multi-engineJS, Python, Java, C#High (Modern, fast, multi-context).35Working Principles: Playwright and the CDPPlaywright represents the state-of-the-art in automation. It communicates directly with the browser's "Chrome DevTools Protocol" (CDP) via a persistent WebSocket connection.36 This architecture allows for "Context Isolation," enabling a single browser process to run multiple independent sessions with different cookies and fingerprints, making it highly efficient for parallel scraping or ATO attacks on SaaS platforms.34Evasion Awareness: The Stealth StackBot evasion is the practice of modifying an automation tool to bypass detection. This is achieved through "Stealth Plugins" that patch the indicators mentioned previously.Working Principles of EvasionPlugins like puppeteer-extra-plugin-stealth work by hooking into the browser's execution cycle before the target website's scripts run. They perform "API Spoofing," such as redefining navigator.languages to return a realistic array or patching HTMLCanvasElement.prototype.toDataURL to add a tiny amount of noise, thereby bypassing canvas fingerprinting.22Best Practices and Security ConsiderationsFrom a defensive perspective, the best practice is to look for "Side Effects" of evasion. For example, if a bot patches a native function, the toString() method of that function might return a non-standard result. Defensive scripts should verify that navigator.webdriver.toString() returns "function get webdriver() { [native code] }" exactly.12 Security considerations also include "Runtime Monitoring," where the system detects the presence of debugging tools or CDP listeners that are active in the browser.12Real-World Scenario: Defensive Architecture for "GlobalCart"GlobalCart is a high-traffic e-commerce and SaaS platform experiencing three simultaneous automated threats: Credential Stuffing on login endpoints, Account Takeover (ATO) through session hijacking, and Price Scraping across its product catalog.Attack Pattern AnalysisThe platform's logs show distinct patterns associated with the OWASP Automated Threats (OAT) taxonomy.ThreatOAT IdentifierObservation in GlobalCart LogsCredential StuffingOAT-008500k failed logins from 20k unique residential IPs; use of stolen username/password pairs.24Account TakeoverOAT-007Spike in "Successful Login" followed by immediate "Change Email" or "Empty Cart" from unusual geolocations.17Price ScrapingOAT-011Millions of requests hitting /api/v1/products/price with a high pageview-to-session ratio and zero "Add to Cart" actions.24Implementing the Multi-Layered DefenseTo mitigate these threats, GlobalCart adopts an integrated strategy across the infrastructure.1. Credential Stuffing Mitigation: NIST and OWASP StandardsFollowing NIST SP 800-63B, GlobalCart implements "Breached Password Protection." During login, the application checks the submitted password against a database of known compromised secrets from previous breaches.39 The platform also uses "Adaptive Throttling" at the WAF level, which doesn't just block by IP, but by the "JA4+ Fingerprint," ensuring that bots cannot evade limits by rotating through residential proxies.42. ATO Prevention: Behavioral and Session IntegrityTo prevent ATO, GlobalCart deploys client-side behavioral biometrics. If a successful login occurs, but the mouse movement patterns or typing speed deviate significantly from the historical "Human Profile" of that account, the system triggers a "Phishing-Resistant MFA" (FIDO2) challenge.17 The system also uses "Device Grouping" to identify if a single physical device is attempting to access hundreds of different user accounts.123. Scraping Defense: Semantic Analysis and Virtual Waiting RoomsFor scraping, GlobalCart utilizes SafeLine WAF's "Semantic Analysis" engine. Instead of looking for simple strings, the engine uses machine learning to understand the intent of the requests. If it identifies a "Scraper Pattern" (e.g., iterating through SKUs), it moves the traffic to a "Virtual Waiting Room," adding a delay (latency) that breaks the economics of the scraper's operation without impacting real customers.11Regulatory Compliance: GDPR, KVKK, and Privacy-First DetectionThe collection of device data for bot detection is governed by strict privacy laws, particularly in Europe (GDPR) and Turkey (KVKK).Legal Frameworks and Data ProcessingUnder both GDPR and KVKK, a high-entropy browser fingerprint is considered "Personal Data" because it can be used to distinguish a specific user's device.25 GlobalCart must establish a legal basis for this processing.Legitimate Interest: Most bot detection is performed under the basis of "Legitimate Interest" (GDPR Art. 6(1)(f)), as it is necessary for the security of the service.26KVKK Specifics: In Turkey, the Personal Data Protection Law (Law No. 6698) requires that data controllers register with the VERBIS system and provide clear "Privacy Notices" explaining that metadata is collected for anti-fraud purposes.25Data Minimization: Industry best practice is to use "One-Way Hashing" for fingerprint attributes. Instead of storing a list of "Installed Fonts," the system stores a salted SHA-256 hash, ensuring that the original data cannot be reconstructed if the security system is breached.26Security Considerations for ComplianceA major risk is "Transitive License Risk." Many open-source detection libraries (like BotD) include dependencies with different licenses (MIT, GPL). Failure to audit these can lead to legal complications during a security audit or a M&A due diligence process.13Visual Educational ComponentsThe Bot Detection Decision Pipeline (Mermaid Diagram)Kod snippet'igraph TD
    A --> B{Network Layer Checks}
    B -->|Fail| C
    B -->|Pass| D{Protocol Fingerprint}
    D -->|Mismatch| E
    D -->|Match| F{Client-Side Interrogation}
    F -->|Headless| G
    F -->|Legit| H{Behavioral Analysis}
    H -->|Bot-like| I
    H -->|Human-like| J[Allow Access to GlobalCart]
Automation Architecture Comparative MatrixFeatureSelenium (Legacy)Playwright (Modern)CommunicationJSON Wire (HTTP)CDP (Binary WebSocket)Speed536ms per click (Avg)290ms per click (Avg).36Memory~19GB for 50 sessions~750MB for 50 contexts.36StealthHigh visibilityNative route interception.35Complete Educational Website Project (HTML/JS/CSS)This code provides a multi-language, theme-supported educational environment for students to test bot detection concepts.HTML<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Detection Education Suite</title>
    <style>
        :root {
            --bg: #ffffff; --text: #1a1a1a; --card: #f8f9fa; --accent: #007bff;
        }
        [data-theme='dark'] {
            --bg: #121212; --text: #e0e0e0; --card: #1e1e1e; --accent: #3700b3;
        }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); transition: 0.3s; margin: 0; padding: 0; }
        nav { background: var(--card); padding: 1rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; }
       .container { max-width: 1000px; margin: 2rem auto; padding: 1rem; }
       .lab-card { background: var(--card); border-radius: 12px; padding: 2rem; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
       .status { padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: bold; }
       .status-danger { background: #ff4d4d; color: white; }
       .status-success { background: #2ecc71; color: white; }
       .controls { margin-top: 1rem; display: flex; gap: 10px; }
        button { padding: 0.6rem 1.2rem; border: none; border-radius: 6px; cursor: pointer; background: var(--accent); color: white; }
    </style>
</head>
<body>
    <nav>
        <div id="nav-brand">Bot Detection Educational Suite v1.0</div>
        <div class="controls">
            <button onclick="toggleLang()">TR / EN</button>
            <button onclick="toggleTheme()">Theme / Tema</button>
        </div>
    </nav>
    <div class="container">
        <div class="lab-card">
            <h2 id="lab-title">Environment Diagnostics</h2>
            <div id="diag-results">
                <p><strong>WebDriver Trace:</strong> <span id="res-wd" class="status">Testing...</span></p>
                <p><strong>Permissions Check:</strong> <span id="res-perm" class="status">Testing...</span></p>
                <p><strong>Hardware Logic:</strong> <span id="res-hw" class="status">Testing...</span></p>
            </div>
            <p id="lab-desc">This lab detects indicators used by systems like Cloudflare and SafeLine.</p>
        </div>
    </div>

    <script>
        const i18n = {
            en: {
                brand: "Bot Detection Educational Suite v1.0",
                title: "Environment Diagnostics",
                desc: "This lab detects indicators used by systems like Cloudflare and SafeLine.",
                bot: "Bot Detected", human: "Human-like", checking: "Checking..."
            },
            tr: {
                brand: "Bot Tespit Eğitim Paketi v1.0",
                title: "Ortam Teşhisi",
                desc: "Bu laboratuvar Cloudflare ve SafeLine gibi sistemler tarafından kullanılan göstergeleri tespit eder.",
                bot: "Bot Tespit Edildi", human: "İnsan Görünümlü", checking: "Kontrol ediliyor..."
            }
        };

        let lang = 'en';
        function toggleLang() {
            lang = lang === 'en'? 'tr' : 'en';
            updateUI();
        }

        function toggleTheme() {
            const current = document.documentElement.getAttribute('data-theme');
            document.documentElement.setAttribute('data-theme', current === 'dark'? 'light' : 'dark');
        }

        function updateUI() {
            document.getElementById('nav-brand').innerText = i18n[lang].brand;
            document.getElementById('lab-title').innerText = i18n[lang].title;
            document.getElementById('lab-desc').innerText = i18n[lang].desc;
            runDiagnostics();
        }

        async function runDiagnostics() {
            // WebDriver Check
            const wd = navigator.webdriver;
            const resWd = document.getElementById('res-wd');
            resWd.innerText = wd? i18n[lang].bot : i18n[lang].human;
            resWd.className = `status ${wd? 'status-danger' : 'status-success'}`;

            // Permissions Check (Headless Indicator)
            try {
                const perm = await navigator.permissions.query({name: 'notifications'});
                const isHeadless = (perm.state === 'granted' &&!('Notification' in window));
                const resPerm = document.getElementById('res-perm');
                resPerm.innerText = isHeadless? i18n[lang].bot : i18n[lang].human;
                resPerm.className = `status ${isHeadless? 'status-danger' : 'status-success'}`;
            } catch(e) {}

            // Hardware Logic (Cores Check)
            const cores = navigator.hardwareConcurrency;
            const resHw = document.getElementById('res-hw');
            resHw.innerText = (cores === 0 |

| cores === undefined)? i18n[lang].bot : `${cores} Cores (${i18n[lang].human})`;
            resHw.className = `status ${(cores === 0)? 'status-danger' : 'status-success'}`;
        }

        updateUI();
    </script>
</body>
</html>
Conclusions and Future OutlookThe landscape of bot detection and evasion is undergoing a fundamental shift driven by the democratization of artificial intelligence. As "Agentic AI" becomes a reality, bots will no longer follow scripts but will possess the ability to make autonomous decisions, mimicking the non-linear logic of human users in real-time.17 This necessitates a move toward "Identity-Based Defense," where the security perimeter is defined by the verified identity of the user rather than the characteristics of the session.For high-traffic e-commerce and SaaS platforms, the challenge is twofold: maintaining a frictionless user experience while defending against an increasingly invisible adversary. The implementation of modern standards like NIST SP 800-63B and the adoption of resilient protocols like JA4 are the first steps toward a more secure digital ecosystem.28 Ultimately, the winner of this technological arms race will be determined by the ability to distinguish between automated execution and human intent with absolute precision, ensuring that the open web remains a space for genuine interaction and economic growth.



sequenceDiagram
    participant User as Actor (Human/Bot)
    participant WAF as Perimeter (WAF)
    participant Challenge as JS Challenge
    participant Server as App Server

    User->>WAF: Initial HTTP GET Request
    Note right of User: Human: "Messy" headers, standard TLS<br/>Bot: Perfect headers, irregular TLS

    alt Known Bad IP
        WAF-->>User: 403 Forbidden
    else Clean IP
        WAF->>Challenge: Forward to Verification
    end

    Challenge->>User: Serve Fingerprint Script
    User-->>Challenge: Return Canvas/Audio Hash

    alt Inconsistent Fingerprint
        Challenge-->>User: CAPTCHA / Block
    else Consistent Fingerprint
        Challenge->>Server: Allow Access
    end

    graph TD
    A[Incoming Request] --> B{Layer 1: Network}
    B -- Datacenter IP --> X[Block]
    B -- Residential IP --> C{Layer 2: Protocol}
    
    C -- Mismatched TLS --> X
    C -- Valid Handshake --> D{Layer 3: Browser Env}
    
    D -- Headless detected --> X
    D -- Consistent Env --> E{Layer 4: Behavior}
    
    E -- Superhuman speed --> X
    E -- Natural Jitter --> F[Allow Traffic]
    
    style X fill:#ff9999,stroke:#333
    style F fill:#99ff99,stroke:#333


    <!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Bot Detection - Educational Research</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        cyber: {
                            dark: '#0f172a',
                            light: '#f8fafc',
                            accent: '#3b82f6',
                            danger: '#ef4444',
                            success: '#10b981'
                        }
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #1e293b; }
        ::-webkit-scrollbar-thumb { background: #475569; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #64748b; }
        
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container { height: 350px; }
        }
    </style>
    <!-- 
    CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. 
    All visuals are rendered via Canvas (Chart.js) or standard Unicode/HTML.
    -->
    
    <!-- Chosen Palette: "Cyber Defense" - Slate/Blue/Emerald
         Backgrounds: Slate-900 (Dark), Slate-50 (Light)
         Accents: Blue-500 (Info), Emerald-500 (Safe), Red-500 (Threat)
    -->
    
    <!-- Application Structure Plan:
         1. Header: Global controls (Lang/Theme) + Navigation.
         2. Hero: Scenario Context (ShopGuard).
         3. Dashboard Layout:
            - Section 1: Technology Stack (Comparison).
            - Section 2: Fingerprinting Lab (Visual explanation).
            - Section 3: Interactive Simulation (The "WAF" Game).
         4. Content is loaded dynamically based on language selection.
         5. Focus on interactive learning: Sliders to adjust WAF sensitivity, Charts to compare tools.
    -->
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 font-sans">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/90 dark:bg-slate-800/90 backdrop-blur border-b border-slate-200 dark:border-slate-700">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <div class="flex items-center gap-2">
                    <span class="text-2xl">🛡️</span>
                    <span class="font-bold text-xl tracking-tight">BotSec<span class="text-blue-500">Edu</span></span>
                </div>
                <div class="hidden md:block">
                    <div class="ml-10 flex items-baseline space-x-4" id="nav-links">
                        <!-- Nav items injected via JS -->
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <button id="lang-toggle" class="px-3 py-1 rounded bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 transition text-sm font-semibold">TR</button>
                    <button id="theme-toggle" class="p-2 rounded-full hover:bg-slate-200 dark:hover:bg-slate-700 transition">
                        🌙
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12">

        <!-- Hero Section: Scenario -->
        <section id="hero" class="bg-white dark:bg-slate-800 rounded-2xl p-8 shadow-lg border-l-4 border-blue-500">
            <h1 id="hero-title" class="text-3xl md:text-4xl font-bold mb-4"></h1>
            <p id="hero-desc" class="text-lg text-slate-600 dark:text-slate-300 mb-6 leading-relaxed"></p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
                <div class="p-4 bg-slate-100 dark:bg-slate-700/50 rounded-lg">
                    <div class="text-2xl mb-2">🤖</div>
                    <h3 id="card1-title" class="font-bold mb-2"></h3>
                    <p id="card1-desc" class="text-sm opacity-80"></p>
                </div>
                <div class="p-4 bg-slate-100 dark:bg-slate-700/50 rounded-lg">
                    <div class="text-2xl mb-2">🕵️</div>
                    <h3 id="card2-title" class="font-bold mb-2"></h3>
                    <p id="card2-desc" class="text-sm opacity-80"></p>
                </div>
                <div class="p-4 bg-slate-100 dark:bg-slate-700/50 rounded-lg">
                    <div class="text-2xl mb-2">⚖️</div>
                    <h3 id="card3-title" class="font-bold mb-2"></h3>
                    <p id="card3-desc" class="text-sm opacity-80"></p>
                </div>
            </div>
        </section>

        <!-- Section: Technologies (Visual Comparison) -->
        <section id="tech" class="scroll-mt-20">
            <div class="mb-6">
                <h2 id="tech-title" class="text-2xl font-bold mb-2"></h2>
                <p id="tech-intro" class="text-slate-600 dark:text-slate-400"></p>
            </div>
            
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
                <!-- Text Content -->
                <div class="space-y-4">
                    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-lg text-blue-500">Selenium</h3>
                        <p id="sel-desc" class="text-sm mt-2"></p>
                    </div>
                    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-lg text-green-500">Puppeteer</h3>
                        <p id="pup-desc" class="text-sm mt-2"></p>
                    </div>
                    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-lg text-orange-500">Playwright</h3>
                        <p id="play-desc" class="text-sm mt-2"></p>
                    </div>
                </div>

                <!-- Radar Chart -->
                <div class="bg-white dark:bg-slate-800 p-4 rounded-xl shadow h-full flex flex-col justify-center">
                    <h3 id="chart1-title" class="text-center font-semibold mb-4 text-sm uppercase tracking-wide opacity-70"></h3>
                    <div class="chart-container">
                        <canvas id="techRadarChart"></canvas>
                    </div>
                    <div class="mt-4 text-xs text-center text-slate-500" id="chart1-caption"></div>
                </div>
            </div>
        </section>

        <!-- Section: Fingerprinting (Interactive) -->
        <section id="fingerprint" class="scroll-mt-20">
            <div class="mb-6">
                <h2 id="fp-title" class="text-2xl font-bold mb-2"></h2>
                <p id="fp-intro" class="text-slate-600 dark:text-slate-400"></p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Concept Visualization -->
                <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow">
                    <h3 id="fp-canvas-title" class="font-bold mb-4"></h3>
                    <div class="flex items-center justify-center bg-slate-100 dark:bg-slate-900 h-48 rounded-lg mb-4 relative overflow-hidden group cursor-crosshair border border-slate-300 dark:border-slate-700">
                        <!-- Simulated Canvas Noise -->
                        <div id="noise-layer" class="absolute inset-0 opacity-50"></div>
                        <span class="relative z-10 font-mono text-xs bg-black/70 text-white p-2 rounded hidden group-hover:block">
                            Hash: 0x4f9a2b3c<br>GPU: Angle (Intel)
                        </span>
                        <div class="absolute bottom-2 right-2 text-xs text-slate-500">Hover to see hash</div>
                    </div>
                    <p id="fp-canvas-desc" class="text-sm text-slate-600 dark:text-slate-400"></p>
                </div>

                <!-- Data Weight Chart -->
                <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow">
                    <h3 id="chart2-title" class="font-bold mb-4 text-center"></h3>
                    <div class="chart-container">
                        <canvas id="fingerprintDoughnut"></canvas>
                    </div>
                </div>
            </div>
        </section>

        <!-- Section: Defensive Simulation (Game) -->
        <section id="simulation" class="scroll-mt-20 bg-slate-900 text-slate-200 rounded-2xl p-8 shadow-2xl overflow-hidden relative">
            <div class="absolute top-0 right-0 p-4 opacity-10 text-9xl">🛡️</div>
            
            <div class="relative z-10">
                <h2 id="sim-title" class="text-3xl font-bold mb-2 text-white"></h2>
                <p id="sim-intro" class="text-slate-400 mb-8 max-w-3xl"></p>

                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <!-- Controls -->
                    <div class="bg-slate-800/50 p-6 rounded-xl border border-slate-700 backdrop-blur-sm">
                        <h3 id="sim-controls" class="font-bold text-blue-400 mb-4 uppercase tracking-wider text-sm"></h3>
                        
                        <div class="mb-6">
                            <label class="block text-sm font-medium mb-2" id="label-sensitivity"></label>
                            <input type="range" id="sensitivity-slider" min="10" max="90" value="50" class="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500">
                            <div class="flex justify-between text-xs text-slate-500 mt-1">
                                <span id="label-loose"></span>
                                <span id="label-strict"></span>
                            </div>
                        </div>

                        <div class="space-y-4">
                            <div class="flex justify-between items-center p-3 bg-slate-800 rounded">
                                <span id="stat-allowed" class="text-sm"></span>
                                <span id="val-allowed" class="font-mono text-green-400 font-bold">0</span>
                            </div>
                            <div class="flex justify-between items-center p-3 bg-slate-800 rounded">
                                <span id="stat-blocked" class="text-sm"></span>
                                <span id="val-blocked" class="font-mono text-red-400 font-bold">0</span>
                            </div>
                            <div class="flex justify-between items-center p-3 bg-slate-800 rounded border border-yellow-500/30">
                                <span id="stat-fp" class="text-sm text-yellow-200"></span>
                                <span id="val-fp" class="font-mono text-yellow-400 font-bold">0%</span>
                            </div>
                        </div>
                        
                        <button id="btn-reset" class="w-full mt-6 py-2 bg-blue-600 hover:bg-blue-500 rounded text-white font-semibold transition"></button>
                    </div>

                    <!-- Live Scatter Plot -->
                    <div class="lg:col-span-2 bg-slate-800/50 p-4 rounded-xl border border-slate-700 backdrop-blur-sm flex flex-col">
                        <div class="flex justify-between items-center mb-2">
                            <h3 id="sim-viz-title" class="text-sm font-bold text-slate-400"></h3>
                            <div class="flex gap-4 text-xs">
                                <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-blue-400"></span> Human</span>
                                <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-red-400"></span> Bot</span>
                            </div>
                        </div>
                        <div class="chart-container flex-grow">
                            <canvas id="simulationChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white dark:bg-slate-800 border-t border-slate-200 dark:border-slate-700 py-8 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <p class="text-slate-500 text-sm">© 2023 BotSecEdu Research. Educational Purpose Only.</p>
        </div>
    </footer>

    <!-- Logic -->
    <script>
        // --- Data & Translations ---
        const translations = {
            en: {
                nav: ["Overview", "Automation", "Fingerprinting", "Simulation"],
                hero: {
                    title: "Advanced Bot Detection & Evasion",
                    desc: "An educational deep-dive into the defensive mechanisms protecting modern web applications from automated threats. Explore how detection works, why evasion happens, and the security implications.",
                    cards: [
                        {title: "Automation", desc: "How headless browsers like Playwright and Puppeteer simulate human behavior."},
                        {title: "Detection", desc: "Layered defense strategies from IP reputation to behavioral analysis."},
                        {title: "Fingerprinting", desc: "Identifying devices through Canvas, WebGL, and TLS signals without cookies."}
                    ]
                },
                tech: {
                    title: "Browser Automation Landscape",
                    intro: "Understanding the tools used for both testing and abuse is critical for defense.",
                    sel: "The legacy standard. High detectability due to `navigator.webdriver` flags. Primary use: QA.",
                    pup: "Chrome-centric automation. Lightweight but distinct 'Headless' footprint. Primary use: Scraping.",
                    play: "Modern, multi-browser engine support. Designed for speed and stealth. The current challenge for WAFs.",
                    chartTitle: "Tool Comparison Matrix",
                    chartCaption: "Comparison based on default configuration detectability vs utility.",
                    labels: ["Speed", "Stealth (Default)", "Community Support", "Ease of Use", "Engine Support"]
                },
                fp: {
                    title: "Digital Fingerprinting",
                    intro: "How servers identify users without cookies by analyzing hardware and software characteristics.",
                    canvasTitle: "Canvas Fingerprinting Concept",
                    canvasDesc: "The server commands the browser to render a hidden 3D image. Subtle differences in your GPU and drivers produce a unique pixel hash.",
                    chartTitle: "Fingerprint Signal Weights",
                    labels: ["Canvas/WebGL", "User-Agent/Headers", "IP/Network", "AudioContext", "Behavior"]
                },
                sim: {
                    title: "WAF Simulation Lab",
                    intro: "Act as the Security Analyst. Adjust the detection threshold. If you are too strict, you block real customers (False Positives). If too loose, bots slip through.",
                    controls: "Defense Configuration",
                    sensitivity: "Blocking Sensitivity",
                    loose: "Loose (More Bots)",
                    strict: "Strict (Block Humans)",
                    allowed: "Traffic Allowed",
                    blocked: "Traffic Blocked",
                    fp: "False Positive Rate",
                    reset: "Reset Simulation",
                    vizTitle: "Live Traffic Analysis (Y: Suspicion Score)"
                }
            },
            tr: {
                nav: ["Genel Bakış", "Otomasyon", "Parmak İzi", "Simülasyon"],
                hero: {
                    title: "Gelişmiş Bot Tespiti ve Atlatma",
                    desc: "Modern web uygulamalarını otomatik tehditlerden koruyan savunma mekanizmalarına eğitimsel bir bakış. Tespitin nasıl çalıştığını ve güvenlik etkilerini keşfedin.",
                    cards: [
                        {title: "Otomasyon", desc: "Playwright ve Puppeteer gibi tarayıcıların insan davranışını taklidi."},
                        {title: "Tespit Etme", desc: "IP itibarından davranışsal analize kadar katmanlı savunma stratejileri."},
                        {title: "Parmak İzi", desc: "Cihazların çerez olmadan Canvas ve TLS sinyalleriyle tanımlanması."}
                    ]
                },
                tech: {
                    title: "Tarayıcı Otomasyon Dünyası",
                    intro: "Hem test hem de kötüye kullanım için kullanılan araçları anlamak savunma için kritiktir.",
                    sel: "Eski standart. `navigator.webdriver` bayrakları nedeniyle kolay tespit edilir. Asıl kullanım: QA.",
                    pup: "Chrome odaklı otomasyon. Hafif ama belirgin 'Headless' izi. Asıl kullanım: Veri kazıma.",
                    play: "Modern, çoklu motor desteği. Hız ve gizlilik için tasarlandı. WAF'lar için güncel zorluk.",
                    chartTitle: "Araç Karşılaştırma Matrisi",
                    chartCaption: "Varsayılan yapılandırma tespit edilebilirliğine karşı fayda karşılaştırması.",
                    labels: ["Hız", "Gizlilik (Varsayılan)", "Topluluk Desteği", "Kullanım Kolaylığı", "Motor Desteği"]
                },
                fp: {
                    title: "Dijital Parmak İzi",
                    intro: "Sunucuların, çerezler olmadan donanım ve yazılım özelliklerini analiz ederek kullanıcıları tanımlaması.",
                    canvasTitle: "Canvas Parmak İzi Konsepti",
                    canvasDesc: "Sunucu, tarayıcıya gizli bir 3D görüntü oluşturmasını emreder. GPU ve sürücülerdeki küçük farklar benzersiz bir piksel özeti oluşturur.",
                    chartTitle: "Sinyal Ağırlıkları",
                    labels: ["Canvas/WebGL", "User-Agent/Başlıklar", "IP/Ağ", "AudioContext", "Davranış"]
                },
                sim: {
                    title: "WAF Simülasyon Laboratuvarı",
                    intro: "Güvenlik Analisti olarak hareket edin. Tespit eşiğini ayarlayın. Çok katı olursanız gerçek müşterileri engellersiniz. Çok gevşek olursanız botlar sızar.",
                    controls: "Savunma Yapılandırması",
                    sensitivity: "Engelleme Hassasiyeti",
                    loose: "Gevşek",
                    strict: "Katı",
                    allowed: "İzin Verilen",
                    blocked: "Engellenen",
                    fp: "Hatalı Pozitif Oranı",
                    reset: "Simülasyonu Sıfırla",
                    vizTitle: "Canlı Trafik Analizi (Y: Şüphe Skoru)"
                }
            }
        };

        // --- State Management ---
        let currentLang = 'en';
        let charts = {};
        let simInterval = null;
        let simData = { allowed: 0, blocked: 0, fps: 0, totalHumans: 0 };
        const simPoints = []; // {x, y, type} type: 0=human, 1=bot

        // --- DOM Elements ---
        const els = {
            navLinks: document.getElementById('nav-links'),
            langBtn: document.getElementById('lang-toggle'),
            themeBtn: document.getElementById('theme-toggle'),
            slider: document.getElementById('sensitivity-slider'),
            valAllowed: document.getElementById('val-allowed'),
            valBlocked: document.getElementById('val-blocked'),
            valFp: document.getElementById('val-fp'),
            btnReset: document.getElementById('btn-reset')
        };

        // --- Initialization ---
        function init() {
            renderContent();
            initCharts();
            startSimulation();
            generateNoise(); // Visual effect for canvas section
            
            // Event Listeners
            els.langBtn.addEventListener('click', toggleLang);
            els.themeBtn.addEventListener('click', toggleTheme);
            els.slider.addEventListener('input', updateSimStats);
            els.btnReset.addEventListener('click', resetSimulation);

            // Auto-detect theme
            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                document.documentElement.classList.add('dark');
            }
        }

        // --- Visual Effects ---
        function generateNoise() {
            const noise = document.getElementById('noise-layer');
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = 100;
            canvas.height = 100;
            
            const w = canvas.width;
            const h = canvas.height;
            const idata = ctx.createImageData(w, h);
            const buffer32 = new Uint32Array(idata.data.buffer);
            const len = buffer32.length;

            for (let i = 0; i < len; i++) {
                if (Math.random() < 0.5) {
                    buffer32[i] = 0xff000000;
                }
            }
            ctx.putImageData(idata, 0, 0);
            noise.style.backgroundImage = `url(${canvas.toDataURL()})`;
        }

        // --- Logic: Language & Content ---
        function toggleLang() {
            currentLang = currentLang === 'en' ? 'tr' : 'en';
            els.langBtn.textContent = currentLang.toUpperCase();
            renderContent();
            initCharts(); // Re-render charts with new labels
        }

        function toggleTheme() {
            document.documentElement.classList.toggle('dark');
        }

        function renderContent() {
            const t = translations[currentLang];
            
            // Nav
            els.navLinks.innerHTML = `
                <a href="#hero" class="px-3 py-2 rounded-md hover:bg-slate-200 dark:hover:bg-slate-700 transition font-medium">${t.nav[0]}</a>
                <a href="#tech" class="px-3 py-2 rounded-md hover:bg-slate-200 dark:hover:bg-slate-700 transition font-medium">${t.nav[1]}</a>
                <a href="#fingerprint" class="px-3 py-2 rounded-md hover:bg-slate-200 dark:hover:bg-slate-700 transition font-medium">${t.nav[2]}</a>
                <a href="#simulation" class="px-3 py-2 rounded-md hover:bg-slate-200 dark:hover:bg-slate-700 transition font-medium">${t.nav[3]}</a>
            `;

            // Hero
            document.getElementById('hero-title').textContent = t.hero.title;
            document.getElementById('hero-desc').textContent = t.hero.desc;
            document.getElementById('card1-title').textContent = t.hero.cards[0].title;
            document.getElementById('card1-desc').textContent = t.hero.cards[0].desc;
            document.getElementById('card2-title').textContent = t.hero.cards[1].title;
            document.getElementById('card2-desc').textContent = t.hero.cards[1].desc;
            document.getElementById('card3-title').textContent = t.hero.cards[2].title;
            document.getElementById('card3-desc').textContent = t.hero.cards[2].desc;

            // Tech
            document.getElementById('tech-title').textContent = t.tech.title;
            document.getElementById('tech-intro').textContent = t.tech.intro;
            document.getElementById('sel-desc').textContent = t.tech.sel;
            document.getElementById('pup-desc').textContent = t.tech.pup;
            document.getElementById('play-desc').textContent = t.tech.play;
            document.getElementById('chart1-title').textContent = t.tech.chartTitle;
            document.getElementById('chart1-caption').textContent = t.tech.chartCaption;

            // Fingerprint
            document.getElementById('fp-title').textContent = t.fp.title;
            document.getElementById('fp-intro').textContent = t.fp.intro;
            document.getElementById('fp-canvas-title').textContent = t.fp.canvasTitle;
            document.getElementById('fp-canvas-desc').textContent = t.fp.canvasDesc;
            document.getElementById('chart2-title').textContent = t.fp.chartTitle;

            // Simulation
            document.getElementById('sim-title').textContent = t.sim.title;
            document.getElementById('sim-intro').textContent = t.sim.intro;
            document.getElementById('sim-controls').textContent = t.sim.controls;
            document.getElementById('label-sensitivity').textContent = t.sim.sensitivity;
            document.getElementById('label-loose').textContent = t.sim.loose;
            document.getElementById('label-strict').textContent = t.sim.strict;
            document.getElementById('stat-allowed').textContent = t.sim.allowed;
            document.getElementById('stat-blocked').textContent = t.sim.blocked;
            document.getElementById('stat-fp').textContent = t.sim.fp;
            document.getElementById('btn-reset').textContent = t.sim.reset;
            document.getElementById('sim-viz-title').textContent = t.sim.vizTitle;
        }

        // --- Logic: Charts ---
        function initCharts() {
            const t = translations[currentLang];
            const isDark = document.documentElement.classList.contains('dark');
            const gridColor = isDark ? '#334155' : '#e2e8f0';
            const textColor = isDark ? '#cbd5e1' : '#475569';

            Chart.defaults.color = textColor;
            Chart.defaults.borderColor = gridColor;

            // 1. Radar Chart (Tech Comparison)
            if (charts.radar) charts.radar.destroy();
            const ctxRadar = document.getElementById('techRadarChart').getContext('2d');
            charts.radar = new Chart(ctxRadar, {
                type: 'radar',
                data: {
                    labels: t.tech.labels,
                    datasets: [
                        {
                            label: 'Selenium',
                            data: [3, 2, 9, 7, 6],
                            borderColor: '#3b82f6',
                            backgroundColor: 'rgba(59, 130, 246, 0.2)',
                        },
                        {
                            label: 'Puppeteer',
                            data: [8, 5, 8, 8, 4],
                            borderColor: '#10b981',
                            backgroundColor: 'rgba(16, 185, 129, 0.2)',
                        },
                        {
                            label: 'Playwright',
                            data: [9, 7, 7, 6, 9],
                            borderColor: '#f97316',
                            backgroundColor: 'rgba(249, 115, 22, 0.2)',
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: { r: { min: 0, max: 10, ticks: { display: false } } }
                }
            });

            // 2. Doughnut Chart (Fingerprint Weights)
            if (charts.doughnut) charts.doughnut.destroy();
            const ctxDoughnut = document.getElementById('fingerprintDoughnut').getContext('2d');
            charts.doughnut = new Chart(ctxDoughnut, {
                type: 'doughnut',
                data: {
                    labels: t.fp.labels,
                    datasets: [{
                        data: [15, 20, 30, 10, 25],
                        backgroundColor: [
                            '#8b5cf6', // Canvas (Purple)
                            '#3b82f6', // UA (Blue)
                            '#ef4444', // IP (Red)
                            '#f59e0b', // Audio (Yellow)
                            '#10b981'  // Behavior (Green)
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // 3. Scatter Plot (Simulation) - Init only
            if (!charts.scatter) {
                const ctxScatter = document.getElementById('simulationChart').getContext('2d');
                charts.scatter = new Chart(ctxScatter, {
                    type: 'scatter',
                    data: {
                        datasets: [
                            {
                                label: 'Human',
                                data: [],
                                backgroundColor: '#3b82f6',
                                pointRadius: 4
                            },
                            {
                                label: 'Bot',
                                data: [],
                                backgroundColor: '#ef4444',
                                pointRadius: 5,
                                pointStyle: 'rectRot'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        animation: false,
                        scales: {
                            x: { display: false, min: 0, max: 100 },
                            y: { min: 0, max: 100, title: { display: true, text: 'Suspicion Score' } }
                        },
                        plugins: { legend: { display: false } }
                    }
                });
            }
        }

        // --- Logic: Simulation ---
        function resetSimulation() {
            simData = { allowed: 0, blocked: 0, fps: 0, totalHumans: 0 };
            simPoints.length = 0;
            charts.scatter.data.datasets[0].data = [];
            charts.scatter.data.datasets[1].data = [];
            charts.scatter.update();
            updateSimStats();
        }

        function startSimulation() {
            if (simInterval) clearInterval(simInterval);
            simInterval = setInterval(() => {
                // Generate traffic
                // X = time (always moving), Y = Suspicion Score (0-100)
                
                // 70% chance Human, 30% chance Bot
                const isBot = Math.random() < 0.3;
                let score;
                
                if (isBot) {
                    // Bots tend to have higher suspicion scores (50-95), but some are stealthy (20-50)
                    score = 40 + Math.random() * 55;
                } else {
                    // Humans tend to have lower scores (0-40), but some look weird (VPNs, strange browsers) (40-70)
                    score = Math.random() * 45;
                    // Occasional "weird" human
                    if (Math.random() < 0.1) score += 20; 
                }

                const point = { x: Date.now(), y: score, isBot: isBot };
                simPoints.push(point);

                // Keep only last 50 points for performance
                if (simPoints.length > 50) simPoints.shift();

                updateSimViz();
                updateSimStats();

            }, 800); // New request every 800ms
        }

        function updateSimViz() {
            // Map points to chart format (x is just index 0-50)
            const humanData = simPoints.filter(p => !p.isBot).map((p, i) => ({ x: i * 2, y: p.y }));
            const botData = simPoints.filter(p => p.isBot).map((p, i) => ({ x: i * 2, y: p.y }));

            charts.scatter.data.datasets[0].data = humanData;
            charts.scatter.data.datasets[1].data = botData;
            charts.scatter.update();
        }

        function updateSimStats() {
            const threshold = parseInt(els.slider.value);
            
            // Recalculate stats based on CURRENT threshold for visual feedback
            // In a real app, decisions are final. Here we show "what if".
            
            let allowed = 0;
            let blocked = 0;
            let falsePositives = 0;
            let humanCount = 0;

            simPoints.forEach(p => {
                const blockedRequest = p.y >= threshold;
                if (blockedRequest) {
                    blocked++;
                    if (!p.isBot) falsePositives++; // Blocked a human
                } else {
                    allowed++;
                }
                if (!p.isBot) humanCount++;
            });

            els.valAllowed.textContent = allowed;
            els.valBlocked.textContent = blocked;
            
            const fpRate = humanCount > 0 ? ((falsePositives / humanCount) * 100).toFixed(1) : 0;
            els.valFp.textContent = fpRate + "%";
            els.valFp.className = `font-mono font-bold ${fpRate > 5 ? 'text-red-400' : 'text-yellow-400'}`;
            
            // Visual threshold line (simple hack: draw a line on chart plugin or just mental model)
            // For simplicity in this constraints, we rely on the user seeing dots above/below their mental line.
        }

        // --- Run ---
        init();

    </script>
</body>
</html>
