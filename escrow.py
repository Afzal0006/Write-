from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8414351117:AAEDEkc1VblJ8NU8Umle1gby1KyY94Gd1x4"
USERBOT_ID = 6999999999

async def create_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(USERBOT_ID, "/create", reply_to_message_id=update.message.message_id)
    await update.message.reply_text("⏳ Creating group... please wait.")

async def receive_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id == USERBOT_ID:
        await context.bot.send_message(update.effective_chat.id, f"✅ Group Created: {update.message.text}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("create", create_group))
app.add_handler(MessageHandler(filters.TEXT & filters.Chat(USERBOT_ID), receive_link))
app.run_polling()
