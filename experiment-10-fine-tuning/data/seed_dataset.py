"""
Synthetic Fine-Tuning Domain Dataset Generator
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
Generates instruction-tuning datasets for cybersecurity domain adaptation benchmarking.
"""

import json
import os

TRAIN_SAMPLES = [
    {
        "instruction": "Explain how to mitigate CVE-2023-23397 Outlook vulnerability in an enterprise environment.",
        "input": "System environment: Windows Server 2019, Microsoft 365 Hybrid.",
        "output": "To mitigate CVE-2023-23397: 1. Apply Microsoft KB5023151 security update across all Exchange servers. 2. Block outbound port TCP 445 at edge firewalls to prevent NTLM hash leakage. 3. Audit Active Directory for unusual NTLM authentication attempts using PowerShell script CVE-2023-23397.ps1."
    },
    {
        "instruction": "Formulate a policy log masking rule for customer social security numbers (SSN).",
        "input": "Format: 9-digit US SSN (XXX-XX-XXXX).",
        "output": "Enforce Log Masking Rule RULE-PII-02B: Apply regex string replacement r'\\b\\d{3}-\\d{2}-\\d{4}\\b' -> '[SSN-REDACTED]' prior to stdout streaming."
    },
    {
        "instruction": "What is the recommended NIST Post-Quantum Cryptography key exchange algorithm?",
        "input": "Target SLA: TLS 1.3 hybrid key encapsulation.",
        "output": "The NIST standardized post-quantum key encapsulation algorithm is CRYSTALS-Kyber (FIPS 203), recommended in hybrid mode paired with ECDH P-256 for backward compatibility."
    }
]

VAL_SAMPLES = [
    {
        "instruction": "How do you detect unauthorized lateral movement via SMB in SOC logs?",
        "input": "Log source: Windows Event ID 5140 (Network Share Access).",
        "output": "Filter Event ID 5140 for access to administrative shares (C$, ADMIN$) originating from non-administrative IP subnets within short time windows."
    }
]

def generate_datasets(train_path: str = None, val_path: str = None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if train_path is None:
        train_path = os.path.join(base_dir, "train_dataset.jsonl")
    if val_path is None:
        val_path = os.path.join(base_dir, "val_dataset.jsonl")

    os.makedirs(os.path.dirname(train_path), exist_ok=True)
    with open(train_path, "w", encoding="utf-8") as f:
        for item in TRAIN_SAMPLES:
            f.write(json.dumps(item) + "\n")

    with open(val_path, "w", encoding="utf-8") as f:
        for item in VAL_SAMPLES:
            f.write(json.dumps(item) + "\n")

    print(f"[OK] Generated {len(TRAIN_SAMPLES)} train & {len(VAL_SAMPLES)} val instruction samples.")

if __name__ == "__main__":
    generate_datasets()
