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


@bot.event
async def on_member_join(member):
        channel=bot.get_channel(channel id)
        role = member.guild.get_role(role id to give)
        to_send = f'Welcome {member.mention} to Rays`s restaurant hope you enjoy!'
        await channel.send(to_send)
        await member.add_roles(role)

@bot.command()
async def time(message):
    time=datetime.now()
    d = time + timedelta(days=0)
    await message.send(discord.utils.format_dt(d))


@bot.command()
async def joined(ctx, member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def nuke(ctx, times:int, content='repeat', limit = 21):
     if times >= limit:
          await ctx.send('To much! Can`t pass 20')
     else:
        for i in range(times):
          await ctx.send(content)


@bot.command()
async def clear(ctx, times:int):
    role = ctx.guild.get_role(role id here)
    role1 = ctx.guild.get_role(role id here)
    if role or role1 in ctx.author.roles:
        for i in range(times):
            await ctx.channel.purge(limit = times +1)
            break
    else:
        await ctx.send('Sorry can`t do')


@bot.command()
async def ship(ctx, member1: discord.Member, member2 : discord.Member ):
    percent = random.randint(1, 100)    
    await ctx.send(f'{member1} has a {percent}% compatibility with {member2}')


@bot.listen()
async def on_message(message):
     msg_content = message.content.lower()
     bignono = ['Pau','Dick','Penis','Bitch','pau','dick','penis','bitch']
     if any(word in msg_content for word in bignono):
          await message.delete()

#snipe tool it will send message whenever a member deletes one
@bot.event
async def on_message_delete(message):
    channel=bot.get_channel(channel id here )
    ctx = f'{message.author} has deleted {message.content}'
    await  channel.send(ctx)


bot.run(token)
