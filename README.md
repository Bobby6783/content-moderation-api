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
   \`\`\`bash
   git clone https://github.com/Bobby6783/content-moderation-api.git
   cd content-moderation-api
   \`\`\`

2. **Launch services:**
   \`\`\`bash
   docker compose up --build
   \`\`\`

3. **Access endpoints:**
   * **Streamlit UI:** `http://localhost:8501`
   * **FastAPI Docs:** `http://localhost:8000/docs`

---

## 📊 API Usage Example

**Endpoint:** `POST /v1/moderate-text`

**Sample Request:**
\`\`\`json
{
  "text": "Cybercriminals attempt to attack system infrastructure."
}
\`\`\`

**Sample Response:**
\`\`\`json
{
  "text": "Cybercriminals attempt to attack system infrastructure.",
  "flagged": false,
  "confidence_score": 0.042,
  "categories": {
    "toxic": 0.042,
    "severe_toxic": 0.001,
    "obscene": 0.003,
    "threat": 0.008,
    "insult": 0.005,
    "identity_hate": 0.002
  },
  "latency_ms": 118.4
}
\`\`\`
"@

