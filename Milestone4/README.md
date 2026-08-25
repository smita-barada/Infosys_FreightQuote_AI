# 🚢 FreightQuote AI

### AI-Powered Maritime Freight Quote Generation & Intelligence Platform

**Transforming maritime freight quoting with AI, RAG, multi-agent intelligence, analytics, and grounded decision support.**


## 📌 Overview

**FreightQuote AI** is an AI-powered maritime freight intelligence platform designed to improve the way freight quotes are generated, analyzed, and managed.

The platform combines **Large Language Models, Retrieval-Augmented Generation (RAG), multi-agent intelligence, port analytics, anomaly detection, multilingual assistance, and persistent data storage** into a single professional system.

The goal is simple:

> **Make maritime freight quoting faster, more intelligent, explainable, and reliable.**

Instead of relying only on static rules or manually searching through documents, FreightQuote AI provides an intelligent workflow that can use structured freight information together with relevant knowledge retrieved from documents.

---

# ✨ Key Features

## 🤖 Grounded AI Copilot

An AI Copilot designed to provide more reliable responses by grounding its answers in available project knowledge and retrieved information.

**Benefits:**

* Reduces unsupported AI responses
* Provides context-aware assistance
* Supports freight-related queries
* Works with the platform's RAG capabilities

---

## 🧠 Multi-Agent Freight Intelligence

FreightQuote AI uses a multi-agent approach to divide freight intelligence tasks into specialized responsibilities.

This allows different parts of the system to focus on areas such as:

* Freight intelligence
* Quote-related analysis
* Route and port information
* Knowledge retrieval
* AI-assisted decision support

The objective is to create a more structured and modular AI workflow rather than depending on a single generic model.

---

## 📄 PDF + RAG Knowledge System

The platform includes PDF/RAG capabilities for working with external knowledge sources.

### RAG Workflow

```text
Documents / PDFs
       ↓
Document Processing
       ↓
Chunking
       ↓
Embeddings
       ↓
Vector Knowledge Base
       ↓
User Query
       ↓
Relevant Context Retrieval
       ↓
AI Model
       ↓
Grounded Response
```

This approach allows the AI system to retrieve relevant information before generating an answer.

---

## ⚓ 100+ Global Ports

The upgraded platform includes support for **100+ global ports**, enabling freight-related analysis across a broader maritime network.

Port information can be used for:

* Port exploration
* Freight analysis
* Route-related intelligence
* Port comparison
* Visualization
* Analytics

---

## 📊 Port Analytics & Map

FreightQuote AI provides an analytics-oriented view of maritime ports.

The platform combines port information with visual analytics to make geographical and operational information easier to understand.

### Analytics Capabilities

* Port exploration
* Geographic visualization
* Port-level analytics
* Route-related insights
* Interactive map-based analysis

---

## 🚨 Alerts & Anomaly Detection

The system includes alerting and anomaly-detection capabilities to identify potentially unusual or important events.

This can help users identify:

* Unexpected patterns
* Potential anomalies
* Important freight-related events
* Conditions requiring attention

The platform is designed to move beyond simply generating information toward **proactive intelligence**.

---

## 🌐 Multilingual AI Copilot

The Copilot is designed with multilingual interaction in mind, allowing users to interact with the AI system across supported languages.

This makes the platform more accessible for users operating in different regions and international maritime environments.

---

## 🛡️ Admin Dashboard

FreightQuote AI includes an administrative dashboard for managing and monitoring the platform.

The admin functionality provides a centralized interface for platform-level operations and oversight.

---

## 💾 Persistent SQLite Database

The platform uses **SQLite** for persistent application data storage.

This provides a lightweight database layer suitable for:

* Local development
* Demonstration
* Colab-based execution
* Persistent application data
* Structured project storage

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │      User / Admin    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Professional UI   │
                         └──────────┬──────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │ AI Copilot   │    │ Freight      │    │ Port         │
        │              │    │ Intelligence │    │ Analytics    │
        └──────┬───────┘    └──────┬───────┘    └──────────────┘
               │                   │
               ▼                   ▼
        ┌─────────────────────────────────┐
        │       Multi-Agent Layer         │
        └───────────────┬─────────────────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
      ┌──────────────┐    ┌──────────────┐
      │ RAG / PDF    │    │ AI Models    │
      │ Knowledge    │    │ & Inference  │
      └──────┬───────┘    └──────┬───────┘
             │                   │
             └─────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ SQLite Database  │
              └──────────────────┘
