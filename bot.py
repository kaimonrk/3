from telegram import Update
from telegram.ext import Updater, CommandHandler

def start(update: Update, context):
    update.message.reply_text("🔒 Security Helper Bot\nCommands:\n/start - Show help\n/scan <IP> - Check host")

def scan(update: Update, context):
    target = context.args[0] if context.args else None
    if not target:
        update.message.reply_text("⚠ Usage: /scan <IP>")
        return
    update.message.reply_text(f"🛡️ Scanning {target} (legal use only)...")
    import os
    result = os.popen(f"ping -c 4 {target}").read()
    update.message.reply_text(f"📡 Ping Results:\n{result}")

updater = Updater("8029133503:AAFvsd5OKAmmwQlEr0lIdFsD8T4X0STPYG4")  # Replace with your bot token
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("scan", scan))
updater.start_polling()
print("Bot is running...")

def nmap_scan(update: Update, context):
    target = context.args[0] if context.args else None
    if not target:
        update.message.reply_text("⚠ Usage: /nmap <IP>")
        return
    update.message.reply_text(f"🔍 Running nmap on {target}...")
    result = os.popen(f"nmap -sV {target}").read()
    update.message.reply_text(f"📡 Nmap Results:\n{result}")

updater.dispatcher.add_handler(CommandHandler("nmap", nmap_scan))