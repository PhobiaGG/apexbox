import discord
from discord.ext import commands
import os

# Render will provide this safely through Environment Variables
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'ApexBox Bot is now LIVE on Render and listening...')

@bot.command()
async def verify(ctx):
    if ctx.channel.name == "verify-here":
        member_role = discord.utils.get(ctx.guild.roles, name="Member")
        if member_role:
            await ctx.author.add_roles(member_role)
            await ctx.send(f"✅ {ctx.author.mention}, you have been verified! Welcome to the ApexBox Community.", delete_after=10)
            try:
                await ctx.message.delete()
            except:
                pass

if __name__ == "__main__":
    bot.run(TOKEN)
