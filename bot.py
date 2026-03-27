import requests
from telegram.ext import Updater, MessageHandler, Filters

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

def handle_link(update, context):
    text = update.message.text.strip()
    if text.startswith("http"):
        update.message.reply_text("⏳ Link short ho raha hai...")
        short = shorten_link(text)
        update.message.reply_text(f"✅ Shortened Link:\n{short}")
    else:
        update.message.reply_text("❌ HTTP link bhejo!")

updater = Updater(BOT_TOKEN)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_link))
updater.start_polling()
updater.idle()
