import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = 're! ')
client.remove_command('help')


#----------------Comandos Básicos---------------#


@client.event
async def on_ready():
    print('Bot is ready')

#@client.event
#async def on_member_join(member):
#    await ctx.send(f'{member} se ha unido al servidor')

#@client.event
#async def on_member_remove(member):
#    await ctx.send(f'{member} ha dejado el servidor')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(aliases=['bola8'])
async def _8ball(ctx, *, question):
    responses = ['Puede ser.', 'Asegurado.', 'Jamás', 'Si', 'No']
    await ctx.send(f'Pregunta: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['Hola', 'hola'])
async def saludos(ctx):
    await ctx.send('Hola!, list@ para que te recomiende juegos?')


#------------------------Comandos personalizados-----------------------------#

@client.command(aliases=['help', 'Help'])
async def cmmdhelp(ctx):
    await ctx.send('¡¡¡Hola!!!, yo soy **Recomendín**, y soy un bot para recomendarte juegos (recuerda que mi prefijo es **re!**.\n\nComandos:\n-Usa **help** para mostrar este mensaje\n-Usa **ping** para medir tu latencia\n-Usa **bola8** para que te adivine el futuro sobre tu pregunta(ejemplo: re! bola8 Tendré suerte hoy?)\n-Usa **hola** para que te de una calurosa bienvenida\n\nComandos de recomendación:\n**-Usa mi prefijo más la categoría de juegos que desees para obtener mi recomendación.**\nCategorías: **shooters, rpgs/jrpgs, juegos de plataformas, juegos estilo metroidvania y juegos de estrategia.**\n\n**Recuerda que si quieres añadir una categoría o un juego no dudes en dejarlo en el canal #juegos-recomendados.** ¡Disfuta tu estancia en el server!')

@client.command(aliases=['shooters', 'Shooters'])
async def rec_shooters(ctx):
    await ctx.send('Los **shooters** que te recomiendo son: Valorant, GTA, Fortnite y Apex')

@client.command(aliases=['rpg', 'Rpg', 'RPG'])
async def rec_rpg(ctx):
    await ctx.send('Los **rpgs o jrpgs** que te recomiendo son: The Legend of Zelda, Final Fantasy, Pokemon, Xenoblade Chronicles y Tales of')

@client.command(aliases=['Plataformas', 'plataformas'])
async def rec_platformers(ctx):
    await ctx.send('Los juegos de **plataformas** que te recomiendo son: Hollow Knight, Metroid, Super Mario y Shantae')

@client.command(aliases=['Metroidvania', 'metroidvania'])
async def rec_metroidvania(ctx):
    await ctx.send('Los juegos **metroidvania** que te recomiendo son: Metroid, Castlevania, Hollow Knight e Iconoclasts')

@client.command(aliases=['estrategia', 'Estrategia'])
async def rec_estrategia(ctx):
    await ctx.send('Los juegos de **estrategia** que te recomiendo son: Fire Emblem, Luminous arc, Plants vs Zombies y Lock\'s Quest')

client.run('NzI3MjgwMTgyOTYwMDYyNDc0.Xvr7Bw.ZrEZhYkQTtIypBagMXimkhlFisg')