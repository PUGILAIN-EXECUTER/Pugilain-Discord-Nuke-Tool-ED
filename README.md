# 🛡️ Pugilain Discord Nuke ULTIMATE Test

<p align="center">
  <img src="https://plain-weur-prod-public.komododecks.com/202608/24/7NTJnFCEJI4pHD7q3xRl/image.jpg" width="600" alt="Pugilain Discord Security Test">
</p>

<p align="center">
  <strong>Discord Server Security & Stress Testing</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Discord-Security_Testing-5865F2?style=for-the-badge&logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Version-6.0.0-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

---

## ⚠️ DISCLAIMER

> **AUTHORIZED USE ONLY**

Pugilain Discord Security Test is intended exclusively for **authorized security testing, research, education, and administration** of Discord servers.

Use this software only on:

* servers you own;
* servers you administer;
* dedicated laboratory environments;
* servers for which you have explicit permission from the owner.

Do not use this project against third-party servers without authorization.

The user is responsible for how the software is used and must comply with the [Discord Terms of Service](https://discord.com/terms), applicable laws, and the rules of the server being tested.

---

# 📋 Description

**Pugilain Discord Security Test** is a Python-based security testing suite designed to help Discord server owners and administrators evaluate their server's security configuration.

The project is designed to simulate controlled abuse scenarios and help administrators identify weaknesses before they can be exploited by malicious users.

Testing areas may include:

* 🛡️ Anti-raid systems;
* 🚫 Anti-spam systems;
* 🔐 Permission configuration;
* 👥 Role management;
* 📢 Channel configuration;
* 🔗 Webhooks;
* 🤖 Bots and integrations;
* 📊 Logging;
* ⚡ Controlled load behavior;
* 🔄 Recovery procedures.

---

# 🎯 Objective

The main objective of the project is to help administrators answer questions such as:

> **"Is my Discord server actually protected against abnormal activity?"**

Controlled testing can reveal configuration weaknesses and help improve the server's defenses.

---

# 🔥 Features

### 🛡️ Anti-Raid Testing

Controlled simulation of raid-like activity to evaluate:

* anti-raid systems;
* user verification;
* AutoMod;
* moderation bots;
* logging;
* administrator response.

### ⚡ Stress Testing

Controlled load testing to evaluate server-side behavior and moderation systems.

Tests should use:

* rate limiting;
* configurable operation counts;
* timeouts;
* maximum limits;
* automatic cleanup;
* emergency stop functionality.

### 🔍 Security Audit

Review server configuration, including:

* roles;
* permissions;
* channels;
* webhooks;
* bots;
* elevated privileges.

### 📊 Reporting

After a test, the application can collect information such as:

```text
Tests executed
Operations completed
Errors
Rate limits
Detected events
Execution time
Overall result
```

### 🖥️ CLI

The project is designed to be operated from a Linux command-line interface.

---

# 👥 Target Users

The project is intended for:

* 👑 Discord server owners;
* 🛡️ administrators;
* 🔧 bot developers;
* 🔐 cybersecurity professionals;
* 📚 students;
* 🧪 authorized penetration testers;
* 🏫 educational laboratories.

---

# ⚙️ Requirements

### Operating System

The project is primarily intended for:

* Kali Linux;
* Debian;
* Ubuntu;
* other compatible Linux distributions.

### Software

You will need:

* Python **3.8+**;
* an Internet connection;
* a Discord bot;
* the dependencies required by the project.

---

# 📁 Project Structure

The current project structure is:

```text
Pugilain-Discord-Nuke-Tool-ED/
│
├── NukeBotLinux/
│   └── Nuke.py
│
├── README.md
└── LICENSE
```

Additional files can be introduced in future versions when they are actually required.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/PUGILAIN-EXECUTER/Pugilain-Discord-Nuke-Tool-ED.git
```

Enter the project directory:

```bash
cd Pugilain-Discord-Nuke-Tool-ED
```

Enter the Linux directory:

```bash
cd NukeBotLinux
```

---

# 🐍 Python Environment

A virtual environment is recommended:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install discord.py aiohttp
```

---

# ▶️ Running

From the `NukeBotLinux` directory:

```bash
python3 Nuke.py
```

The program should then start its command-line interface.

> The main script is **`Nuke.py`**.

---

# 🔑 Discord Bot Configuration

A properly configured Discord bot is required to perform the tests.

The bot should receive only the permissions required for the specific test.

### ⚠️ Bot Token

Never publish your bot token in the repository.

Do not place it in:

* the README;
* public source code;
* screenshots;
* Git commits;
* public messages.

Using an environment variable is recommended:

```bash
export DISCORD_TOKEN="YOUR_BOT_TOKEN"
```

If a token is accidentally exposed, **regenerate it immediately**.

---

# 🧪 Testing Modes

## 🔎 Audit Mode

A non-invasive mode designed to analyze server configuration.

Examples:

```text
Role Audit
Permission Audit
Channel Audit
Webhook Audit
Bot Audit
Security Audit
```

---

## 🧪 Dry Run

Dry Run allows an operation to be simulated without actually applying the change.

Example:

```text
[DRY-RUN] Channel test
[DRY-RUN] Permission check
[DRY-RUN] Security event
```

Using Dry Run before more intensive testing is strongly recommended.

---

## ⚡ Controlled Stress Test

Stress tests should have configurable limits.

Recommended parameters:

```text
Maximum operations
Test duration
Delay
Concurrency
Rate limit handling
Automatic cleanup
Emergency stop
```

Do not use mechanisms designed to bypass Discord's rate limits.

---

# 🛡️ Recommended Tests

| Test             | Purpose                                 |
| ---------------- | --------------------------------------- |
| Anti-Raid Test   | Evaluate raid detection                 |
| Anti-Spam Test   | Evaluate spam protection                |
| Permission Audit | Review permissions                      |
| Role Audit       | Review roles and privileges             |
| Channel Audit    | Review channel configuration            |
| Webhook Audit    | Review webhooks                         |
| Bot Audit        | Review bots and integrations            |
| Stress Test      | Evaluate behavior under controlled load |
| Logging Test     | Verify security logging                 |
| Recovery Test    | Verify recovery procedures              |

---

# 🧹 Cleanup

Any test that creates temporary resources should provide a cleanup mechanism.

Recommended workflow:

```text
START
  │
  ▼
Create test resources
  │
  ▼
Run security test
  │
  ▼
Collect results
  │
  ▼
Generate report
  │
  ▼
Cleanup
  │
  ▼
END
```

Test resources should be easy to identify, for example:

```text
security-test-001
security-test-002
security-test-003
```

---

# 🛑 Emergency Stop

The program should allow the operator to stop a test immediately.

Example:

```text
CTRL+C
```

When interrupted, the program should:

1. stop starting new operations;
2. cancel running tasks;
3. perform cleanup;
4. save available results;
5. terminate cleanly.

---

# 📊 Example Report

```text
========================================
      PUGILAIN SECURITY TEST
========================================

Server: Security Lab

Test: Anti-Raid Simulation
Duration: 00:02:14

Operations
----------------------------------------
Test Events:       50
Successful:        48
Rate Limited:       2
Errors:             0

Security Detection
----------------------------------------
Anti-Raid:         PASS
Anti-Spam:         PASS
Logging:           PASS

Cleanup
----------------------------------------
Status:             PASS

Overall Result
----------------------------------------
SECURITY POSTURE:   GOOD

========================================
```

---

# 🔐 Best Practices

## Least Privilege

Give the bot only the permissions required for the test.

## Safe by Default

The application should start with conservative settings.

## Dry Run

Use Dry Run before performing actual testing.

## Rate Limiting

Always respect platform rate limits.

## Automatic Cleanup

Automatically remove temporary test resources.

## Logging

Record the operations performed during testing.

## Emergency Stop

Provide an immediate way to stop the test.

## Authorization

Require explicit authorization before running potentially invasive tests.

---

# 🚨 Destructive Operations

Features such as:

```text
Ban All
Delete All Channels
Delete All Roles
Mass Channel Creation
Mass Role Creation
Mass Spam
Full Server Wipe
```

must not be used against third-party servers.

For a security-testing project, safer simulated equivalents are recommended:

```text
Ban Simulation
Channel Deletion Simulation
Role Modification Simulation
Spam Detection Simulation
Recovery Simulation
```

If destructive testing is genuinely required for authorized research, it should be restricted to a **dedicated Discord laboratory server** with appropriate safeguards, limits, and recovery procedures.

---

# 🐛 Troubleshooting

### Python not found

Check your Python version:

```bash
python3 --version
```

Python 3.8 or newer is recommended.

### Discord module missing

Install:

```bash
pip install discord.py
```

### aiohttp missing

Install:

```bash
pip install aiohttp
```

### Bot cannot see the server

Check:

* that the bot was invited correctly;
* that it has the required permissions;
* that the required intents are configured;
* that the server is authorized for testing.

### Rate limits

If the application encounters rate limits, reduce:

```text
Concurrency
Operation count
Request rate
Test duration
```

Do not attempt to bypass rate limits.

---

# 📚 Educational Purpose

The project can be used to study:

* Discord Bot Development;
* Python AsyncIO;
* Security Auditing;
* Permission Management;
* Rate Limiting;
* Logging;
* Incident Response;
* Detection Engineering;
* Recovery Planning.

---

# 🤝 Contributing

Pull requests and issues are welcome.

When adding a new feature, make sure that it:

* is properly documented;
* respects rate limits;
* uses the minimum required permissions;
* includes appropriate safety checks;
* handles errors correctly;
* does not introduce functionality intended for abuse.

---

# 📄 License

This project is distributed under the **MIT License**.

See the `LICENSE` file for the complete license text.

---

# ⭐ Security First

> **Test. Measure. Analyze. Improve.**

An effective security tool should not simply demonstrate that a server can be compromised.

It should help administrators understand:

* which defenses work;
* which configurations are risky;
* which events are detected;
* how security can be improved;
* how to recover from an incident.

---

# 📌 Project Information

```text
Project:
Pugilain-Discord-Nuke-Tool-ED

Main Linux Script:
NukeBotLinux/Nuke.py

Version:
6.0.0

Language:
Python

Platform:
Linux / Kali Linux

License:
MIT

Purpose:
Authorized Discord Security Testing
```

---

## ⚠️ Remember

**Use this project only on servers you own or for which you have explicit authorization.**

**Security testing ≠ attacking.**

The purpose of this project is to help Discord administrators identify weaknesses and improve the security of their servers.
