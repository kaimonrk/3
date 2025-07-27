from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔒 Security Helper Bot\nCommands:\n/start - Show help\n/scan <IP> - Check host")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    target = context.args[0] if context.args else None
    if not target:
        await update.message.reply_text("⚠ Usage: /scan <IP>")
        return
    await update.message.reply_text(f"🛡️ Scanning {target} (legal use only)...")
    import os
    result = os.popen(f"ping -c 4 {target}").read()
    await update.message.reply_text(f"📡 Ping Results:\n{result}")

def main():
    application = Application.builder().token("YOUR_BOT_TOKEN").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("scan", scan))
    
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