```

---

# 🔄 How FreightQuote AI Works

### 1. User Input

The user provides a freight-related request through the application.

### 2. Intelligent Processing

The request is analyzed and routed through the appropriate intelligence components.

### 3. Knowledge Retrieval

When relevant, the RAG pipeline retrieves useful information from the available document knowledge base.

### 4. Multi-Agent Reasoning

Specialized AI components process the information required for the task.

### 5. Grounded AI Response

The Copilot generates a response using the available context to reduce unsupported responses.

### 6. Analytics & Alerts

Relevant information can be visualized through port analytics, maps, and alert mechanisms.

---

# 🛠️ Technology Stack

| Category            | Technology            |
| ------------------- | --------------------- |
| Programming         | Python                |
| Environment         | Google Colab          |
| AI                  | Large Language Models |
| AI Architecture     | Multi-Agent System    |
| Knowledge Retrieval | RAG                   |
| Documents           | PDF Processing        |
| Database            | SQLite                |
| Visualization       | Maps & Analytics      |
| Language Support    | Multilingual AI       |
| Runtime             | GPU Recommended       |

### Recommended Runtime

For faster AI inference, the project recommends using a GPU runtime such as:

* **NVIDIA T4**
* **NVIDIA L4**
* **NVIDIA A100**

---

# 📁 Project Structure

```text
FreightQuote-AI/
│
├── 📓 FreightQuote_AI_Milestone4_Professional_Colab.ipynb
│
├── 📂 data/
│   ├── documents/
│   ├── ports/
│   └── knowledge_base/
│
├── 📂 models/
│
├── 📂 rag/
│
├── 📂 agents/
│
├── 📂 database/
│
├── 📂 ui/
│
├── 📂 screenshots/
│
└── README.md
```

> The exact repository structure should match the folders actually committed to GitHub. Don't add folders to this section just because they sound appropriate.

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd <YOUR-REPOSITORY>
```

## 2. Open the Notebook

Open:

```text
FreightQuote_AI_Final_Code_(1)_(1).ipynb
```

using **Google Colab**.

## 3. Select a GPU Runtime

In Google Colab:

```text
Runtime
   ↓
Change runtime type
   ↓
Hardware accelerator
   ↓
GPU
```

A T4/L4/A100 runtime is recommended for faster model inference.

## 4. Run the Notebook

Execute the notebook cells sequentially.

The notebook acts as the launcher for the upgraded Milestone 4 FreightQuote AI platform.

---

# 🎯 Project Objectives

FreightQuote AI focuses on solving several challenges in maritime freight intelligence:

### Traditional Challenge

```text
Manual Information Search
        ↓
Scattered Data
        ↓
Time-Consuming Analysis
        ↓
Limited Automation
        ↓
Delayed Decision Making
```

### FreightQuote AI Approach

```text
User Request
     ↓
AI Processing
     ↓
Knowledge Retrieval
     ↓
Multi-Agent Intelligence
     ↓
Grounded Response
     ↓
Analytics / Alerts
     ↓
Better Decision Support
```

---

# 🌟 Milestone 4 Upgrades

The Milestone 4 version introduces several major platform improvements:

| Feature                     | Status |
| --------------------------- | :----: |
| 🤖 Grounded AI Copilot      |    ✅   |
| ⚓ 100+ Global Ports         |    ✅   |
| 🎨 Professional UI          |    ✅   |
| 📊 Port Analytics           |    ✅   |
| 🗺️ Port Map                |    ✅   |
| 🧠 Multi-Agent Intelligence |    ✅   |
| 📄 PDF / RAG Tools          |    ✅   |
| 🚨 Alerts                   |    ✅   |
| 🔍 Anomaly Detection        |    ✅   |
| 🛡️ Admin Dashboard         |    ✅   |
| 💾 SQLite Persistence       |    ✅   |
| 🌐 Multilingual Copilot     |    ✅   |

## 🧠 Multi-Agent Maritime Intelligence

FreightQuote AI is built around a specialized multi-agent architecture where individual AI agents focus on different aspects of maritime freight operations.

| Agent / Module | Purpose |
|---|---|
| 🤖 AI Copilot | Conversational AI for freight-related assistance |
| ⚓ Port Network | Global maritime port exploration and intelligence |
| 🧭 Route AI | Maritime route analysis and decision support |
| 💰 Spot Quotes | Freight spot-quote and pricing intelligence |
| 🚚 Carriers | Carrier-related freight intelligence |
| 🌦️ Weather Risk | Weather-related shipping risk analysis |
| 📈 Margin Predictor | Freight margin and profitability prediction |
| 📑 Customs & Tariff | Customs and tariff-related intelligence |
| 📄 Docs (OCR) | Extracts information from documents using OCR |
| 🚨 Alerts & Incidents | Monitors important incidents and operational events |
| 🔔 Notifications | Delivers important system notifications |
| 🌐 Translation | Multilingual interaction and translation |
| 🕸️ Knowledge Graph | Represents relationships between maritime entities and information |
| 🔄 Digital Twin | Simulates and represents the maritime operational environment |
| 🔍 Anomaly Scanner | Detects unusual patterns and potential anomalies |
| 📚 PDF RAG Studio | Enables document-based RAG and knowledge retrieval |
| ☁️ Data Feed Center | Centralized data-feed management |
| 🛡️ Admin Dashboard | Platform administration and monitoring |
---

