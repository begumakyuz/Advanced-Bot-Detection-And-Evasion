# Prompts for deepseek
Based on your request, here is the English version of the comprehensive, Deep Research-style technical guide for your project, structured according to the specific principles and output format you provided.
OBJECTIVE

Develop an advanced SecOps and Reverse Engineering-focused framework for analyzing modern bot detection (Browser Fingerprinting) and implementing robust evasion techniques using Playwright.
BACKGROUND

    Target: Analysis of digital footprints left by automation tools (Playwright, Puppeteer, Selenium).

    User Profile: Undergraduate student in Information Security Technology at Istinye University.

    Project Context: Final Project for "Open Source Operating Systems," requiring specific automation and metadata standards.

    Environment: Python 3.13, Playwright (Chromium), Windows/Linux.

REQUIREMENTS

    Bot Detection Analysis: Scripting for identifying leaks in headless browsers, including navigator.webdriver flags, User-Agent anomalies, and missing feature sets.

    Evasion Implementation: Manual manipulation of browser fingerprint data such as hardwareConcurrency, languages, and plugins to mimic legitimate user behavior.

    Header Analysis: Identifying and rectifying anomalies in HTTP headers (Sec-Ch-Ua, Accept-Language, etc.).

    Automation & Compliance: Implementing "Auto Control" and "Auto Test" abilities as per project specifications, including a standardized project_info.json.

OUTPUT FORMAT
Section 1: Theoretical Analysis of Browser Fingerprinting

A deep dive into how modern anti-bot systems (e.g., Cloudflare, Akamai) utilize client-side JavaScript to differentiate between human-driven and automated browsers.
Section 2: Detection & Diagnostic Scripts

Complete Python implementations using Playwright to extract and log "leaky" attributes that reveal a browser's headless nature.
Section 3: Advanced Evasion Framework

A library-independent implementation using page.add_init_script to mask the navigator.webdriver property and inject realistic hardware/software metadata into the browser context.
Section 4: Self-Diagnostic System (check_system.py)

Implementation of the "Auto Test Ability". This script must verify library dependencies, browser driver status, and target site reachability before execution.
Section 5: Standardized Project Metadata

A comprehensive README.md and a compliant project_info.json structure as required by the "Açık Kaynak İşletim Sistemi Projesi" guidelines.
DEPTH EXPECTATION

Request a comprehensive, high-resolution analysis. Do not abbreviate code blocks or summarize technical concepts unless specifically requested. Provide complete implementation details for SecOps professionals, including full JavaScript injection payloads and Python automation logic.
