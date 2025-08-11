from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7607621887:AAHVpaKwitszMY9vfU2-s0n60QNL56rdbM0"
USERBOT_ID = 7278904232

async def create_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.forward(USERBOT_ID)
    await update.message.reply_text("📨 Request sent to userbot, please wait...")

async def link_receiver(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        original = update.message.reply_to_message
        if original.forward_from and original.forward_from.id == USERBOT_ID:
            await original.reply_text(f"✅ Group Created: {update.message.text}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("create", create_cmd))
app.add_handler(CommandHandler("", link_receiver))
app.run_polling()
