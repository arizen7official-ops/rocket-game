from fastapi import FastAPI, Request
import requests
from config import BOT_TOKEN, ADMIN_ID

app = FastAPI()

@app.post("/send")
async def send(req: Request):
    data = await req.json()
    user_id = data.get("user_id", "unknown")
    username = data.get("username", "unknown")
    coins = data.get("coins", 0)
    addr = data.get("address", "")
    text = (
        f"🔥 Новая заявка\n\n"
        f"👤 Пользователь: @{username}\n"
        f"🆔 ID: {user_id}\n"
        f"💰 Монет: {coins}\n"
        f"🏦 Адрес: {addr}\n"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={ "chat_id": ADMIN_ID, "text": text })
    return {"ok": True, "tg_status": resp.status_code}
