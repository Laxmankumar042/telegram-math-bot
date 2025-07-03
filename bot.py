from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m a Math Bot.\nSend me any mathematical expression and I’ll calculate it!\nExamples:\n2+3\n(4*5)-3\n10/2")

# Define the handler for mathematical expressions
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    expression = update.message.text
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, {})
        await update.message.reply_text(f"✅ Result: {result}")
    except Exception as e:
        await update.message.reply_text("❌ Invalid Expression! Please try again with valid math input.")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'os.environ[8052792980:AAGRDnyxSplbDRLAY-MwqSQbtMq33A8NSFs]'

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
