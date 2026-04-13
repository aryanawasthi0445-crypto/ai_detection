# Project Report: AI Violence & Weapon Detection System

## 1. Table of Content
1. [Table of Content](#1-table-of-content)
2. [Abstract](#2-abstract)
3. [Introduction](#3-introduction)
4. [Problem Statement and Proposed Solutions](#4-problem-statement-and-proposed-solutions)
5. [Hardware and Software Requirements](#5-hardware-and-software-requirements)
6. [Analysis (Use Case Diagram)](#6-analysis-use-case-diagram)
7. [Conclusion](#7-conclusion)

---

## 2. Abstract
The AI Violence & Weapon Detection System is a real-time monitoring solution that leverages Deep Learning to enhance public safety. Utilizing the YOLOv8 architecture, the system identifies persons and weapons (e.g., knives) within a video feed. It further analyzes the interaction between detected entities using heuristic algorithms to flag potential violent acts. The system is designed for high-performance execution on both CPU and GPU (CUDA) environments, providing visual alerts and JSON-structured logs for seamless backend integration.

---

## 3. Introduction
In modern security environments, the volume of surveillance data often exceeds the capacity of human operators to monitor effectively. This project introduces an automated AI-driven layer to traditional monitoring.

**Purpose:** To provide an autonomous detection mechanism that reduces response time for security personnel during critical incidents.
**Scope:** Real-time analysis of webcam feeds, pre-recorded video files, and network-based RTSP streams.
**Key Features:**
*   Human and Weapon detection via YOLOv8.
*   Proximity-based risk assessment.
*   Automated screenshot logging for evidence collection.
*   Modular detection pipeline for easy scalability.

---

## 4. Problem Statement and Proposed Solutions

### Problem Statement
Traditional surveillance systems rely heavily on manual observation. This approach suffers from:
1.  **Human Fatigue:** Continuous monitoring leads to decreased attention spans and missed events.
2.  **Delayed Response:** Identifying a threat manually and notifying authorities takes critical seconds or minutes.
3.  **Scalability Issues:** Managing hundreds of camera feeds simultaneously is nearly impossible for small security teams.

### Proposed Solutions
The system addresses these issues by:
*   **Automation:** AI models never fatigue and can monitor multiple frames per second with consistent accuracy.
*   **Instant Alerting:** The system triggers visual and data-driven alerts the moment a threat is identified.
*   **Intelligent Heuristics:** Beyond simple object detection, the system analyzes movement patterns and entity distances to differentiate between normal activity and violence.

---

## 5. Hardware and Software Requirements

### Hardware Requirements
*   **Processor:** Intel i5/AMD Ryzen 5 or higher.
*   **Memory:** 8GB RAM (Minimum), 16GB (Recommended).
*   **Graphics:** NVIDIA GPU with 4GB+ VRAM (Recommended for real-time inference).
*   **Input Device:** Standard USB Webcam or IP Camera supporting RTSP.

### Software Requirements
*   **Operating System:** Windows 10/11, Ubuntu 20.04+, or macOS.
*   **Environment:** Python 3.10.x.
*   **Core Libraries:**
    *   `ultralytics==8.2.0` (YOLOv8 framework)
    *   `torch==2.3.1` (Deep Learning backend)
    *   `opencv-python==4.9.0.80` (Image processing)
    *   `numpy==1.26.4` (Numerical computation)

---

## 6. Analysis (Use Case Diagram)

The following diagram illustrates the interactions between the user, the camera source, and the internal AI detection engine.

```mermaid
usecaseDiagram
    actor "Security Personnel" as user
    actor "Camera/Video Source" as camera
    
    package "AI Detection System" {
        usecase "Initialize Stream" as UC1
        usecase "Process Visual Feed" as UC2
        usecase "Detect Persons & Weapons" as UC3
        usecase "Analyze Violence Heuristics" as UC4
        usecase "Display Real-Time Feed" as UC5
        usecase "Trigger Visual Alerts" as UC6
        usecase "Save Evidence Screenshots" as UC7
    }

    camera --> UC1
    UC1 --> UC2
    UC2 --> UC3
    UC3 --> UC4
    UC4 --> UC5
    UC4 --> UC6
    UC6 --> UC7
    UC5 --> user
    UC6 --> user
```

---

## 7. Conclusion
The AI Violence & Weapon Detection System successfully demonstrates the feasibility of using lightweight object detection models for critical security applications. By combining the speed of YOLOv8 with custom behavioral analysis, the project provides a robust foundation for modern surveillance. Future enhancements could include multi-camera tracking, audio-based threat detection, and integration with cloud-based notification services (SMS/Email) to further improve situational awareness and emergency response times.
