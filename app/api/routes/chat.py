# 1. Imports (जरूरी चीजें मंगाना)
from fastapi import APIRouter
import requests

# 2. Router Initialization (राउटर बनाना)
router = APIRouter()

# 3. API Endpoint (रास्ता तय करना)
@router.post("/prompt")
def ask_ai(user_prompt: str):
    """
    यह फंक्शन यूजर से एक सवाल (prompt) लेगा और उसे Ollama LLM के पास भेजेगा।
    """
    # Ollama का लोकल URL जहाँ Llama मॉडल चल रहा है
    ollama_url = "http://localhost:11434/api/generate"
    
    # Ollama को भेजने के लिए डेटा (Payload) तैयार करना
    payload = {
        "model": "llama3.2:latest",  # या जो भी मॉडल तुमने डाउनलोड किया है (जैसे llama3.2, mistral)
        "prompt": user_prompt,
        "stream": False # अभी हम बिना स्ट्रीम के सिंपल रिस्पॉन्स ले रहे हैं
    }
    
    # Ollama को Request भेजना
    response = requests.post(ollama_url, json=payload)
    
    # Response में से सिर्फ टेक्स्ट डेटा निकालना
    result = response.json()
    
    # क्लाइंट (Swagger UI) को जवाब वापस भेजना
    return {"status": "success", "ai_response": result.get("response")}