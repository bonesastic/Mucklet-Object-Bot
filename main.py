from Mucklet import Bot, ResClient
from Mucklet.CachedDictionary import CachedDictionary

client = ResClient("wss://api.wolfery.com", "https://wolfery.com")

bot = Bot("BLZAH6CTXZZKTEF5KNUABULPFU2G6QPH", client)

Objects = CachedDictionary("Local Objects Storage")

# object params:
#   name: string
#   description: string
#   **kwargs: any

@bot.on("message")
def on_command(message):
    context = message.event.message.strip().lower().split(" ")
    if context[0] == "ping":
        bot.say("pong")
    else:
        bot.say("I don't know what you mean by that.")


bot.boot()