# 🔬 AI & RAG Pipeline

The knowledge-grounding pipeline follows a retrieval-based architecture:

```text
             ┌───────────────┐
             │ PDF Documents │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Text Extract  │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │   Chunking    │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │  Embeddings   │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │ Vector Search │
             └───────┬───────┘
                     ↓
              Relevant Context
                     ↓
             ┌───────────────┐
             │ AI / Copilot  │
             └───────┬───────┘
                     ↓
             Grounded Response
```

---

# 💡 Why This Project?

Maritime freight operations involve large amounts of information distributed across documents, ports, routes, and operational data.

FreightQuote AI brings these information sources together into an AI-assisted environment.

### The platform aims to provide:

* ⚡ Faster information access
* 🧠 AI-assisted analysis
* 📚 Knowledge-grounded responses
* ⚓ Maritime port intelligence
* 📊 Visual analytics
* 🚨 Proactive anomaly awareness
* 🌐 Multilingual interaction
* 🛡️ Administrative control

---

# 📈 Future Enhancements

Potential future improvements include:

* Real-time freight-rate integration
* Live vessel tracking
* Advanced route optimization
* Dynamic freight-price prediction
* Cloud deployment
* API-based architecture
* Scalable vector databases
* Advanced model evaluation
* Automated quote comparison
* Real-time maritime data integration

---

# 👥 Team

**Project:** FreightQuote AI
**Milestone:** 4
**Domain:** Artificial Intelligence + Maritime Logistics
**Platform:** Google Colab

### Contributors

| Name                | Role          |
| -----------         | ------------- |
| Sai Laghuvar        | AI / ML       |
| Vishnu Vardhan Reddy| RAG / LLM     |
| Syed Saleem Malik   | Backend       |
| Sravya Nanda        | Frontend / UI |
| Smita Barada        | README.MD     |

---

# 📚 Project Context

This project was developed as part of an **AI-based maritime freight intelligence and quote-generation initiative**, combining modern AI techniques with domain-specific freight knowledge.

The Milestone 4 implementation focuses on turning the earlier freight-quote concept into a more complete AI-assisted platform with grounded Copilot functionality, multi-agent intelligence, port analytics, RAG tools, alerts, administration, persistence, and multilingual interaction.

---

# ⚠️ Disclaimer

This project is intended for **educational, research, and demonstration purposes**.

AI-generated outputs should be validated against authoritative maritime, commercial, and operational data before being used for real-world business decisions.

---

# ⭐ Support the Project

If you find this project useful:

⭐ **Star the repository**

🍴 **Fork the repository**

🐛 **Report issues**

💡 **Suggest improvements**

🤝 **Contribute**

---

### 🚢 FreightQuote AI

**AI-powered intelligence for smarter maritime freight decisions.**

# 📸 Application Screenshots

### 🚢 SignUp page:
<img width="1908" height="888" alt="Screenshot 2026-08-18 184737" src="https://github.com/user-attachments/assets/7fdc0fcf-8ccb-4723-a6c6-7ac40b1ea12e" />

### 🤖 AI Copilot:
The main conversational interface of the platform. Users can interact with the AI to ask freight-related questions and receive intelligent assistance.
<img width="1898" height="868" alt="Screenshot 2026-08-18 190536" src="https://github.com/user-attachments/assets/5f846ccd-cc88-4c8e-ad47-09ee0b43adb6" />

### ⚓ Port Network:
Provides access to the maritime port network and information about supported ports, helping users explore the global freight ecosystem.
<img width="1901" height="900" alt="Screenshot 2026-08-18 190756" src="https://github.com/user-attachments/assets/2ec93cd1-061d-4563-a2fa-cf593696bb12" />

### 🧭 Agent 1 — Route AI:
Analyzes and assists with maritime route-related decisions, helping users understand possible routes and route information.
<img width="1903" height="742" alt="Screenshot 2026-08-18 191000" src="https://github.com/user-attachments/assets/d821d952-5bba-44fb-bbc5-57da6c9d2d85" />

