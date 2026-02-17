# ApexBox (Patent Pending)

![Status](https://img.shields.io/badge/Status-Prototyping-orange)
![License](https://img.shields.io/badge/License-Proprietary-red)
![Patent](https://img.shields.io/badge/Patent-Pending%20(2026)-blue)
![Discord](https://img.shields.io/discord/1341188636757659648?color=5865F2&label=Community&logo=discord&logoColor=white)

**High-Performance Automotive Telemetry & GPS Datalogging Ecosystem.**

---

## 🏎️ Overview

**ApexBox** is a headless, race-grade telemetry module designed for grassroots motorsport. By combining **25Hz multi-constellation GNSS** with direct **OBD2 CAN bus integration**, it delivers professional-level data fidelity at a fraction of the cost of traditional loggers.

> **⚠️ Current Status:** Prototype 2 (Regulator Validation Phase). Housing design is in CAD development.

---

## 🚀 Key Features

*   **25Hz GNSS Positioning:** Updates position 25 times per second (vs. 1Hz on standard phones).
*   **Direct ECU Bridge:** Pulls real-time engine data (RPM, TPS, Temps) via CAN bus.
*   **Headless Design:** Zero-distraction "Ghost Box" form factor. Auto-wake/sleep.
*   **BLE 5.0 Streaming:** Low-latency data transmission to the ApexBox Companion App.
*   **VirtualDyno™:** Real-time horsepower and torque calculation based on GPS acceleration data.

---

## 🛠️ Hardware Specifications (Target)

| Component | Specification | Status |
| :--- | :--- | :--- |
| **MCU** | ESP32-S3 Dual-Core @ 240MHz | ✅ Validated |
| **GNSS** | Multi-Constellation (GPS/GLONASS) | ✅ Validated (25Hz) |
| **OBD2** | ISO 15765-4 CAN Bus Interface | ✅ Validated |
| **Power** | 12V Vehicle Power (Internal Reg) | ⚠️ Proto 2 Testing |
| **Housing** | MJF Nylon PA12 (Heat Resistant) | 🚧 In CAD Design |

---

## 📅 Roadmap

*   **Nov 2025:** Project Inception & Concept.
*   **Jan 2026:** Prototype 1 Testing (Proof of Concept).
*   **Feb 2026:** Patent Filing & Prototype 2 Development (Current).
*   **Mar 2026:** Prototype 3 (PCB Refinement).
*   **Q2 2026:** Production Launch & Shipping.

---

## 🔗 Links & Resources

*   **🌐 Official Website:** [phobiagg.github.io/apexbox](https://phobiagg.github.io/apexbox/)
*   **💬 Discord Community:** [Join the Waitlist & Chat](https://discord.gg/YOUR_INVITE_LINK)
*   **📄 Documentation:** See `MASTER_DOCUMENTATION.md` for technical details.

---

**Copyright © 2026 Jaiden James (ApexBox). Patent Pending. All Rights Reserved.**
