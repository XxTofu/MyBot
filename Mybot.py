import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random

description = '''Simple bot'''

token = input('Token: ')

intents= discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/',description=description,intents=intents)


@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('----------')


@bot.event#welcome message to the server
async def on_member_join(member):
        channel=bot.get_channel(channel id here)
        role = member.guild.get_role(channel id here)
        to_send = f'Welcome {member.mention} to the server hope you enjoy!'
        await channel.send(to_send)
        await member.add_roles(role)



@bot.command()
async def git(ctx):
    await ctx.send('Here`s my owner profile on github: https://github.com/XxTofu')


@bot.command()#show the time? Not relevant code user can look at the time without this
async def time(message):
    time=datetime.now()
    d = time + timedelta(days=0)
    await message.send(discord.utils.format_dt(d))


@bot.command()#tell when a member joined the server
async def joined(ctx, member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()#repeat the message the user want by the amout of time he choose, can't pass 20
async def nuke(ctx, times:int, content='repeat', limit = 21):
     if times >= limit:
          await ctx.send('To much! Can`t pass 20')
     else:
        for i in range(times):
          await ctx.send(content)


@bot.command()#clear the number of messages the user as asked on the channel
async def clear(ctx, times:int):
    role = ctx.guild.get_role(role id here)
    role1 = ctx.guild.get_role(other role id here)
    if role or role1 in ctx.author.roles:
        for i in range(times):
            await ctx.channel.purge(limit = times +1)
            break
    else:
        await ctx.send('Sorry can`t do')


@bot.command() #simple ship command, doesnt have any image 
async def ship(ctx, member1: discord.Member, member2 : discord.Member ):
    percent = random.randint(1, 100)    
    await ctx.send(f'{member1} has a {percent}% compatibility with {member2}')


@bot.listen()#block the words you want
async def on_message(message):
     msg_content = message.content.lower()
     bignono = [list of bad words]
     if any(word in msg_content for word in bignono):
          await message.delete()




@bot.event #it will send every single message a user has deleted to the channel you choose
async def on_message_delete(message):
    channel=bot.get_channel(channel id here)
    ctx = f'{message.author} has deleted {message.content}'
    await  channel.send(ctx)


bot.run(token)
