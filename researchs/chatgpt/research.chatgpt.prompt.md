# Prompts for chatgpt
# GOAL
I need to produce a comprehensive, academic, and portfolio-ready technical research report titled "Advanced Bot Detection & Evasion: A Defensive and Analytical Study." The objective is to analyze how modern websites detect automation (Playwright, Puppeteer, Selenium) and to investigate the technical mechanisms behind evasion techniques from a Security Research perspective.

# CONTEXT
- **Role:** Security Researcher / Automation Specialist.
- **Project Purpose:** To analyze the traces left by headless browsers and research how to manipulate browser fingerprinting data to appear as a legitimate human user.
- **Technical Focus:** SecOps, Reverse Engineering, and Browser Automation.
- **Target Libraries:** Puppeteer, Playwright.
- **Key Concept:** High-fidelity Browser Fingerprinting in the 2025-2026 landscape.

# SCOPE
- **Include:** 1. Detection of headless mode indicators (User-Agent, Webdriver property, missing features, runtime variables like `window.cdc_`).
    2. Fingerprint Manipulation (navigator.hardwareConcurrency, navigator.languages, navigator.plugins, Canvas, WebGL).
    3. Advanced Header Analysis (HTTP/2-3 anomalies, JA4+ TLS Fingerprinting).
    4. Comparative analysis of Playwright vs. Puppeteer stealth capabilities.
- **Exclude:** Operational exploit scripts for illegal bypass, copy-paste malicious payloads, and corporate SOC playbooks.
- **Sources:** Academic papers (IEEE/ACM), industry reports (Cloudflare, Akamai, Datadome), and open-source documentation.

# DELIVERABLE
- **Format:** Comprehensive Markdown Research Report.
- **Tone:** Instructional, academic, and student-friendly (University-review ready).
- **Structure:**
    1. **Executive Summary:** Overview of the bot-vs-human arms race.
    2. **Detection Pillars:** Working principles of headless detection with code-level indicators.
    3. **Evasion Mechanics:** How fingerprint manipulation works at the browser engine level.
    4. **Network Intelligence:** TLS and HTTP/2-3 fingerprinting (JA4/JA4+).
    5. **Comparative Review:** Open-source vs. Commercial solutions.
    6. **Security & Ethics:** Responsible research and compliance (GDPR/KVKK).

# SUCCESS CRITERIA
- Every technical concept must answer: (1) Fundamental principle, (2) Industry standards, (3) Alternatives, (4) Critical parameters/configs, and (5) Common security pitfalls.
- Use clear, professional terminology (e.g., CDP, TLS Fingerprinting, Behavioral Biometrics).
- The report must be exhaustive, leaving "Zero unanswered questions" for a cybersecurity student.
