# 🛡️ Real-Time Multimodal Content Moderation System

An end-to-end, containerized AI content safety microservice engineered to evaluate text for toxicity, hate speech, and harmful content with sub-150ms inference response times.

---

## 🚀 Key Features

* **Transformer-Powered Engine:** Contextual toxicity classification powered by Hugging Face Transformer models (`unitary/toxic-bert`).
* **High-Performance REST API:** Built with **FastAPI** leveraging asynchronous non-blocking execution and strict **Pydantic** payload validation.
* **Interactive Dashboard:** Live **Streamlit** user interface to analyze text, view real-time confidence scores, and monitor execution latency.
* **Containerized Deployment:** Fully orchestrated microservice architecture using **Docker** and **Docker Compose** on WSL 2.

---

## 🛠️ System Architecture & Tech Stack

* **Language:** Python 3.11+
* **Machine Learning:** PyTorch, Hugging Face Transformers
* **Backend Framework:** FastAPI, Uvicorn, Pydantic
* **Frontend UI:** Streamlit
* **DevOps & Containerization:** Docker, Docker Compose, WSL 2
* **Version Control:** Git, GitHub

---

## 📦 Quickstart with Docker

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bobby6783/content-moderation-api.git https://github.com/Bobby6783/content-moderation-api.git
   cd content-moderation-api
