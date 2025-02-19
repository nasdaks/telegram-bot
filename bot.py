from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Il tuo token - sarà configurato su Render
TOKEN = os.environ.get('BOT_TOKEN', '7594091724:AAHW7cKcBEHThjThTQYon2sXW8tt0wIc2yM')
# ID del tuo canale
CHANNEL_ID = os.environ.get('CHANNEL_ID', '1001845907230')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Funzione che gestisce il comando /start"""
    keyboard = [
        [InlineKeyboardButton("Unisciti al Canale", url=f"https://t.me/+{CHANNEL_ID}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Benvenuto! Clicca qui sotto per unirti al canale:",
        reply_markup=reply_markup
    )

def main():
    # Crea l'applicazione
    app = Application.builder().token(TOKEN).build()

    # Aggiungi il gestore per il comando /start
    app.add_handler(CommandHandler("start", start))

    # Avvia il bot
    print("Bot avviato! Premi Ctrl+C per terminare.")
    app.run_polling()

if __name__ == "__main__":
    main()
