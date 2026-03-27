import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8324977619:AAFkDY6Ynwep4tpfhI0ygUZEA8EuKzVcSUc"
SHRINKME_API = "e0c9c424fa96ac23ade071ff99682bdb95450eff"

def shorten_link(url):
    try:
        api_url = f"https://shrinkme.io/api?api={SHRINKME_API}&url={url}&format=text"
        response = requests.get(api_url, timeout=10)
        result = response.text.strip()
        if result.startswith("http"):
            return result
        else:
            return f"API Error: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith("http"):
        await update.message.reply_text("⏳ Link short ho raha hai...")
        short = shorten_link(text)
        await update.message.reply_text(f"✅ Shortened Link:\n{short}")
    else:
        await update.message.reply_text("❌ HTTP link bhejo!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()
