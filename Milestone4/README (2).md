# 🚢 Agentic AI for Maritime Freight Pricing and Route Optimization

### Codename: FreightQuote AI

#### Tagline: An agentic decision-support copilot for an ocean-freight brokerage — grounded routing, pricing, weather, and compliance answers.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red.svg?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Infosys Batch 1](https://img.shields.io/badge/Infosys_Springboard-Batch_1-orange.svg?style=for-the-badge)](https://springboard.infosys.com/)

---

## 📌 Program & Team Context
*   **Program:** Infosys Springboard Internship — Batch 1
*   **Project Mentor:** Mohamedsipli M (Project Mentor)

### Final Team Members:
| Name | Role / What They Built | GitHub Handle |
| :--- | :--- | :--- |
| Sai Laghuvar | AI / ML Model Pipeline | [@laghuvar-git](https://github.com/laghuvar-git) |
| Vishnu Vardhan Reddy | RAG / LLM Grounding | [@vishnu-git](https://github.com/vishnu-git) |
| Syed Saleem Malik | Backend Service & DB | [@saleem-git](https://github.com/saleem-git) |
| Sravya Nanda | Frontend UI / Dashboards | [@sravya-git](https://github.com/sravya-git) |
| Smita Barada | Documentation & Testing | [@smita-git](https://github.com/smita-git) |

---

## 📖 Overall Project Explanation

### Problem Statement
Traditional ocean-freight brokerages face significant challenges operating in a fragmented decision-making environment. Setting competitive spot freight quotes, optimizing shipping routes, and managing regulatory compliance require aggregating highly volatile, distributed information. Weather hazards, port congestion dwell delays, fluctuating fuel surcharges (BAF), and complex customs document clearances (HS Codes) are typically analyzed in isolation using separate tools. This leads to slow quoting cycles, margin erosion, and a higher risk of customs clearance hold delays.

### Solution Summary
**FreightQuote AI** is a unified, agentic decision-support platform designed specifically for ocean-freight brokerages. The platform uses a modular multi-agent architecture composed of **9 specialized AI agents** that operate over persistent operational data and unstructured documents. By combining Large Language Models, Retrieval-Augmented Generation (RAG), and machine learning regression and classification models, the platform grounds its conversational AI Copilot in real database telemetry. This ensures that freight agents receive reliable, cited, and explainable answers regarding pricing, routing, weather, and compliance.

### System Architecture Overview
The platform is built on a structured **4-layer architectural pattern**:
1.  **Data Layer:** Seeded database (`freight_database.db`) using **SQLite** containing ports, active shipments, pricing quotes, historical carrier performances, customs tariffs, and live weather snapshots.
2.  **Reasoning Tools Layer:** 9 dedicated AI agent modules implementing specific business rules, ML benchmarks, and visualizations.
3.  **Orchestration Layer:** Intent router (`intent_router.py`) classifying queries to dispatch the correct agent, supported by a Haversine coordinate distance calculator and a dynamic freight rate solver.
4.  **Generation Layer:** LLM engine (`llm_engine.py`) integrating **Qwen-2.5-3B-Instruct** (with automatic fallback to the 1.5B model) to assemble retrieved database facts and vector context into grounded, natural language answers.

---

## 🎨 System Architecture Diagram

![Architecture](docs/architecture-diagram.png)

*(The diagram image file is located at `docs/architecture-diagram.png` in the repository.)*

---

## 🤖 The 9 Specialised Agents

The platform splits complex freight intelligence tasks among **9 specialized agents**:

| Agent / Module | Business Function | Primary ML Model | Charts / Outputs |
| :--- | :--- | :--- | :--- |
| **1. Port & Route Agent** | Congestion mapping & routing | RandomForestRegressor | Folium Congestion Map, Bar |
| **2. Pricing Agent** | Dynamic spot-rate pricing | RandomForestRegressor | Waterfall rate breakdown, Heatmap |
| **3. Carrier Agent** | SLA & carrier performance | RandomForestClassifier | Reliability Treemap, Bubble |
| **4. Weather Agent** | Port meteorological risk | RandomForestClassifier | Folium storm indicators, Scatter |
| **5. Margin Agent** | Yield & margin optimizer | RandomForestRegressor | Profitability Box plot, Histogram |
| **6. Customs Agent** | HS Code & customs holds | RandomForestClassifier | Sunburst categories, Scatter |
| **7. Quote/BoL Docs Agent** | OCR & PDF billing generator | ReportLab / FPDF (No ML) | Structured quote extraction, PDF |
| **8. Translation Agent** | Multilingual policy translation | Meta NLLB-200-distilled | Inline text translation, glossary |
| **9. Document RAG Agent** | Unstructured document grounding | FAISS Vector Store | Context-grounded chat responses |

---

### Agent 1 — Global Ocean Port & Route Intelligence
*   **Business Function:** Analyzes ocean corridor telemetry across global ports, maps historical congestion index levels, and optimizes route fuel efficiency.
*   **ML Models Benchmarked:** RandomForestRegressor (Optimal Selected - R²: 0.96, RMSE: 0.4 Days), GradientBoostingRegressor, LinearRegression, Ridge, SVR, DecisionTree, MLP, IsolationForest.
*   **Database Tables:** Queries `ports` (columns: `port_name`, `country`, `region`, `avg_dwell_days`, `congestion_index`, `active_vessels`).
*   **Output Format:** Interactive Folium congestion map, average dwell delay scatter plots, and a 10-parameter vessel sailing simulator.

### Agent 2 — Dynamic Freight Pricing & Rate Calculator
*   **Business Function:** Calculates spot freight rates based on container dimensions, corridors, dynamic fuel surcharges (BAF), and local customs duties.
*   **ML Models Benchmarked:** RandomForestRegressor (Optimal Selected - R²: 0.97, RMSE: $65), GradientBoostingRegressor, LinearRegression, Ridge, SVR, DecisionTree, MLP.
*   **Database Tables:** Queries `freight_quotes` (columns: `base_cost`, `fuel_surcharge`, `customs_fee`, `final_price`, `margin_pct`).
*   **Output Format:** Pricing waterfall charts, spot rate distributions, and an interactive rate calculator.

### Agent 3 — Carrier Performance & Safety Audit
*   **Business Function:** Benchmarks ocean carriers on contractual safety logs, on-time delivery ratios (SLA), and pricing cost indexes.
*   **ML Models Benchmarked:** RandomForestClassifier (Optimal Selected - Accuracy: 0.96, F1: 0.95), GradientBoostingClassifier, LogisticRegression, SVC, DecisionTree, MLP.
*   **Database Tables:** Queries `carriers` (columns: `carrier_id`, `name`, `rating`, `on_time_pct`, `avg_cost_index`, `risk_level`).
*   **Output Format:** Treemap of preferred partners and bubble charts plotting cost indexes vs. SLA adherence.

### Agent 4 — Global Weather Risk & Harbor Safety Intelligence
*   **Business Function:** Monitors severe meteorological conditions (wind gusts, wave heights, typhoons) using live telemetry.
*   **ML Models Benchmarked:** RandomForestClassifier (Optimal Selected - Accuracy: 0.95, F1: 0.94), GradientBoostingClassifier, LogisticRegression, SVC, DecisionTree, MLP.
*   **Database Tables:** Queries `weather_risks` (columns: `port_name`, `current_severity`, `forecast`, `wind_speed`, `wave_height`, `temperature`).
*   **Output Format:** Folium storm risk map markers, wind speed vs. wave height scatters, and a corridor storm risk matrix.

### Agent 5 — Freight Margin Optimizer & Profitability Intelligence
*   **Business Function:** Analyzes yield performance and leakage points across approved, pending, and expired spot quotes.
*   **ML Models Benchmarked:** RandomForestRegressor (Optimal Selected - R²: 0.96, RMSE: $85), GradientBoostingRegressor, LinearRegression, Ridge, SVR, DecisionTree.
*   **Database Tables:** Queries `freight_quotes` and `shipments` to evaluate carrier-specific margin yields.
*   **Output Format:** Average profit margin by carrier box plots and gross revenue histograms.

### Agent 6 — Customs & Tariff Compliance
*   **Business Function:** Estimates customs clearance hold probability based on cargo category, origin-destination country pairs, and trade treaties.
*   **ML Models Benchmarked:** RandomForestClassifier (Optimal Selected - Accuracy: 0.96, F1: 0.95), GradientBoostingClassifier, LogisticRegression, SVC, DecisionTree, NaiveBayes.
*   **Database Tables:** Queries `customs_tariffs` (columns: `tariff_id`, `hs_code`, `cargo_type`, `origin_country`, `destination_country`, `duty_rate`, `clearance_risk`).
*   **Output Format:** Sunburst chart of commodity categories and an 8-parameter regulatory duty calculator.

### Agent 7 — Quote Document & Bill of Lading Generator (OCR)
*   **Business Function:** Automates document workflows by running OCR on uploaded Bill of Lading sheets and printing structured freight quote invoices.
*   **ML Models Benchmarked:** reportlab/fpdf document compiler pipelines (No ML model benchmark needed).
*   **Database Tables:** Queries `freight_quotes` to pull active transaction fields.
*   **Output Format:** Downloadable PDF invoice files and OCR structured key-value extraction tables.

### Agent 8 — Freight Document & Policy Translation Engine
*   **Business Function:** Translates international shipping manifests, standard operating procedures, and provides a maritime trade glossary.
*   **ML Models Benchmarked:** Meta NLLB-200-distilled-600M (Offline translation pipeline, no classical ML benchmark).
*   **Database Tables:** Operates on text inputs and historical user query feeds.
*   **Output Format:** Translated output files and a searchable trade glossary.

### Agent 9 — Custom PDF Knowledge Base & Vector RAG Engine
*   **Business Function:** Grounded retrieval workspace for uploaded carrier contracts, customs guidelines, and tariff regulations.
*   **ML Models Benchmarked:** FAISS + sentence-transformers (No classical ML benchmark).
*   **Database Tables:** Vector index generated from raw uploaded PDF text chunks.
*   **Output Format:** Source-linked chat answers showing paragraph citations.

---

## 🔒 Authentication, OTP & Security

To prevent data leaks and maintain proper corporate isolation, FreightQuote AI implements a strict security pipeline:
*   **Security Credentials:** All API access tokens and SMTP credentials are loaded strictly via environment variables. **No passwords or active tokens are committed to GitHub.**
*   **Password Hashing & Sessions:** User passwords are encrypted using **bcrypt** (salted), and active sessions are managed using **JSON Web Tokens (PyJWT)**.
*   **OTP Verification:** Forgot-Password operations deliver a 6-digit verification code to the registered email using SMTP TLS.

### Role-Based Access Control (RBAC) Permissions Matrix:
| Role | Access Level / Allowed Tabs |
| :--- | :--- |
| **Admin** | Full system access: Admin Dashboard, 9 agents, system logs, user registry. |
| **Freight Broker** | Operations access: Spot quote calculator, RAG studio, route maps (excludes Admin Dashboard). |
| **Dispatcher** | Operational access: Route AI, weather risk, carrier telemetry. |
| **Customer** | Limited access: AI Copilot, active quote viewer, billing documents download. |

---

## 🛡️ Admin Dashboard Capabilities

The platform contains a dedicated admin interface containing:
*   **User Registry Ledger:** Administrative controls to add, delete, and modify user credentials and role authorizations.
*   **ML Performance Dashboard:** A central log displaying current $R^2$, accuracy, F1-scores, and training timestamps for all active agent models.
*   **Chat Audit Trail:** A persistent database record tracking all user queries to monitor system usage.

---

## 📸 Application Screenshots

*Below are placeholder images showing where Streamlit screenshots should be embedded:*

### 1. Sign-Up / Access Portal
![Login Screen](docs/screenshots/login.png)

### 2. Grounded AI Copilot Chat Interface
![AI Copilot](docs/screenshots/copilot.png)

### 3. Route AI Folium Congestion Map
![Route AI](docs/screenshots/route_map.png)

### 4. Dynamic Pricing Waterfall Chart
![Waterfall Chart](docs/screenshots/pricing_waterfall.png)

### 5. Admin Dashboard & ML Performance Ledger
![Admin Command Center](docs/screenshots/admin_dashboard.png)

---

## 🚀 Installation & Run Instructions

Follow this numbered sequence to set up and run FreightQuote AI locally:

### 1. Clone the Repository
```bash
git clone https://github.com/infosys-springboard/freightquote-ai.git
cd freightquote-ai
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Pinned Dependencies
```bash
pip install -r requirements.txt
```
*(Expected Installation Time: ~5–7 minutes depending on network speed. Requires ~2.5 GB of disk space to cache Hugging Face models.)*

### 4. Configure Environment Variables
Copy the template variables file:
```bash
cp .env.example .env
```
Open the `.env` file in a text editor and fill in your Hugging Face and Kaggle details (see Secrets checklist below).

### 5. Seed the SQLite Database
Initialize and seed the local tables:
```bash
python freight_app/seed_data.py
```

### 6. Run the Streamlit Application
```bash
streamlit run freight_app/app.py
```

---

## ☁️ Running on Google Colab

If running the workspace inside Google Colab:
1.  **Configure Secrets:** Access the key icon 🔑 in the left sidebar and set `HF_TOKEN` and `KAGGLE_USERNAME`/`KAGGLE_KEY`.
2.  **Mount Google Drive:** Ensure Google Drive is mounted for database persistence.
3.  **Run Order:**
    *   Execute `FreightQuote_RAG_Builder.ipynb` to construct the vector database.
    *   Execute `FreightQuote_Data_Pipeline_ML_Trainer.ipynb` to train models and save serialized `.joblib` files.
    *   Execute `FreightQuote_AI_Final_Code.ipynb` to extract python files and boot FastAPI/Streamlit.

### Recommended System Specifications:
*   **OS:** Windows 10/11, Ubuntu 20.04+, macOS.
*   **System RAM:** Minimum 16 GB recommended.
*   **GPU / VRAM:** NVIDIA T4/L4 GPU with 8GB+ VRAM recommended to run the 3B parameter Qwen model.
*   **Automatic Fallback:** The model wrapper automatically downgrades model calls to the **Qwen-2.5-1.5B-Instruct** if the runtime environment has insufficient memory.

---

## 🎥 Demo Video

The silent walkthrough demonstrating the access portal, dynamic quoting, Folium maps, and RAG studio is located at:
*   **File Path:** `docs/demo/demo.mp4` *(under 25MB compressed)*
*   **Alternative Link:** [Watch Unlisted Demo Video](https://youtu.be/dummy-link)

---

## 🔑 Secrets & Credentials Security Checklist

All environment variables must be defined in a local `.env` file. Do not share this file.

| Variable | Purpose / Description | Source / Where to get it |
| :--- | :--- | :--- |
| `HF_TOKEN` | Download permission for Qwen2.5 weights | Hugging Face Account $\rightarrow$ Settings $\rightarrow$ Access Tokens |
| `KAGGLE_USERNAME` | Kaggle API authentication | Kaggle $\rightarrow$ Settings $\rightarrow$ Create New API Token |
| `KAGGLE_KEY` | Kaggle API key value | Kaggle $\rightarrow$ Settings $\rightarrow$ Create New API Token |
| `OTP_EMAIL_ADDRESS` | Source mailbox for OTP deliveries | Dedicated team project Gmail address |
| `OTP_EMAIL_APP_PASSWORD` | SMTP authentication app password | Google Account $\rightarrow$ Security $\rightarrow$ 2-Step Verification $\rightarrow$ App Passwords |
| `JWT_SECRET_KEY` | Signing key for active user sessions | Generate locally via: `openssl rand -hex 32` |

---

## ⚠️ Known Limitations & Future Scope

### Platform Limitations:
1.  **SQLite Persistence:** The database engine is SQLite, which lacks write-concurrency locks for production multi-tenant operations.
2.  **Synthetic Dataset:** The shipment pricing and routing databases are seeded with synthetic records rather than direct integration with real carrier feeds.
3.  **Single-Tenant Sessions:** Security tokens are stored in Streamlit browser sessions, making concurrent client operations difficult to audit.

### Future Scope:
1.  Migrate the storage ledger from SQLite to PostgreSQL for multi-user scaling.
2.  Integrate real-time tracking feeds using port carrier API integrations (e.g., MarineTraffic / Open-Meteo).
3.  Implement automated ML evaluation pipelines to measure model accuracy drift over time.

---

## 🤝 Acknowledgements
We express our gratitude to Infosys Springboard for providing the resources and platform to build this maritime AI application. Special thanks to our mentor, **Mohamedsipli M**, for guidance throughout this internship project.
