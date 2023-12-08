import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url =file.url
            await file.save(f'./{file.filename}')
            hasil = get_class(model_path="keras_model.h5",labels_path="labels.txt",image_path=f'./{file.filename}')

            if hasil[0] == 'makanan tidak sehat\n' and hasil[1] >= 0.7:
                await ctx.send("makanan ini tidak sehat" )
                await ctx.send("tidak sehat bagi tubuh ")
                await ctx.send("tidak boleh sering makan ini,tidak sehat ")
            elif hasil[0] == 'makanan sehat\n' and hasil[1] >= 0.7:
                await ctx.send("makanan ini sehat" )
                await ctx.send(" sehat bagi tubuh ")
                await ctx.send("makanan ini dapat sangat berguna bagi tubuh ")


    else:
        await ctx.send("gambar tidak valid")


        
bot.run("MTExOTIxMDAzODkwOTc1MTMzNw.GAwtaE.JCANn7mViUw5IH4HiNlCB9IHJa6T-QBR1wRiiY")