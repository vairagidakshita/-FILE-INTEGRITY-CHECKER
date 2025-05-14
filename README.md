# -FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DAKSHITA VAIRAGI

*INTER ID*: CT08DL1157

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

# 🛡️ Description

**File Integrity Monitor** is a simple yet powerful Python-based tool designed to help developers, system administrators, and security-conscious users **track changes in important files** using cryptographic hash comparisons. The tool ensures that any unauthorized, accidental, or malicious changes to files are detected promptly and clearly.

Whether you're maintaining a set of critical configuration files, managing scripts in a production environment, or just want to keep an eye on sensitive documents, this tool offers a lightweight and effective solution for **file integrity verification**.

---

## 📌 What Is File Integrity Monitoring?

File Integrity Monitoring (FIM) is the process of validating the integrity of files by comparing their current state to a known good baseline. This is typically done using cryptographic hash functions, such as SHA-256, which produce a unique digital fingerprint of a file's contents. If the file changes, even slightly, the resulting hash will differ — allowing you to detect the change immediately.

This script uses Python’s built-in `hashlib` library to calculate hashes and stores them in a simple JSON file (`file_hashes.json`). Each time the script runs, it compares the current file hashes against the saved ones to detect:

- **NEW** files that weren’t previously tracked
- **MODIFIED** files that have changed
- **DELETED** files that are no longer present

---

## 🚀 Features

- ✅ **No dependencies** – only standard Python libraries (`hashlib`, `os`, `json`, `argparse`)
- 🔐 Uses secure cryptographic hash algorithms (default: `SHA-256`)
- 🧠 Maintains a persistent JSON database of file hashes
- ⚠️ Detects new, modified, and deleted files
- 📂 Supports monitoring of one or many files at once
- 🧪 Useful for security audits, system configuration tracking, or backup verification
- 💡 Fully scriptable and suitable for automation via cron jobs or task schedulers

---

## 🔧 Installation

To use the File Integrity Monitor, you only need Python 3.7 or above installed.

```bash
git clone https://github.com/your-username/file-integrity-monitor.git
cd file-integrity-monitor
