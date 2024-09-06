import discord
from discord.ext import commands
import random
import requests
import wikipediaapi

intents = discord.Intents.default()
intents.message_content = True
intents.members= True
bot = commands.Bot(command_prefix='!', intents=intents)



#----------INICIO CLIMA----------

OWM_API_KEY = "22307f5b30073b825bd4e4298ef13655"

@bot.command()
async def clima(ctx, *, lugar: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={lugar},AR&appid={OWM_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperatura = data['main']['temp']
        descripcion = data['weather'][0]['description']
        await ctx.send(f"El clima en {lugar} es {descripcion} con una temperatura de {temperatura}°C.")
    else:
        await ctx.send(f"No se pudo obtener el clima para {lugar}.")
#----------FIN CLIMA----------

#---------INICIO MENSAJE AUTOMATICO DE COMANDOS------
CHANNEL_ID = 632400399210512395
INTERVAL = 21600

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_message.start()

@tasks.loop(seconds=INTERVAL)
async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(comandos_bot)

#--------FIN MSJ AUTOMATICO DE COMANDOS--------


#----------INICIO RIFA----------

premios = [
    '¡Felicidades! Ganaste un manual de instrucciones ilegible. 📜',
    '¡Enhorabuena! Ahora posees un paracaídas de segunda mano. 🪂',
    '¡Te ganaste una pelota cuadrada para jugar fútbol! ⬛️⚽️',
    '¡Felicitaciones! Has recibido un abanico sin aspas. 🌀',
    '¡Aquí tienes un sombrero que no te queda! 🎩',
    '¡Has ganado un mapa del tesoro sin indicaciones! 🗺️',
    '¡Te llevas un diccionario sin verbos! 📖',
    '¡Felicidades! Ahora tienes un cuadro en blanco. 🖼️',
    '¡Te ganaste un par de calcetines desparejados! 🧦🧦'
]


def rifa_random():
    return random.choice(premios)


@bot.command()
async def rifa(ctx):
    premios = rifa_random()
    await ctx.send(premios)

#----------FIN RIFA----------


#----------UNIRSE Y SALIR DEL SERVIDOR----------

# Evento cuando un miembro se une al servidor
@bot.event
async def on_member_join(member):
    # Especificar el canal 'canal' para el mensaje de bienvenida
    channel = discord.utils.get(member.guild.text_channels, name='canal')
    if channel:
        await channel.send(f'¡Bienvenido al servidor, {member.mention}! 🎉')
        print(f'Welcome message sent to {member.name}')
    else:
        print('Channel canal not found')

# Evento cuando un miembro se va del servidor
@bot.event
async def on_member_remove(member):
    # Especificar el canal 'canal' para el mensaje de despedida
    channel = discord.utils.get(member.guild.text_channels, name='canal')
    if channel:
        await channel.send(f'{member.name} ha dejado el servidor. 😢')
        print(f'Goodbye message sent to {member.name}')
    else:
        print('Channel canal not found')

#----------FIN UNIRSE Y SALIRSE----------



#----------ROL_ALEATORIO----------

roles = ["MID 🧙","TOP ⚔️","JUNGLA 🐺","ADC 🧝‍♂️","SUPORTIN 🏳️‍🌈"]

def rol_random():
    return random.choice(roles)

@bot.command()
async def rol(ctx):
    roles = rol_random()
    await ctx.send(roles)


#----------FIN----------




#INICIO_COMANDO_INFORMACION

comandos_bot = ["!jungla", "!mid", "!soporte", "!top", "!adc", "!rol", "!feo", "!clima", "!rifa", "!quejugar", "!chiste", "!equipos", "!wiki [lo que quieras buscar]" , "!Noticias"]


@bot.command()
async def comandos(ctx):
    await ctx.send("Los comandos son: " + " ▪️ ".join(comandos_bot))

#---------FIN_COMANDO_INFORMACION------------



#----------ELEGIR RANDOM LEAGUE OF LEGENDS----------

campeones_jungla = [
    "Amumu 🐻", "Lee Sin 🥋", "Warwick 🐺", "Kayn 😈", "Elise 🕷️", "Jarvan IV ⚔️",
    "Nunu & Willump 🦧", "Rek'Sai 🐉", "Graves 💀", "Nidalee 🐾", "Kindred 🐺🐏",
    "Master Yi 🗡️", "Xin Zhao 🐉", "Evelynn 😈", "Rengar 🦁", "Vi 👊", "Hecarim 🐴",
    "Shaco 🃏", "Kha'Zix 🦗", "Sejuani 🐷", "Olaf ⚔️", "Fiddlesticks 🎻", "Zac 🟢",
    "Skarner 🦂", "Udyr 🐻", "Gragas 🍺", "Nocturne 🌙", "Taliyah 🏔️", "Jax 🏹", "Twitch 🐀"
]

campeones_mid = [
    "Ahri 🦊", "Annie 🔥", "Zed 💀", "Yasuo 🌪️", "Syndra ✨", "Fizz 🐟", "Twisted Fate 🎴",
    "Katarina 🔪", "Orianna ⚙️", "Veigar 🧙", "Lux ✨", "Akali 🦇", "Viktor 🤖", "Talon 🗡️",
    "LeBlanc 🎭", "Azir 🌞", "Malzahar 🕷️", "Galio 🛡️", "Vel'Koz 👁️", "Cassiopeia 🐍",
    "Ekko ⏳", "Ryze 📘", "Ahri 🦊", "Anivia ❄️", "Kassadin 🔮", "Seraphine 🎤", "Lissandra ❄️","Aurelion 🐉"
]

campeones_support = [
    "Thresh 🗝️", "Lulu 🌺", "Leona 🛡️", "Nautilus ⚓", "Blitzcrank ⚡", "Soraka 🌟",
    "Janna 🌪️", "Bard 🎻", "Yuumi 🐾", "Rakan 🦊", "Nami 🌊", "Morgana 🖤", "Sona 🎵",
    "Zyra 🌿", "Lux ✨", "Taric 💎", "Alistar 🐮", "Braum 🛡️", "Karma ☯️", "Pyke 🗡️"
]

campeones_top = [
    "Sett 🥊", "Darius ⚔️", "Garen ⚔️", "Renekton 🐊", "Fiora 🗡️", "Camille 🕸️", "Jax 🏹",
    "Mordekaiser ⚔️", "Ornn 🔨", "Maokai 🌳", "Cho'Gath 🦈", "Shen 🗡️", "Sion 🛡️", "Nasus 🐶",
    "Riven 🗡️", "Teemo 🍄", "Illaoi 🐙", "Aatrox ⚔️", "Poppy 🛡️", "Tryndamere ⚔️", "Yorick ☠️",
    "Kayle ⚔️", "Volibear 🐻", "Wukong 🐵", "Gnar 🐾", "Kennen ⚡", "Malphite 🌋", "Pantheon ⚔️"
]

campeones_adc = [
    "Ezreal 🏹", "Jinx 🚀", "Miss Fortune ☠️", "Caitlyn 🔫", "Vayne 🏹", "Kai'Sa 🦋",
    "Samira 🔪", "Ashe 🏹", "Tristana 💣", "Sivir 🏹", "Draven 💰", "Varus 🏹", "Lucian 🔫",
    "Kog'Maw 🐛", "Xayah 🕊️", "Kalista 🌹", "Twitch 🐀", "Jhin 🔫", "Aphelios 🌙", "Kennen ⚡","Aurelion 🐉"
]



def junglas():
    return random.choice(campeones_jungla)

def mids():
    return random.choice(campeones_mid)

def sup():
    return random.choice(campeones_support)

def tops():
    return random.choice(campeones_top)

def adcs():
    return random.choice(campeones_adc)


#Comando elegir jungla aleatorio
@bot.command()
async def jungla(ctx):
    lista_junglas = junglas()
    await ctx.send(lista_junglas)

#Comando elegir mid aleatorio
@bot.command()
async def mid(ctx):
    lista_mid = mids()
    await ctx.send(lista_mid)

#Comando elegir soporte aleatorio
@bot.command()
async def soporte(ctx):
    lista_support = sup()
    await ctx.send(lista_support)

#Comando elegir top aleatorio
@bot.command()
async def top(ctx):
    lista_tops = tops()
    await ctx.send(lista_tops)

#Comando elegir adc aleatorio
@bot.command()
async def adc(ctx):
    lista_adc = adcs()
    await ctx.send(lista_adc)

#------------------FIN-------------------

#----------COMANDO CHAMPYARMADO----------
tres= ["Daño de Ataque (AD)❤️ ","Poder de Habilidad(AP)💙","Tanque💚"]
def quearmarlo():
    return random.choice(tres)




def randomplayer(rol):
    if rol == "JUNGLA 🐺":
        return junglas()
    elif rol == "MID 🧙":
        return mids()
    elif rol == "SUPORTIN 🏳️‍🌈":
        return sup()
    elif rol == "TOP ⚔️":
        return tops()
    elif rol == "ADC 🧝‍♂️":
        return adcs()

@bot.command()
async def quejugar(ctx):
    rol = rol_random()
    campeon = randomplayer(rol)
    adaptan = quearmarlo()
    await ctx.send(f'Te toca jugar como {rol} con {campeon} y {adaptan}')

#----------FIN CHAMPYARMADO----------


#--------COMANDOCHISTES-----------

todosloschistes = [
    "¿Por qué Teemo no puede ir al cine? 🎥 Porque siempre lo van a ubicar.",
    "¿Por qué Nasus siempre pierde en el amor? ❤️ Porque nunca junta suficientes corazones.",
    "¿Por qué Annie no usa internet? 🌐 Porque siempre está incendiada.",
    "¿Qué hace un Zac en el gimnasio? 🏋️‍♂️ ¡Flexea como un campeón!",
    "¿Qué hace Garen cuando está aburrido? 🔄 Da vueltas... ¡y vueltas... y vueltas!",
    "¿Qué pasa cuando Leona entra a una habitación? ☀️ Todos se iluminan.",
    "¿Por qué Udyr nunca se resfría? ❄️ Porque siempre está en forma.",
    "¿Por qué Thresh no juega al escondite? 🔦 Porque siempre te atrapa.",
    "¿Cómo se llama la fiesta favorita de Jhin? 🎉 ¡La cuarta!",
    "¿Qué dijo Yasuo cuando entró a la panadería? 🥖 '¿Dónde está el pan? Lo sigo buscando.'",
]



def randomchistes():
    return random.choice(todosloschistes)

@bot.command()
async def chiste(ctx):
    chistesrandom = randomchistes()
    await ctx.send(chistesrandom)



#---------FINCOMANDOCHISTES--------




#-------INICIAR COMANDO EQUIPOS--------


equiposenv =[
    "Huracán (Argentina) 🇦🇷", "Colón (Argentina) 🇦🇷", "Independiente (Argentina) 🇦🇷", "River Plate (Argentina) 🇦🇷", "Talleres (Argentina) 🇦🇷", "Argentinos Jrs (Argentina) 🇦🇷", "Atletico Tucuman (Argentina) 🇦🇷", "Banfield (Argentina) 🇦🇷", "Gimnasia (Argentina) 🇦🇷", "Rosario Central (Argentina) 🇦🇷", "Barracas Central (Argentina) 🇦🇷", "Arsenal (Argentina) 🇦🇷", "Racing Club (Argentina) 🇦🇷", "Belgrano (Argentina) 🇦🇷", "Defensa y Justicia (Argentina) 🇦🇷", "Sarmiento (Argentina) 🇦🇷", "Central Córdoba (Argentina) 🇦🇷", "Newell's (Argentina) 🇦🇷", "San Lorenzo (Argentina) 🇦🇷", "Boca Juniors (Argentina) 🇦🇷",
    "Unión (Argentina) 🇦🇷", "Platense (Argentina) 🇦🇷", "Estudiantes (Argentina) 🇦🇷", "Tigre (Argentina) 🇦🇷", "Lanús (Argentina) 🇦🇷", "Vélez Sarsfield (Argentina) 🇦🇷",
    "🇩🇪 Alemania", "🇦🇷 Argentina", "🇧🇪 Bélgica", "🇶🇦 Catar", "🇭🇷 Croacia", "🇩🇰 Dinamarca", "🏴 Escocia", "🇪🇸 España",
    "🇺🇸 Estados Unidos", "🇫🇮 Finlandia", "🇫🇷 Francia", "🏴 Gales", "🇬🇭 Ghana", "🇭🇺 Hungría", "🏴 Inglaterra",
    "🇬🇧 Irlanda del Norte", "🇮🇸 Islandia", "🇮🇹 Italia", "🇲🇦 Marruecos", "🇲🇽 México", "🇳🇴 Noruega", "🇳🇿 Nueva Zelanda",
    "🇳🇱 Países Bajos", "🇵🇱 Polonia", "🇵🇹 Portugal", "🇮🇪 Irlanda", "🇨🇿 República Checa", "🇷🇴 Rumanía", "🇸🇪 Suecia", "🇺🇦 Ucrania"
]



def equiporandom1():
    return random.sample(equiposenv, 2)



@bot.command()
async def equipos(ctx):
    equiposrandom,equiposrandom2 = equiporandom1()
    await ctx.send(f'El equipo 1 es {equiposrandom} y El equipo 2 es {equiposrandom2}')



#--------FIN COMANDO EQUIPOS---------






#-----INICIO WIKIPEDIA API---------

# Configuración de la API de Wikipedia en español con user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='es',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='MyDiscordBot/1.0 (https://example.com/contact)'
)

# Comando !wiki
@bot.command()
async def wiki(ctx, *, search):
    page = wiki_wiki.page(search)
    if page.exists():
        summary = page.summary
        if len(summary) > 2000:
            chunks = [summary[i:i+2000] for i in range(0, len(summary), 2000)] #Manda mensajes de maximo 2000 carateres en diferentes msj
            for chunk in chunks:
                await ctx.send(chunk)
        else:
            await ctx.send(f"**{page.title}**\n\n{summary}\n\nLeer más: {page.fullurl}")
    else:
        await ctx.send("No se encontró ninguna página con ese título en Wikipedia.") #Si no se encuentra la pag

#-----FIN WIKIPEDIA API---------

#---INICIO COMANDO NOTICIAS (Devuelve las 5 mejores noticias del dia en Argentina)

API_KEY = '#Clave API de NewsAPI'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def obtener_noticias(pais='ar', categoria=None):
    parametros = {
        'apiKey': API_KEY,
        'country': pais,
    }
    if categoria:
        parametros['category'] = categoria

    respuesta = requests.get(BASE_URL, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos['articles']
    else:
        return None

@bot.command()
async def noticias(ctx, categoria=None):
    noticias = obtener_noticias(pais='ar', categoria=categoria)
    if noticias:
        for noticia in noticias[:5]:  # Limitar a las primeras 5 noticias
            await ctx.send(noticia['title'])
    else:
        await ctx.send('No se pudieron obtener noticias.')
        
#-----Fin comando noticias)


bot.run("TOKEN DEL BOT")
