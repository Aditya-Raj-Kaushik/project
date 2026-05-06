# Quant Market Data & Analytics Platform

A **full-stack quantitative finance system** that ingests, validates, analyzes, and visualizes **OHLCV (Open, High, Low, Close, Volume)** market data with **real-time updates, portfolio analytics, and interactive dashboards**.

---

# 🚀 Overview

This project simulates a **mini institutional-grade market data and analytics platform** used by quant researchers and trading systems.

It integrates:

- Data engineering  
- Financial analytics  
- Real-time systems  
- Frontend visualization  

into a single **end-to-end system**.

---

# 🧠 What This System Does

- Collects live market data  
- Cleans and validates financial time-series  
- Stores historical data  
- Computes quantitative metrics  
- Tracks portfolio performance  
- Visualizes data in real time  

---

# 🏗️ Architecture

```
Market Data API (Yahoo Finance)
            ↓
        Scheduler
            ↓
         FastAPI
       ↙        ↘
   MongoDB     Redis
 (Historical) (Live Cache)
            ↓
        Next.js UI
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI  
- MongoDB  
- Redis  

## Frontend

- Next.js  
- Tailwind CSS  
- Recharts  

## Data & Infrastructure

- Pandas  
- NumPy  
- Python Scheduler  
- Docker  

---

# 📂 Project Structure

```
project/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── fetcher.py
│   ├── validator.py
│   └── cache.py
│
├── scheduler.py
├── quant-dashboard/      # Next.js frontend
├── requirements.txt
├── .env
└── README.md
```

---

# 📥 Features

## 🔹 Data Ingestion

- Fetches OHLCV data from **Yahoo Finance**
- Supports **100+ global assets**
- Automated updates via scheduler

---

## 🔹 Data Validation

- Detects invalid price relationships  
- Filters corrupted data  
- Prevents duplicate entries  

---

## 🔹 Storage Layer

- Historical data stored in **MongoDB**
- Indexed queries for fast retrieval  

---

## 🔹 Real-Time System

- Latest prices cached in **Redis**
- Fast API responses
- Auto-refresh every few seconds  

---

## 🔹 Quant Analytics

### Returns

```
r_t = (P_t - P_{t-1}) / P_{t-1}
```

### Volatility

```
σ = sqrt( (1 / (n-1)) * Σ (r_i - r̄)^2 )
```

### Sharpe Ratio

```
Sharpe = E[R] / σ
```

### Drawdown

```
Drawdown = (Peak - P_t) / Peak
```

---

## 🔹 Portfolio Analytics

- Multi-asset return aggregation  
- Risk metrics  
- Correlation matrix  
- Diversification insights  

---

## 🔹 Anomaly Detection

- Price spike detection  
- Volume anomaly detection  
- Data reliability checks  

---

## 🔹 Dashboard (Next.js)

Features include:

- Live price tracking  
- Price change indicators (green/red)  
- Portfolio metrics  
- Correlation heatmap  
- Price charts  
- Portfolio growth curve  

---

# 📡 API Endpoints

## Core APIs

```
GET /fetch/{symbol}
GET /data/{symbol}
GET /live/{symbol}
GET /chart/{symbol}
```

---

## Analytics APIs

```
GET /analytics/{symbol}/returns
GET /analytics/{symbol}/volatility
GET /analytics/{symbol}/moving-average
GET /analytics/{symbol}/summary
```

---

## Portfolio APIs

```
POST /portfolio/analytics
POST /portfolio/correlation
```

---

## Quality APIs

```
GET /quality/{symbol}
GET /anomaly/{symbol}
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```
git clone <repo-url>
cd project
```

---

## 2️⃣ Setup Backend

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 3️⃣ Run Services (Docker)

```
docker run -d --name quant-mongo -p 27017:27017 mongo
docker run -d --name quant-redis -p 6379:6379 redis
```

---

## 4️⃣ Start Backend

```
uvicorn app.main:app --reload
```

---

## 5️⃣ Run Scheduler

```
python scheduler.py
```

---

## 6️⃣ Setup Frontend

```
cd quant-dashboard
npm install
npm run dev
```

Open in browser:

```
http://localhost:3000
```

---

# 📊 Example Assets

- AAPL  
- MSFT  
- NVDA  
- SPY  
- RELIANCE.NS  

---

# 🧪 What This Project Demonstrates

- Financial data engineering  
- Time-series analysis  
- Portfolio theory implementation  
- Real-time system design  
- Backend + frontend integration  
- Quantitative reasoning  

---

# 📌 Future Enhancements

- WebSocket-based live streaming  
- Advanced portfolio optimization  
- Strategy backtesting engine  
- Multi-source data aggregation  
- ML-based anomaly detection  

---

# 🧾 Resume Line

Developed a full-stack **quantitative market data and analytics platform** with real-time ingestion, validation, Redis caching, portfolio analytics, and interactive dashboards using FastAPI, MongoDB, and Next.js.

---

# ⚠️ Disclaimer

This project is for **educational and research purposes only** and does not constitute financial advice.

---

# 👨‍💻 Author

**Aditya Raj Kaushik**
