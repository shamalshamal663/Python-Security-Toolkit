
 Repository Architecture


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
    └── brute_defender.py         # Rate-Limited Credential & Lockout Defender