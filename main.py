from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import random

BOT_TOKEN = "8221867831:AAGUULzOPowvPpkGNRQpEylmmcTIjvbtcuE"

# Load words from file
def load_words():
    words = []
    with open("words.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                word, hint = line.strip().split("|", 1)
                words.append((word.lower(), hint))
    return words

WORDS = load_words()

# Game state: {chat_id: {...}}
games = {}

async def startgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    host_id = update.effective_user.id

    if games.get(chat_id, {}).get("in_progress"):
        await update.message.reply_text("⚠ A game is already running!")
        return

    games[chat_id] = {"host_id": host_id, "in_progress": True, "round": 0}
    await update.message.reply_text(f"🎮 Game started by {update.effective_user.mention_html()}!", parse_mode="HTML")
    await start_round(chat_id, context)

async def start_round(chat_id, context):
    game = games.get(chat_id)
    if not game or not game["in_progress"]:
        return

    word, hint = random.choice(WORDS)
    game["word"] = word
    game["hint"] = hint
    game["round"] += 1

    keyboard = [[InlineKeyboardButton("👀 See Word", callback_data="see_word")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id,
        f"🔵 Round {game['round']} Started!\nClick the button to see the word (only host).",
        reply_markup=reply_markup
    )

async def see_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    game = games.get(chat_id)

    if not game or not game.get("in_progress"):
        await query.answer("❌ No game running!", show_alert=True)
        return

    if user_id != game["host_id"]:
        await query.answer("⚠ Only the host can see the word!", show_alert=True)
        return

    await query.message.reply_text(f"🎯 WORD: {game['word']}\n💡 HINT: {game['hint']}")

async def hint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    game = games.get(chat_id)

    if not game or not game.get("in_progress"):
        await update.message.reply_text("❌ No game running!")
        return

    if user_id != game["host_id"]:
        await update.message.reply_text("⚠ Only the host can give a hint!")
        return

    await update.message.reply_text(f"💡 HINT: {game['hint']}")

async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = games.get(chat_id)

    if not game or not game.get("in_progress"):
        return

    guess = update.message.text.strip().lower()
    if guess == game["word"]:
        await update.message.reply_text(
            f"🏆 {update.effective_user.mention_html()} guessed it right!\n🎯 Word: {game['word']}",
            parse_mode="HTML"
        )
        await start_round(chat_id, context)

async def stopgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in games:
        games.pop(chat_id)
        await update.message.reply_text("🛑 Game stopped!")
    else:
        await update.message.reply_text("❌ No game running!")

# Bot setup
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("startgame", startgame))
app.add_handler(CommandHandler("hint", hint))
app.add_handler(CommandHandler("stopgame", stopgame))
app.add_handler(CallbackQueryHandler(see_word, pattern="^see_word$"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess))

print("🤖 Bot is running...")
app.run_polling()
