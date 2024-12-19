import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def ecotips(ctx):
    tips = [
        "Reduce el consumo de plástico utilizando bolsas reutilizables.",
        "Ahorra agua cerrando el grifo mientras te cepillas los dientes.",
        "Opta por productos ecológicos o hechos con materiales reciclados.",
        "Recicla correctamente: separa los residuos en casa.",
        "Apaga las luces y desconecta los aparatos electrónicos cuando no los uses."
    ]
    tip = random.choice(tips)

    # Opciones de título y color para el embed
    opciones_embed = [
        {"titulo": "🌱 Consejo Ecológico 🌱", "color": 0x34A853},
        {"titulo": "♻️ Práctica Sostenible", "color": 0x00C853},
        {"titulo": "Ecomantra 🌍", "color": 0x1B5E20},
        {"titulo": "Eco-Tip del Día 🌞", "color": 0xFFCC00},
        {"titulo": "Chiste Verde 🌿", "color": 0x76FF03}
    ]

    # Selecciona aleatoriamente una opción
    opcion_seleccionada = random.choice(opciones_embed)

    # Crear el embed usando la opción seleccionada
    embed = discord.Embed(
        title=opcion_seleccionada["titulo"],
        description=tip,
        color=opcion_seleccionada["color"]
    )
    await ctx.send(embed=embed)

@bot.command()
async def chistes(ctx):
    jokes = [
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué las focas miran siempre hacia arriba? ¡Porque ahí están los focos!",
        "¿Cuál es el colmo de Aladdín? Tener mal genio.",
        "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
        "¿Cómo se dice pañuelo en japonés? Saka-moko."
    ]
    joke = random.choice(jokes)
    await ctx.send(joke)

# Iniciar el bot (asegúrate de usar tu propio token)
bot.run("MTI5NDA5MTc1NDkwNzM3MzY0OQ.GAzYdF.LHnE9lOc-4zlyyvLhtxa9gJbxRi6NnRPInTaFM")

