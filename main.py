import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7607621887:AAHVpaKwitszMY9vfU2-s0n60QNL56rdbM0"
DATA_FILE = "message_counts.json"

# Load data from file
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Track every message in groups
async def track_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    data = load_data()
    chat_id = str(update.message.chat.id)
    user_id = str(update.message.from_user.id)
    name = update.message.from_user.first_name

    if chat_id not in data:
        data[chat_id] = {}

    if user_id not in data[chat_id]:
        data[chat_id][user_id] = {"name": name, "count": 0}

    data[chat_id][user_id]["count"] += 1
    save_data(data)

# /rankings command
async def rankings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /rankings {count}")
        return

    try:
        count = int(context.args[0])
    except ValueError:
        await update.message.reply_text("Count must be a number!")
        return

    chat_id = str(update.message.chat.id)
    data = load_data()

    if chat_id not in data or not data[chat_id]:
        await update.message.reply_text("No data available for this group yet.")
        return

    sorted_users = sorted(data[chat_id].items(), key=lambda x: x[1]["count"], reverse=True)
    total_messages = sum(u["count"] for _, u in sorted_users)

    text = f"🏆 **Top {count} Active Members** 🏆\n\n"
    for i, (uid, info) in enumerate(sorted_users[:count], start=1):
        text += f"{i}. {info['name']} — {info['count']} messages\n"

    text += f"\n📊 **Total messages in group:** {total_messages}"
    await update.message.reply_text(text, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & filters.GROUPS, track_messages))
    app.add_handler(CommandHandler("rankings", rankings))

    app.run_polling()

if __name__ == "__main__":
    main()
