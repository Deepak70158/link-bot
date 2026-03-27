import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8324977619:AAFkDY6Ynwep4tpfhI0ygUZEA8EuKzVcSUc"
SHRINKME_API = "e0c9c424fa96ac23ade071ff99682bdb95450eff"

def shorten_link(url):
    api_url = f"https://shrinkme.io/api?api={SHRINKME_API}&url={url}"
    response = requests.get(api_url)
    data = response.json()
    return data.get("shortenedUrl", url)

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("http"):
        short = shorten_link(text)
        await update.message.reply_text(f"✅ Shortened Link:\n{short}")
    else:
        await update.message.reply_text("❌ Bhai HTTP link bhejo!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()
