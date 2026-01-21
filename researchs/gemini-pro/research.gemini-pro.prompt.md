You are Gemini Pro with Deep Research capabilities.

Your task is to perform a comprehensive, academically rigorous,
real-world grounded security research and present ALL results
as a complete, production-ready technical website.

CRITICAL INSTRUCTIONS:
- Use explicit internal step-by-step reasoning.
- Decompose complex systems into logical, operational, and detection layers.
- Base all claims on up-to-date, reputable sources.
- Clearly cite references (academic papers, vendor docs, trusted security blogs).
- Do NOT omit any mandatory output.
- Do NOT provide weaponized, copy-paste exploit or bypass instructions.

---

PROJECT TITLE:
Advanced Bot Detection & Evasion

DOMAIN:
SecOps | Blue Team | Authorized Red Team (Lab) | DFIR | Browser Automation Security

---

CONTEXT:
This research focuses on Advanced Bot Detection & Evasion primarily from a
Blue Team and SecOps perspective, complemented by:
- Authorized Red Team simulation in a controlled lab
- Post-incident forensic reconstruction
- MITRE-style adversary emulation for defensive mapping

The project analyzes how modern websites detect automation traffic from
Playwright, Puppeteer, and Selenium, and how defenses respond.

---

PURPOSE:
To deliver an end-to-end technical, operational, and governance-aware analysis
of bot detection systems, their limitations, defensive hardening strategies,
and their integration into SOC / SecOps workflows—culminating in a full
web-based technical presentation.

---

REAL-WORLD SCENARIO (MANDATORY):

Assume a realistic scenario:

A high-traffic e-commerce & SaaS platform suffers automated abuse:
- Account takeover (ATO)
- Credential stuffing
- Inventory & price scraping
- Promotion & API abuse

Controls in place:
- Commercial Bot Management (e.g., Cloudflare, Akamai, HUMAN)
- WAF
- SIEM + SOAR

Despite controls, sophisticated automation partially bypasses detection.

ALL analysis MUST be grounded in this scenario.

---

ANALYSIS MODES (ALL MANDATORY):

1) BLUE TEAM (PRIMARY):
- Production detection signals (fingerprints, headers, TLS, behavior)
- Signal strength vs false positives
- Hardening strategies
- Monitoring, logging, alerting, response

2) AUTHORIZED RED TEAM (LAB-ONLY):
- Simulated adversary behavior in an isolated, authorized test environment
- High-level evasion concepts (non-operational)
- Risks and indicators introduced by evasion
- NO step-by-step, NO payloads, NO bypass scripts

3) POST-INCIDENT FORENSIC (DFIR):
- Reconstruction of a completed attack
- Log, alert, and timeline analysis
- Root cause identification
- Lessons learned and preventive controls

4) MITRE ADVERSARY EMULATION (DEFENSIVE):
- Map observed behaviors to TTPs
- Focus on detection opportunities and gaps
- Translate TTPs into defensive controls

5) LEGAL & ETHICAL ANALYSIS:
- GDPR / KVKK and privacy implications
- Fingerprinting consent & data minimization
- Ethical research boundaries
- Responsible disclosure
- Misuse risk assessment

---

TECHNICAL SCOPE:

BOT DETECTION:
- Headless indicators:
  - User-Agent inconsistencies
  - navigator.webdriver
  - Missing/abnormal browser APIs
- Behavioral & heuristic analysis
- Client- vs server-side detection
- Conceptual review of real-world scripts

EVASION (DEFENSIVE AWARENESS):
- Conceptual fingerprint signals:
  - hardwareConcurrency, languages, plugins
  - Canvas, WebGL, AudioContext
- Consistency challenges and side-effects

HTTP & TLS:
- Header anomaly detection
- Automation patterns
- TLS fingerprint consistency

---

DEFENSIVE METRICS & KPIs (MANDATORY):

Define and analyze:
- Bot Detection Rate
- False Positive Rate
- Observed Evasion Success
- MTTD / MTTR
- Signal Confidence Scores
- Reduction in bot-driven incidents

Explain usage for:
- SOC analysts
- SecOps engineers
- Security leadership

---

SOC / SECOPS INTEGRATION (MANDATORY):

Describe end-to-end workflows:
- Log generation & normalization
- SIEM correlation
- Alerting & prioritization
- SOAR automation
- WAF / rate-limit enforcement

---

SOC ALERT SCENARIOS (MANDATORY):

Provide realistic scenarios:
- High-confidence automation fingerprint
- Credential stuffing pattern
- Reused fingerprint across IPs
- TLS anomaly
- Behavioral deviation

For each:
- Trigger
- Severity
- Analyst action
- Automated vs manual response

---

TOOLS & CONCEPTS:

LIBRARIES:
- Playwright
- Puppeteer
- Selenium (comparative)

CONCEPTS:
- Browser Fingerprinting
- Headless Detection
- Bot Mitigation
- DFIR
- SOC / SecOps
- MITRE-style emulation (defensive)

---

MANDATORY OUTPUTS (ALL REQUIRED):

1) MARKDOWN TECHNICAL RESEARCH REPORT
- Academic, professional tone
- Includes all sections above
- Citations & references

2) VISUAL INFOGRAPHIC
- Mermaid or structured ASCII
- Detection layers, adversary concepts, SOC flow

3) MODERN HTML TECHNICAL WEBSITE (CODE ONLY)

HTML WEBSITE CONSOLIDATION (CRITICAL):
The HTML site MUST be a complete web-based representation of ALL outputs.
It MUST include sections/pages for:
- Full research content (from Markdown)
- Infographics
- Defensive metrics & KPI explanations
- KPI dashboard (HTML-based)
- SOC / SecOps workflows
- SOC alert scenarios
- Legal & ethical analysis

HTML FEATURES (MANDATORY):
- Semantic HTML
- Multilanguage: Turkish (TR) & English (EN)
- Language switcher
- Theme modes: Light / Dark / System
- Accessible, readable, portfolio-ready
- No unnecessary external dependencies

---

OUTPUT ORDER (STRICT):
1) Markdown Report
2) Infographic
3) HTML Website Source Code

---

QUALITY BAR:
- Security-first, defensive mindset
- No vague claims
- Real-world applicability
- Neutral, academic tone
- Suitable for university review, portfolio, and professional use

Begin the research now.

türkçe ve ingilizce destekli multilanguage rapor ve site istiyorum.
