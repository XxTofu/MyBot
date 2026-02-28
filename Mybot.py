import discord
from discord.ext import commands
from datetime import datetime, timedelta
import random

description = '''Simple bot'''

token = input('Token: ')

intents= discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!',description=description,intents=intents, help_command=None)


@bot.event
async def on_ready():
    assert bot.user is not None
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('----------')


@bot.event#welcome message to the server and give a role to the new member
async def on_member_join(member):
        channel=bot.get_channel('channel id')
        role = member.guild.get_role('role id')
        to_send = f'Welcome {member.mention} to Rays`s restaurant hope you enjoy!'
        await channel.send(to_send)
        await member.add_roles(role)


@bot.command()
async def git(ctx):
    await ctx.send('Here`s my owner profile on github: https://github.com/XxTofu')


@bot.command()#show the time? Not relevant code user can look at the time without this
async def time(ctx):
    time=datetime.now()
    d = time + timedelta(days=0)
    await ctx.send(discord.utils.format_dt(d))


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
    role = ctx.guild.get_role('role id')
    role1 = ctx.guild.get_role('role id')
    if role or role1 in ctx.author.roles:
        for i in range(times):
            await ctx.channel.purge(limit = times +1)
            break
    else:
        await ctx.send('Sorry can`t do')


@bot.command()#ban a user
async def ban(ctx, member:discord.Member, reason=None):
    role = member.guild.get_role('role id')
    role1 = member.guild.get_role('role id')
    if role or role1 in ctx.author.roles:
        await member.ban(reason=reason)


@bot.command()#kick a user
async def kick(ctx, member:discord.Member, reason = None):
    role = member.guild.get_role('role id')
    role1 = member.guild.get_role('role id')
    if role or role1 in ctx.author.roles:
        await member.kick(reason=reason)
        await ctx.send(f'{member} was kicked by {ctx.author}: {reason}')
        

@bot.command()#simple ship command, doesnt have any image 
async def ship(ctx, member1: discord.Member, member2 : discord.Member):
    percent = random.randint(1, 100)
    name1 = str(member1.display_name)
    name2 = str(member2.display_name)
    name1 = name1.capitalize()
    name2 = name2.capitalize()  
    if len(name1) >= 3 and len(name2) >= 3:
        shipname = name1[:3] + name2[-2:]
    elif len(name1) >= 3 and len(name2) < 3:
        shipname = name1[:3] + name2[-1:]
    elif len(name1) < 3 and len(name2) >= 3:
        shipname = name1[:1] + name2[-2:] 
    else:
        shipname = name1[:1] + name2[-1:]
     
    await ctx.send(f'Ship Name: {shipname}')
    await ctx.send(f'{member1} has a {percent}% compatibility with {member2}')


@bot.command()#send the users icon to the channel
async def rob(ctx, member: discord.Member):
    if member.display_avatar == member.default_avatar:
        await ctx.send(f'Default Discord avatar...')
    else:
        await ctx.send(f'Here is the icon: {member.display_avatar}')
    

@bot.listen()#block the words you want
async def on_message(message):
     msg_content = message.content.lower()
     bignono = ['list of blocked words']
     if any(word in msg_content for word in bignono):
          await message.delete()


@bot.event#it will send every single message a user has deleted to the channel you choose
async def on_message_delete(message):
    channel=bot.get_channel('channel id')
    ctx = f'{message.author} has deleted {message.content}'
    await  channel.send(ctx)


bot.run(token)

