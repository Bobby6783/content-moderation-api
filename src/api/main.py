from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time

app = FastAPI(
    title="Multimodal Content Moderation API",
    version="1.0.0"
)

# Baseline moderation keywords (Replace with ONNX fine-tuned model later)
TOXIC_KEYWORDS = ["hate", "abuse", "harm", "threat", "badword"]

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Content Moderation Engine active."}

@app.post("/v1/moderate-text")
def moderate_text(payload: TextRequest):
    start_time = time.time()
    
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
        
    text_lower = payload.text.lower()
    flagged = any(word in text_lower for word in TOXIC_KEYWORDS)
    score = 0.88 if flagged else 0.02
    
    latency = round((time.time() - start_time) * 1000, 2)
    
    return {
        "text": payload.text,
        "flagged": flagged,
        "confidence_score": score,
        "category": "toxicity" if flagged else "safe",
        "latency_ms": latency
    }