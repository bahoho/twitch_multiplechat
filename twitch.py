from twitchio.ext import commands
import socket
import twitch


bot = commands.Bot(
    irc_token='oauth:14**3tjpg****j', #your irc token
    api_token='oauth:1uo***qxlf*******', #your api token
    nick='here', #your bot name
    prefix='!',
    initial_channels=['#xqcow', '#hasanabi'] #you can add multiple channels
)

@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')


@bot.event
async def event_message(ctx):
    print(f'{ctx.author.name}:{ctx.content}')
    
    await bot.handle_commands(ctx)

bot.run()
