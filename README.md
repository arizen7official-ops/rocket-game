# Rocket MiniApp — Full package

This package contains 3 parts:
- `webapp/` — the HTML/JS mini-app. Deploy this to GitHub Pages.
- `server/` — FastAPI server that accepts withdraw requests and sends them to your Telegram.
- `bot/` — simple Aiogram bot that can show a WebApp button.

## 1) Publish webapp to GitHub Pages
1. Create a new GitHub repository (e.g. `rocket-miniapp`).
2. Push the `webapp/` folder contents to the repository root (index.html).
3. In GitHub repo settings → Pages → choose branch `main` and folder `/ (root)` — enable. 
4. After a minute your site will be available at:
   `https://<your-github-username>.github.io/<repo>/index.html`
5. Edit `bot/bot.py` and replace `WEBAPP_URL` with that URL.

## 2) Run the server (FastAPI)
The server accepts POST /send with JSON body:
```
{ "user_id": ..., "username": "...", "coins": 123, "address": "EQ..." }
```

Install and run:
```
cd server
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Expose this server on the internet (Render, Railway, Fly, or VPS).
Take the server URL `https://your-server.com/send` — you'll add it to the webapp (see next).

## 3) Connect webapp -> server
Open `webapp/index.html` and in the `sendReq` button area you can add a `fetch` to your server URL.
Example (already included in the HTML comments):
```
fetch("https://your-server.com/send", { method: "POST", headers: {"Content-Type":"application/json"}, body: JSON.stringify({
  user_id: window.Telegram.WebApp?.initDataUnsafe?.user?.id || 0,
  username: window.Telegram.WebApp?.initDataUnsafe?.user?.username || "unknown",
  coins: coins, address: addr
})});
```

Note: GitHub Pages is a static host — the fetch will work only if your server supports CORS (server allows requests from the webapp origin).

## 4) Run the bot
```
cd bot
pip install -r requirements.txt
python bot.py
```
Start the bot and send `/start` to it — it will show a button that opens the MiniApp (after you update WEBAPP_URL).

## Security note
Your bot token is included in `server/config.py` and `bot/bot.py` for convenience. Do **not** push tokens to public repos. Replace tokens with environment variables for production.

---
If you want, I can update `webapp/index.html` to automatically POST to server URL and include Telegram init data — tell me the server URL and I will wire it and rebuild the ZIP.