### 🧭 Agent 2 — Spot Quotes:
Handles spot freight quote intelligence, helping users work with freight pricing and quote-related information.
<img width="1911" height="898" alt="Screenshot 2026-08-18 191151" src="https://github.com/user-attachments/assets/af4ae157-b499-4ada-87c4-423cde5d0521" />

### 🧭 Agent 3 — Carriers:
Provides carrier-related intelligence, helping users analyze or retrieve information associated with shipping carriers.
<img width="1908" height="918" alt="Screenshot 2026-08-18 191543" src="https://github.com/user-attachments/assets/789afea9-0e3a-4c61-80ac-721f38be9688" />

### 🌦️ Agent 4 — Weather Risk:
Focuses on weather-related maritime risks, helping identify how weather conditions can potentially affect shipping operations and routes.
<img width="1906" height="857" alt="Screenshot 2026-08-18 191559" src="https://github.com/user-attachments/assets/db54a6ac-3c73-47ff-bad8-cbabe4d3ae7e" />

### 📈 Agent 5 — Margin Predictor:
Focuses on margin prediction, helping estimate potential profitability associated with freight quotations.
<img width="1903" height="908" alt="Screenshot 2026-08-18 191620" src="https://github.com/user-attachments/assets/38495d66-ca69-4fe6-8056-62c1345908bf" />

### 📑 Agent 6 — Customs & Tariff:
Provides intelligence related to customs requirements and tariffs, helping users understand trade-related cost and regulatory considerations.
<img width="1908" height="908" alt="Screenshot 2026-08-18 191651" src="https://github.com/user-attachments/assets/72c4e90e-333c-4618-bdd0-58299de0d6b7" />

### 📄 Agent 7 — Docs (OCR):
Uses Optical Character Recognition (OCR) to extract useful information from documents, making document-based freight information easier to process.
<img width="1917" height="891" alt="Screenshot 2026-08-18 191712" src="https://github.com/user-attachments/assets/2d2887d1-bd84-423c-aa12-c2af190f3375" />

### 🚨 Agent 8 — Alerts & Incidents):

Handles alerts and incident-related intelligence, helping users identify and monitor important events that may affect freight operations.

### 🔔Notification:

Provides notifications for important system events, alerts, or updates so users don't have to continuously monitor the platform.

### 🌐 Agent 8 — Translation:

The screenshot labels this as Agent 8: Translation. It supports multilingual interaction and translation capabilities within the platform.
<img width="1907" height="907" alt="Screenshot 2026-08-18 192104" src="https://github.com/user-attachments/assets/4824f9bf-9953-4288-8aae-fcd348f413aa" />


### 🕸️ Knowledge Graph:
Connects and represents relationships between relevant entities and information, providing a structured knowledge layer for the system.
<img width="1901" height="905" alt="Screenshot 2026-08-18 192123" src="https://github.com/user-attachments/assets/77899bcf-d8a1-4451-afef-f9f6aa61c6b7" />

### 🔄 Digital Twin:
Provides a digital representation/simulation of the maritime environment or operational system, allowing the platform to model and explore scenarios.
<img width="1897" height="893" alt="Screenshot 2026-08-18 192140" src="https://github.com/user-attachments/assets/edc4fcd3-b26d-4751-9ba6-29a210a5004e" />

### 🔍 Anomaly Scanner:
Looks for unusual or abnormal patterns/events that may require attention.
<img width="1900" height="897" alt="Screenshot 2026-08-18 192207" src="https://github.com/user-attachments/assets/f601a55a-a821-450b-b04d-06d8ff46ac7d" />

### 📚 Agent 9 — PDF RAG Studio:
Provides a Retrieval-Augmented Generation (RAG) environment for working with PDF documents and using their content as a knowledge source for AI responses.
<img width="1902" height="860" alt="Screenshot 2026-08-18 192236" src="https://github.com/user-attachments/assets/76a40ec1-71b4-4991-9192-a526f25a9280" />

### ☁️ Data Feed Center:
Acts as a central area for managing or accessing incoming data feeds used by the platform.
<img width="1905" height="892" alt="Screenshot 2026-08-18 192252" src="https://github.com/user-attachments/assets/f732bcd4-b68d-4391-86f5-c65e47ebbd3e" />

### 🛡️ Admin Dashboard:
Provides administrative access for monitoring and managing the platform.
<img width="1906" height="897" alt="Screenshot 2026-08-18 192324" src="https://github.com/user-attachments/assets/e668dcec-2a6f-45a8-9a9e-b09a9e5d1c8b" />
