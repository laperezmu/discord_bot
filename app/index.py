import discord
import datetime
from urllib import parse, request
import re
from discord.ext import commands

bot = commands.Bot(command_prefix='#', description='This is a tuttifruti bot')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
   await ctx.send(numOne + numTwo)

@bot.command()
async def ping(ctx):
   await ctx.send('pong')


@bot.command()
async def stats(ctx):
   embed = discord.Embed(title=f"{ctx.guild.name}", description = "AresBot", timestamp = datetime.datetime.utcnow(), color = discord.Color.blue())
   embed.add_field(name="Server created at", value = f"{ctx.guild.created_at}")
   embed.add_field(name="Server owner", value = f"{ctx.guild.owner}")
   embed.add_field(name ="Server region", value = f"{ctx.guild.region}")
   embed.add_field(name = "Server ID", value = f"{ctx.guild.id}")
   embed.set_thumbnail(url='https://placekitten.com/408/287')
   await ctx.send(embed=embed)


@bot.command()
async def play(ctx, *, search):
   query_string = parse.urlencode({'search_query': search})
   url_wanted = 'https://www.youtube.com/results?'+query_string
   html_content = request.urlopen(url=url_wanted)
   search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
   await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


#Events
@bot.event
async def on_ready():
    print('My bot is ready')



bot.run('ODgwOTg3MzQxNjg5MzQ0MDcx.YSmRZg.Q1vJyVXFe5Z3FoEPoAb3hf2cj9Y')