# 📈 Market Logic AI: S&P 500 Intelligence Pipeline

**Market Logic AI** is a production-grade financial tool that automates the generation of trading signals using a live Data-as-a-Service (DaaS) architecture. 

### 🚀 Live Demo
* **Interactive Dashboard:** [https://market-logic-ai.streamlit.app](https://market-logic-ai.streamlit.app)
* **Production API (Swagger):** [https://market-logic-ai.hub.zerve.cloud/docs](https://market-logic-ai.hub.zerve.cloud/docs)
* **Zerve Logic & Backtest:** [https://www.zerve.ai/gallery/073645cd-9e82-42e6-8985-1a423a66fb79](https://www.zerve.ai/gallery/073645cd-9e82-42e6-8985-1a423a66fb79)

---

### 🧠 The Problem
Manual market analysis is prone to psychological bias and data latency. This project asks: *Can we build a system that moves from raw economic data to a validated signal in sub-seconds?*

### 🛠️ Technical Architecture
This project utilizes a **Directed Acyclic Graph (DAG)** to ensure data integrity and automated execution:

1. **Data Layer:** Real-time ingestion of 11 years of S&P 500 data via the **FRED (Federal Reserve)** API.
2. **Orchestration Layer:** Built on **Zerve**, utilizing a DAG to handle data cleaning, 20-day SMA calculation, and historical backtesting.
3. **Backend Layer:** A **FastAPI** microservice hosted on Zerve Hub, exposing the strategy logic via a RESTful API.
4. **Frontend Layer:** A **Streamlit** dashboard that consumes the API to provide real-time "Decision-Grade" visuals for users.

### 📊 Key Features
* **Live Signal Engine:** Color-coded BUY/SELL indicators based on validated trend-following logic.
* **Integrated Backtesting:** Every signal is served alongside a historical win-rate metric.
* **Automated Pipeline:** No manual data handling; the system is "always-on."

### 💻 Local Setup
1. Clone the repo: `git clone https://github.com/infosectestwin/market-logic-ai`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app.py`

---
*Developed for the 2026 Zerve Hackathon. Part of the "The Inner Hour" project series exploring AI and Human Decision Making.*