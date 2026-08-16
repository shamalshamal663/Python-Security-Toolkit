# 🛡️ Python Security Automation Toolkit

A modular collection of command-line security tools, log analysis parsers, and authentication utilities built in Python. Designed for automated reconnaissance, defense evaluation, and payload generation.

---

## 📂 Repository Architecture

```text
python-security-toolkit/
│
├── README.md                     # Documentation and usage guides
│
├── recon_and_discovery/
│   ├── target_checker.py         # CLI Target & Host Validator (sys, os, time)
│   └── port_scanner.py           # Port Risk Analyzer & Evaluator (def, in/not in)
│
├── log_and_threat_analysis/
│   ├── log_auditor.py            # Fault-Tolerant Log Auditor (try/except, FileNotFoundError)
│   ├── file_parser.py            # Disk Threat Extractor (open "r", .strip())
│   └── audit_logger.py           # Persistent Security Event Appender (open "a")
│
└── payload_and_auth/
    ├── token_generator.py        # Automated Session Token Generator (random, time)
    ├── wordlist_builder.py       # Custom Targeted Wordlist Compiler (sys, random, open "w")
    └── auth_auditor.py           # An IAM privilege  and security posture auditor that verify user role ,enforces 
                                  # Multi Factor Authentication (MFA),and look out for account exceeding failed login threshold 
```

---

## 🛠️ Modules & Tool Overview

### 📡 1. Recon & Discovery (`/recon_and_discovery`)

* **`target_checker.py`**
  * **Description:** Command-line target verification tool. Validates CLI argument length, verifies file existence on disk, simulates network probing latency, and processes target hosts.
  * **Usage:**
    ```bash
    python3 recon_and_discovery/target_checker.py hosts.txt
    ```

* **`port_scanner.py`**
  * **Description:** Evaluates scanned network ports against known dangerous services (FTP: 21, SSH: 22, RDP: 3389) and classifies threat levels dynamically.

---

### 🔍 2. Log & Threat Analysis (`/log_and_threat_analysis`)

* **`log_auditor.py`**
  * **Description:** Fault-tolerant log parsing engine equipped with exception handling to safely process target logs without crashing on missing files.

* **`file_parser.py`**
  * **Description:** Reads raw system log files (`server.log`), filters lines matching threat indicators (`CRITICAL`, `WARNING`), and normalizes whitespace.

* **`audit_logger.py`**
  * **Description:** Appends timestamped security events to persistent disk logs without overwriting historical audit data.

---

### 🔑 3. Payload & Authentication (`/payload_and_auth`)

* **`token_generator.py`**
  * **Description:** Generates formatted, randomized authentication tokens pairing security clearance tiers, usernames, unique 4-digit session IDs, and server nodes.

* **`wordlist_builder.py`**
  * **Description:** Targeted dictionary generator. Combines seed keywords with randomized numerical padding and security suffixes, exporting custom wordlists directly to disk via CLI arguments.
  * **Usage:**
    ```bash
    python3 payload_and_auth/wordlist_builder.py custom_passwords.txt
    ```

* **`brute_defender.py`**
  * **Description:** Authentication threshold monitor that simulates wordlist evaluations, tracks failed login attempts, and triggers an automated firewall lockout.

* **'auth_auditor.py'**
  * **Description:** IAM privilege and security posture auditor that verify user role ,enforces Multi Factor Authentication(MFA) compilance ,and lock out account exceeding failed login threshold.
---

## 💻 Setup & Requirements

1. **Prerequisites:** Python 3.8+ installed on Linux, macOS, or Windows.
2. **Clone the Repository:**
   ```bash
   git clone [https://github.com/shamalshamal663/Python-Security-Toolkit.git](https://github.com/shamalshamal663/Python-Security-Toolkit.git)
   cd Python-Security-Toolkit
   ```