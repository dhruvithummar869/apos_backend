# 1. Imports
from fastapi import FastAPI
from app.api.routes import chat  # हमने अपनी chat.py फ़ाइल को यहाँ इम्पोर्ट किया

# 2. App Initialization (मुख्य ऐप बनाना)
app = FastAPI(
    title="AI Personal Operating System (APOS)",
    description="Production-level AI OS Backend",
    version="1.0.0"
)

# 3. Include Routers (राउटर को जोड़ना)
# हम अपने सारे चैट वाले रास्तों को मुख्य ऐप में शामिल कर रहे हैं
app.include_router(chat.router, prefix="/api/v1/chat", tags=["AI Chat"])

# 4. Root Endpoint (चेक करने के लिए कि सर्वर चल रहा है या नहीं)
@app.get("/")
def read_root():
    return {"message": "Welcome to APOS Backend is running successfully!"}