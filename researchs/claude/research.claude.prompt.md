# Prompts for claude
# ROLE: Senior Infrastructure & Security Research Engineer
# TASK: Create an Enterprise-Grade System Management and Web Automation Security Framework
# CONTEXT: 
You are managing an infrastructure of 50+ Linux servers (Ubuntu 22.04 / RHEL 9) running microservices and containerized workloads (Docker/K8s). Your mission is twofold: 
1. Establish rock-solid server performance and resource management.
2. Conduct deep-dive research into Advanced Bot Detection & Evasion for the automation services running on this fleet.
Please produce a comprehensive technical documentation in the following structure:
---
## 1. ARCHITECTURE & INFRASTRUCTURE MONITORING
- Design a monitoring strategy for a 50-server fleet using open-source tools.
- Focus on automated resource alerting and centralized logging.
## 2. ADVANCED PROCESS MANAGEMENT (Task 1)
- **Mechanics:** Detailed management of processes using `htop` metrics, handling zombie processes, and setting `ulimits`.
- **Automation:** Provide a Bash or Python script that identifies high-resource processes and automatically manages them based on defined thresholds.
## 3. ADVANCED DISK & STORAGE MANAGEMENT (Task 2)
- **Monitoring:** LVM-based partition management and health checks.
- **Automation:** An automated disk cleanup script that handles Docker logs, temporary files, and stale microservice artifacts without disrupting services.
## 4. SECURITY RESEARCH: BOT DETECTION & EVASION (Task 3)
*Analyze the interaction between our automation tools (Playwright, Puppeteer, Selenium) and modern anti-bot systems.*
- **Detection Analysis:** Explain how headless browsers are detected via `User-Agent` strings, `navigator.webdriver` properties, and missing browser features.
- **Evasion Implementation:** - Provide conceptual code/logic to manipulate fingerprinting data (navigator.hardwareConcurrency, languages, plugins).
    - Explain "Header Anomaly Detection" and how to normalize HTTP headers to mimic organic traffic.
- **Technical Comparison:** Compare Playwright and Puppeteer in terms of stealth capabilities and memory footprint on our Linux fleet.
## 5. AUTOMATION & INTEGRATION (Final Output)
- Provide a "Production-Ready" automation suite that integrates the disk/process management tools.
- Include an "Educational Review" section for a student portfolio, explaining the "First Principles" of why these detection and system management techniques work.
---
# CONSTRAINTS & REQUIREMENTS
- **Environment:** Ubuntu 22.04, RHEL 9, Docker, K8s.
- **Exclusions:** NO proprietary tools (e.g., Datadog, New Relic). Use only open-source Linux native tools.
- **Style:** Academically grounded but student-friendly. Use professional terminology (CDP, LVM, Zombie PID, Fingerprinting).
- **Tone:** Defensive and analytical. 
# OUTPUT FORMAT
Deliver a structured Markdown document with clear code blocks, technical explanations, and a "Success Criteria" checklist at the end.
