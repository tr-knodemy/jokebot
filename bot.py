import random
import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

banned_words = ["badword1", "badword2", "badword3"]  

dad_jokes = [
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "I used to hate facial hair... but then it grew on me.",
    "Why did the math book look sad? Because it had too many problems.",
    "I only know 25 letters of the alphabet. I don’t know y.",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere."
]


roasts = [
    "I'd agree with you, but then we'd both be wrong.",
    "You're not stupid, you just have bad luck thinking.",
    "You bring everyone so much joy... when you leave.",
    "I'd explain it to you, but I left my crayons at home.",
    "You're like a cloud—when you disappear, it's a beautiful day."
]


puns = [
    "I used to be a baker, but I couldn't make enough dough.",
    "I’m on a seafood diet. I see food and I eat it.",
    "I would tell you a joke about construction, but I’m still working on it.",
    "I wondered why the ball was getting bigger… then it hit me.",
    "I used to play piano by ear, now I use my hands."
]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  
    if channel:
        await channel.send(f" Welcome to the server, {member.mention}!")

# Safety filter
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for word in banned_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(
                f" {message.author.mention}, please keep it clean!"
            )
            return

    await bot.process_commands(message)

# -------------------------
# Commands
# -------------------------

# Dad joke command
@bot.command(name="dadjoke")
async def dadjoke(ctx):
    embed = discord.Embed(title="👨 Dad Joke", color=discord.Color.orange())
    embed.add_field(name="Here you go:", value=random.choice(dad_jokes), inline=False)
    await ctx.send(embed=embed)

# Roast command
@bot.command(name="roast")
async def roast(ctx, member: discord.Member = None):
    target = member.mention if member else ctx.author.mention
    embed = discord.Embed(title="🔥 Roast", color=discord.Color.red())
    embed.add_field(name=f"{target}", value=random.choice(roasts), inline=False)
    await ctx.send(embed=embed)

# Pun command
@bot.command(name="pun")
async def pun(ctx):
    embed = discord.Embed(title="😄 Pun", color=discord.Color.green())
    embed.add_field(name="Enjoy:", value=random.choice(puns), inline=False)
    await ctx.send(embed=embed)

# Help command (4th command)
@bot.command(name="helpme")
async def helpme(ctx):
    embed = discord.Embed(title="🤖 JokeBot Commands", color=discord.Color.blue())
    embed.add_field(name="!dadjoke", value="Get a random dad joke", inline=False)
    embed.add_field(name="!roast [@user]", value="Roast yourself or a friend", inline=False)
    embed.add_field(name="!pun", value="Get a random pun", inline=False)
    embed.add_field(name="!helpme", value="Show this command list", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)

