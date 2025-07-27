import telebot

TOKEN = "8232316700:AAG94DJ_8B2lWy14qlelwoqH3MnvaoQ8bfs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "سلام! 🎬 خوش اومدی به استودیو فیلم.")

bot.infinity_polling()
