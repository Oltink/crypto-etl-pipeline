# 🚀 Crypto ETL Pipeline

An ETL (Extract, Transform, Load) pipeline for fetching, processing, and storing cryptocurrency price data in PostgreSQL using Apache Airflow and Docker.

---

## 🧩 Features

- 📥 Fetches real-time prices for **Bitcoin** and **Ethereum** using the CoinGecko API
- 🧠 Transforms and parses JSON response
- 🗄️ Loads data into a **PostgreSQL** database
- ⏱️ Schedules tasks with **Apache Airflow**
- 🐳 Runs everything via **Docker Compose**

---

## 📦 Tech Stack

- **Python 3**
- **Apache Airflow**
- **PostgreSQL**
- **Docker + Docker Compose**
- **CoinGecko Public API**

---

## 📁 Project Structure

crypto-etl-pipeline/
│
├── dags/
│   └── crypto_pipeline.py         # Main DAG pipeline
│
├── config/
│   └── airflow.cfg                # Airflow configuration (if used)
│
├── logs/                          # Airflow logs (excluded from Git)
│
├── docker-compose.yml             # Docker services for Airflow, PostgreSQL
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (excluded from Git)
├── .gitignore                     # Git ignore rules
├── README.md                      # Project documentation

---

## ⚙️ How to Run Locally

# 1. Clone the repository
git clone https://github.com/Oltink/crypto-etl-pipeline.git
cd crypto-etl-pipeline

# 2. Start services
docker-compose up --build

# 3. Access Airflow at:
http://localhost:8080

---

# Default Airflow login:

Username: admin
Password: admin

---

# 📦 Installation( ven v - optional ) 

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

---

# Testing the Pipeline( optional )

# List DAGs
airflow dags list

# Trigger manually
airflow dags trigger crypto_price_pipeline

# Check logs
airflow tasks logs save_prices <run_id>

---

## License
Distributed under the Apache 2.0 License. See [LICENSE](./LICENSE) for more information.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

