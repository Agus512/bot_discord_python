import discord
from discord.ext import commands, tasks
import os
import time
import random
import requests
import string
from dotenv import load_dotenv
import wikipediaapi
from openai import OpenAI
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members= True
load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)

#------Updates------

#Último update 04/09/2025 (Se integró OpenAI al bot de discord funcionado correctamente con la apikey)
#

#------Fin_updates------


#------------INICIO SERVIDOR PYTHON----------------

#open-message.console.log
print("▪️ ▪️ ▪️ INICIALIZANDO SERVIDOR ▪️ ▪️ ▪️")
print("▪️ 10% ▪️")
time.sleep(2)
print("▪️ 20% ▪️")
time.sleep(4)
print("▪️ 40% ▪️")
time.sleep(1)
print("▪️ 80% ▪️")
time.sleep(1)
print("▪️ ▪️ 100% ▪️ ▪️")
print("🤖Conexión con IA: realizada correctamente🤖")
print("🚀🚀🚀SERVIDOR ACTIVO: BOT ONLINE🚀🚀🚀")

#close-message.console.log

#equiposenv = os.getenv('equiposenv') #PRUEBA PARA USAR LAS VARIABLES .env
#-----------fin.servidor----------------

#Inicio Chatbot
OPENAI_API_KEY=("API OPENAI")
client = OpenAI(api_key=OPENAI_API_KEY)

client = OpenAI(api_key=OPENAI_API_KEY)

@bot.command()
async def bandurri(ctx, *, pregunta: str):
    if len(pregunta) > 99:
        await ctx.send("La pregunta no puede tener más de 100 caracteres.")
        return

    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Sos un chatbot argentino creado por la persona Code512, mal hablado, "
                            "Burlón, siempre que respondes puteas "
                            "Respondé de forma graciosa pero siendo un sorete, irónica y despectiva, basicamente como un forro. "
                            "No seas neutral ni educado, siempre mal hablado"
                        )
                    },
                    {"role": "user", "content": pregunta}
                ],
                max_tokens=150
            )
        )

        respuesta = response.choices[0].message.content.strip()
        await ctx.send(respuesta)

    except Exception as e:
        await ctx.send(f"⚠️ Error al contactar OpenAI: {e}")


#Fin Chatbot

#----------------------------------

#open-weather-command
OWM_API_KEY = "Open weather map APIKEY"

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
#close-weather-command

#----------------------------------

#open-rifa-command

premios = [
    '¡Felicidades! Ganaste un manual de instrucciones ilegible. 📜',
    '¡Enhorabuena! Ahora posees un paracaídas de segunda mano. 🪂',
    '¡Te ganaste una pelota cuadrada para jugar fútbol! ⬛️⚽️',
    '¡Felicitaciones! Has recibido un abanico sin aspas. 🌀',
    '¡Aquí tienes un sombrero que no te queda! 🎩',
    '¡Has ganado un mapa del tesoro sin indicaciones! 🗺️',
    '¡Te llevas un diccionario sin verbos! 📖',
    '¡Felicidades! Ahora tienes un cuadro en blanco. 🖼️',
    '¡Te ganaste un par de calcetines desparejados! 🧦🧦',
    '¡Aquí tienes una botella de agua vacía! 💧',
    '¡Has recibido un traje de baño con agujeros! 👙',
    '¡Te llevas un paraguas que solo abre hacia adentro! ☂️',
    '¡Felicitaciones! Has ganado una tostadora que solo quema el pan. 🍞',
    '¡Ganaste una estatua de hielo para el Sahara! 🗿❄️',
    '¡Te llevas una cámara que solo toma fotos borrosas! 📷',
    '¡Aquí tienes un reloj que siempre marca las 13:00! ⏰',
    '¡Felicidades! Ahora posees un móvil sin pantalla táctil. 📱',
    '¡Ganaste un juego de ajedrez sin piezas negras! ♟️',
    '¡Te llevas un coche que solo avanza marcha atrás! 🚗',
    '¡Has recibido un teclado sin la tecla de espacio! ⌨️',
    '¡Aquí tienes una almohada que siempre está fría! 🛌',
    '¡Felicitaciones! Ahora posees un bolígrafo que solo escribe en invisible. 🖊️',
    '¡Ganaste unos auriculares que solo reproducen música de anuncios! 🎧',
    '¡Te llevas un GPS que siempre indica la dirección opuesta! 🗺️',
    '¡Has recibido un televisor que solo transmite canales de radio! 📺📻',
]



def rifa_random():
    return random.choice(premios)


@bot.command()
async def rifa(ctx):
    premios = rifa_random()
    await ctx.send(premios)


#close-rifa-command


#----------------------------------


#-----open-welcome_bye_member-notification-----

#Evento cuando un miembro se une al servidor
@bot.event
async def on_member_join(member):
    #Especificar el canal 'p1j4z' para el mensaje de bienvenida
    channel = discord.utils.get(member.guild.text_channels, name='p1j4z')
    if channel:
        await channel.send(f'¡Bienvenido al servidor trolaso, {member.mention}! 🎉')
        print(f'Welcome message sent to {member.name}')
    else:
        print('Channel p1j4z not found')

#Evento cuando un miembro se va del servidor
@bot.event
async def on_member_remove(member):
    # Especificar el canal 'p1j4z' para el mensaje de despedida
    channel = discord.utils.get(member.guild.text_channels, name='p1j4z')
    if channel:
        await channel.send(f'{member.name} dejó el servidor el cagón. 😢')
        print(f'Goodbye message sent to {member.name}')
    else:
        print('Channel p1j4z not found')

#-----close-welcome_bye_member-notification-----


#----------------------------------


#Open-ROL-Command

roles = ["MID 🧙","TOP ⚔️","JUNGLA 🐺","ADC 🧝‍♂️","SUPORTIN 🏳️‍🌈"]

def rol_random():
    return random.choice(roles)

@bot.command()
async def rol(ctx):
    roles = rol_random()
    await ctx.send(roles)


#Close-ROL-Command


#----------------------------------


#Open-FEO-Command

@bot.command()
async def feo(ctx):
    feo_porcentaje = random.randint(0, 100)
    if feo_porcentaje > 50 and feo_porcentaje < 99:
        await ctx.send(f"Sos un {feo_porcentaje}% garchable😍")
    else:
        await ctx.send(f"Sos un {feo_porcentaje}% garchable🤮")
    if feo_porcentaje == 100:
        await ctx.send(f"Sos un {feo_porcentaje}% garchableee🍆😍💝")

#Close-FEO-Command

#----------------------------------


#Open-COMANDOS-command

comandos_bot = "Los comandos son: ▪️ !jungla ▪️ !mid ▪️ !soporte ▪️ !top ▪️ !adc ▪️ !rol ▪️ !feo ▪️ !clima(lugar) ▪️ !rifa ▪️ !quejugar ▪️ !chiste ▪️ !equipos ▪️ !equipos4 ▪️ !equiposx ▪️ !wiki [lo que quieras buscar] ▪️ !fifa ▪️ !csmap ▪️ !bandurri (chat con IA)"

@bot.command()
async def comandos(ctx):
    # Enviar la cadena completa de comandos
    await ctx.send(comandos_bot)

#Close-COMANDOS-command

#----------------------------------

#Open-Random_LOL-Command

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

#Comando elegir ADC aleatorio
@bot.command()
async def adc(ctx):
    lista_adc = adcs()
    await ctx.send(lista_adc)

#Close-RANDOM_LOL-command

#----------------------------------

#Open-ARMADO_RANDOM-command
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

#Close-ARMADO_RANDOM-command


#----------------------------------

#Open-CHISTES-Command

todosloschistes = [
    "¿Cuál es el Counter de Vladimir?....Un tampón", "¿Cuál es el Counter de Kha' Zix?...El insecticida","¿Que hace Lucian full ap?......Magia Negra","¿Por qué ni 10.000 bronces pueden cambiar una lámpara?....Porque no pueden subir",
    "¿Por qué yasuo no puede conseguir novia?....Porque crítica mucho","¿Por que hay que desconfiar siempre de ahri?....Porque es una zorra", "¿Que es mas rápido que ramus con Fantasmal?...Ekko con tu telefono",
    "Por qué gragas es gordo?...Porque juega league of legends","¿Cual es el counter de Kassadin?....El divorcin.","¿Cual es el helado favorito de Vayne?...La vainilla","Se abre el telón y aparece Zed matando a Zilean y Ekko ¿Cómo se llama la obra?.....Matando el tiempo","¿Cuál es el Counter de Karthus?...El suicidio asistido."
]



def randomchistes():
    return random.choice(todosloschistes)

@bot.command()
async def chiste(ctx):
    chistesrandom = randomchistes()
    await ctx.send(chistesrandom)


#Close-CHISTES-Command

#----------------------------------

#Open-EQUIPOS4-Command

equipos_4_estrellas_o_mas = [
    "AFC Richmond (Inglaterra) 🇬🇧",
    "Arsenal FC (Inglaterra) 🇬🇧",
    "Aston Villa (Inglaterra) 🇬🇧",
    "Chelsea FC (Inglaterra) 🇬🇧",
    "Liverpool FC (Inglaterra) 🇬🇧",
    "Manchester City (Inglaterra) 🇬🇧",
    "Manchester United (Inglaterra) 🇬🇧",
    "Tottenham Hotspur (Inglaterra) 🇬🇧",
    "Brighton & Hove Albion (Inglaterra) 🇬🇧",
    "Real Madrid (España) 🇪🇸",
    "FC Barcelona (España) 🇪🇸",
    "Atletico Madrid (España) 🇪🇸",
    "Sevilla FC (España) 🇪🇸",
    "Real Betis (España) 🇪🇸",
    "Real Sociedad (España) 🇪🇸",
    "Paris Saint-Germain (Francia) 🇫🇷",
    "AS Monaco (Francia) 🇫🇷",
    "Olympique de Marseille (Francia) 🇫🇷",
    "Olympique Lyonnais (Francia) 🇫🇷",
    "Bayern Munich (Alemania) 🇩🇪",
    "Borussia Dortmund (Alemania) 🇩🇪",
    "RB Leipzig (Alemania) 🇩🇪",
    "Inter de Milán (Italia) 🇮🇹",
    "AC Milan (Italia) 🇮🇹",
    "Juventus (Italia) 🇮🇹",
    "Napoli (Italia) 🇮🇹",
    "AS Roma (Italia) 🇮🇹",
    "Lazio (Italia) 🇮🇹",
    "Atalanta (Italia) 🇮🇹",
    "Sporting CP (Portugal) 🇵🇹",
    "SL Benfica (Portugal) 🇵🇹",
    "FC Porto (Portugal) 🇵🇹",
    "AFC Ajax (Países Bajos) 🇳🇱",
    "PSV Eindhoven (Países Bajos) 🇳🇱",
    "Feyenoord (Países Bajos) 🇳🇱",
    "River Plate (Argentina) 🇦🇷",
    "Boca Juniors (Argentina) 🇦🇷",
    "LAFC (Estados Unidos) 🇺🇸",
    "Seattle Sounders (Estados Unidos) 🇺🇸",
    "New York City FC (Estados Unidos) 🇺🇸",
    "CF Montreal (Canadá) 🇨🇦"
]

def equiporandom():
    return random.sample(equipos_4_estrellas_o_mas, 2)

@bot.command()
async def equipos4(ctx):
    equipo1, equipo2 = equiporandom()
    await ctx.send(f'El equipo 1 es {equipo1} y El equipo 2 es {equipo2}')


#Close-EQUIPOS4-Command

#----------------------------------

#Open-EQUIPOS-Command

equiposenv =[
    "Huracán (Argentina) 🇦🇷", "Colón (Argentina) 🇦🇷", "Independiente (Argentina) 🇦🇷", "River Plate (Argentina) 🇦🇷", "Talleres (Argentina) 🇦🇷", "Argentinos Jrs (Argentina) 🇦🇷", "Atletico Tucuman (Argentina) 🇦🇷", "Banfield (Argentina) 🇦🇷", "Gimnasia (Argentina) 🇦🇷", "Rosario Central (Argentina) 🇦🇷", "Barracas Central (Argentina) 🇦🇷", "Arsenal (Argentina) 🇦🇷", "Racing Club (Argentina) 🇦🇷", "Belgrano (Argentina) 🇦🇷", "Defensa y Justicia (Argentina) 🇦🇷", "Sarmiento (Argentina) 🇦🇷", "Central Córdoba (Argentina) 🇦🇷", "Newell's (Argentina) 🇦🇷", "San Lorenzo (Argentina) 🇦🇷", "Boca Juniors (Argentina) 🇦🇷",
    "Unión (Argentina) 🇦🇷", "Platense (Argentina) 🇦🇷", "Estudiantes (Argentina) 🇦🇷", "Tigre (Argentina) 🇦🇷", "Lanús (Argentina) 🇦🇷", "Vélez Sarsfield (Argentina) 🇦🇷",
    "Adelaide United (Australia) 🇦🇺", "Brisbane Roar (Australia) 🇦🇺", "Central Coast Mariners (Australia) 🇦🇺", "Macarthur FC (Australia) 🇦🇺", "Melbourne City (Australia) 🇦🇺", "Newcastle United Jets (Australia) 🇦🇺", "Perth Glory (Australia) 🇦🇺", "Sydney FC (Australia) 🇦🇺", "Wellington Phoenix (Australia) 🇦🇺", "Western Sydney Wanderers (Australia) 🇦🇺", "Western United (Australia) 🇦🇺",
    "RB Salzburg (Austria) 🇦🇹", "SK Sturm Graz (Austria) 🇦🇹", "LASK (Austria) 🇦🇹", "Austria Klagenfurt (Austria) 🇦🇹", "TSV Hartberg (Austria) 🇦🇹", "SCR Altach (Austria) 🇦🇹", "SK Rapid Wien (Austria) 🇦🇹", "Wolfsberger AC (Austria) 🇦🇹",
    "KAA Gent (Bélgica) 🇧🇪", "RSC Anderlecht (Bélgica) 🇧🇪", "Club Brugge KV (Bélgica) 🇧🇪", "Royale Union Saint-Gilloise (Bélgica) 🇧🇪", "Cercle Brugge (Bélgica) 🇧🇪", "Royal Antwerp FC (Bélgica) 🇧🇪", "KRC Genk (Bélgica) 🇧🇪", "Sint-Truidense VV (Bélgica) 🇧🇪", "RWD Molenbeek (Bélgica) 🇧🇪", "KV Mechelen (Bélgica) 🇧🇪", "KAS Eupen (Bélgica) 🇧🇪", "Standard Liège (Bélgica) 🇧🇪", "Sporting Charleroi (Bélgica) 🇧🇪", "KVC Westerlo (Bélgica) 🇧🇪", "KV Kortrijk (Bélgica) 🇧🇪",
    "Shanghai Port FC (China) 🇨🇳", "Shandong Taishan FC (China) 🇨🇳", "Shanghai Shenhua FC (China) 🇨🇳", "Zhejiang Professional FC (China) 🇨🇳", "Chengdu Rongcheng FC (China) 🇨🇳", "Beijing Guoan FC (China) 🇨🇳", "Wuhan Three Towns FC (China) 🇨🇳", "Tianjin Jinmen Tiger FC (China) 🇨🇳", "Changchun Yatai FC (China) 🇨🇳", "Henan Songshan Longmen FC (China) 🇨🇳", "Cangzhou Mighty Lions FC (China) 🇨🇳", "Meizhou Hakka FC (China) 🇨🇳", "Qingdao FC (China) 🇨🇳", "Dalian Professional FC (China) 🇨🇳", "Nantong Zhiyun FC (China) 🇨🇳", "Shenzhen FC (China) 🇨🇳",
    "FC Copenhagen (Dinamarca) 🇩🇰", "Silkeborg IF (Dinamarca) 🇩🇰", "FC Nordsjælland (Dinamarca) 🇩🇰", "Brøndby IF (Dinamarca) 🇩🇰", "FC Midtjylland (Dinamarca) 🇩🇰", "Aarhus GF (Dinamarca) 🇩🇰", "Lyngby BK (Dinamarca) 🇩🇰", "Viborg FF (Dinamarca) 🇩🇰", "Randers FC (Dinamarca) 🇩🇰", "Odense Boldklub (Dinamarca) 🇩🇰", "Vejle Boldklub (Dinamarca) 🇩🇰",
    "1. FC Nürnberg (Alemania) 🇩🇪", "Braunschweig (Alemania) 🇩🇪", "Düsseldorf (Alemania) 🇩🇪", "FC Hansa Rostock (Alemania) 🇩🇪", "FC Schalke 04 (Alemania) 🇩🇪", "FC St. Pauli (Alemania) 🇩🇪", "Fürth (Alemania) 🇩🇪", "Hamburger SV (Alemania) 🇩🇪", "Hannover 96 (Alemania) 🇩🇪", "Hertha BSC (Alemania) 🇩🇪", "Holstein Kiel (Alemania) 🇩🇪", "Kaiserslautern (Alemania) 🇩🇪", "Karlsruher SC (Alemania) 🇩🇪", "Magdeburg (Alemania) 🇩🇪", "SC Paderborn 07 (Alemania) 🇩🇪", "SV Elversberg (Alemania) 🇩🇪", "VFL Osnabrück (Alemania) 🇩🇪", "Wiesbaden (Alemania) 🇩🇪",
    "1860 Munich (Alemania) 🇩🇪", "Arminia Bielefeld (Alemania) 🇩🇪", "Borussia Dortmund II (Alemania) 🇩🇪", "Duisburg (Alemania) 🇩🇪", "Dynamo Dresden (Alemania) 🇩🇪", "FC Erzgebirge Aue (Alemania) 🇩🇪", "FC Ingolstadt 04 (Alemania) 🇩🇪", "Hallescher FC (Alemania) 🇩🇪", "Jahn Regensburg (Alemania) 🇩🇪", "Preuben Münster (Alemania) 🇩🇪", "Rot-Weiss Essen (Alemania) 🇩🇪", "Saarbrücken (Alemania) 🇩🇪", "SC Freiburg II (Alemania) 🇩🇪", "SC Verl (Alemania) 🇩🇪", "SSV Ulm 1846 (Alemania) 🇩🇪", "SV Sandhausen (Alemania) 🇩🇪", "SV Waldhof (Alemania) 🇩🇪", "Unterhaching (Alemania) 🇩🇪", "VFB Lübeck (Alemania) 🇩🇪", "Viktoria Köln (Alemania) 🇩🇪",
    "Abha Club (Arabia Saudí) 🇸🇦", "Al Ahli (Arabia Saudí) 🇸🇦", "Al Fateh (Arabia Saudí) 🇸🇦", "Al Fayha (Arabia Saudí) 🇸🇦", "Al Hilal (Arabia Saudí) 🇸🇦", "Al Ittihad (Arabia Saudí) 🇸🇦", "Al Khaleej (Arabia Saudí) 🇸🇦", "Al Nassr (Arabia Saudí) 🇸🇦", "Al Raed (Arabia Saudí) 🇸🇦", "Al Riyadh (Arabia Saudí) 🇸🇦", "Al Shabab (Arabia Saudí) 🇸🇦", "Al Taawoun (Arabia Saudí) 🇸🇦", "Al Tai (Arabia Saudí) 🇸🇦", "Al Wehda (Arabia Saudí) 🇸🇦", "Al-Okhdood (Arabia Saudí) 🇸🇦", "Al Hazem (Arabia Saudí) 🇸🇦", "Damac FC (Arabia Saudí) 🇸🇦", "Ettifaq FC (Arabia Saudí) 🇸🇦",
    "Aberdeen (Escocia) 🇸🇨", "Celtic de Glasgow (Escocia) 🇸🇨", "Dundee FC (Escocia) 🇸🇨", "Hearts (Escocia) 🇸🇨", "Hibernian (Escocia) 🇸🇨", "Kilmarnock (Escocia) 🇸🇨", "Livingston (Escocia) 🇸🇨", "Motherwell (Escocia) 🇸🇨", "Rangers FC (Escocia) 🇸🇨", "Ross County (Escocia) 🇸🇨", "St. Johnstone (Escocia) 🇸🇨", "St. Mirren (Escocia) 🇸🇨",
    "Athletic Club de Bilbao (España) 🇪🇸", "Atlético de Madrid (España) 🇪🇸", "Osasuna (España) 🇪🇸", "Cádiz CF (España) 🇪🇸", "Deportivo Alavés (España) 🇪🇸", "FC Barcelona (España) 🇪🇸", "Getafe CF (España) 🇪🇸", "Girona FC (España) 🇪🇸", "Granada CF (España) 🇪🇸", "Rayo Vallecano (España) 🇪🇸", "RC Celta (España) 🇪🇸", "RCD Mallorca (España) 🇪🇸", "Real Betis (España) 🇪🇸", "Real Madrid (España) 🇪🇸", "Real Sociedad (España) 🇪🇸", "Sevilla FC (España) 🇪🇸", "UD Almería (España) 🇪🇸", "UD Las Palmas (España) 🇪🇸", "Valencia CF (España) 🇪🇸", "Villarreal CF (España) 🇪🇸",
    "AD Alcorcón (España) 🇪🇸", "Albacete BP (España) 🇪🇸", "Burgos CF (España) 🇪🇸", "CD Eldense (España) 🇪🇸", "CD Leganés (España) 🇪🇸", "CD Mirandés (España) 🇪🇸", "CD Tenerife (España) 🇪🇸", "Elche CF (España) 🇪🇸", "FC Andorra (España) 🇪🇸", "FC Cartagena (España) 🇪🇸", "Levante UD (España) 🇪🇸", "Real Oviedo (España) 🇪🇸", "Real Racing Club (España) 🇪🇸", "Real Sporting (España) 🇪🇸", "Real Valladolid CF (España) 🇪🇸", "Racing de Ferrol (España) 🇪🇸", "RCD Espanyol (España) 🇪🇸", "Real Zaragoza (España) 🇪🇸", "SD Amorebieta (España) 🇪🇸", "SD Eibar (España) 🇪🇸", "SD Huesca (España) 🇪🇸", "Villarreal CF B (España) 🇪🇸",
    "Atlanta United (Estados Unidos) 🇺🇸", "Austin FC (Estados Unidos) 🇺🇸", "CF Montréal (Estados Unidos) 🇺🇸", "Charlotte FC (Estados Unidos) 🇺🇸", "Chicago Fire FC (Estados Unidos) 🇺🇸", "Colorado Rapids (Estados Unidos) 🇺🇸", "Columbus Crew (Estados Unidos) 🇺🇸", "D.C. United (Estados Unidos) 🇺🇸", "FC Cincinnati (Estados Unidos) 🇺🇸", "FC Dallas (Estados Unidos) 🇺🇸", "Houston Dynamo (Estados Unidos) 🇺🇸", "Inter Miami CF (Estados Unidos) 🇺🇸", "LA Galaxy (Estados Unidos) 🇺🇸", "LAFC (Estados Unidos) 🇺🇸", "Minnesota United (Estados Unidos) 🇺🇸", "Nashville SC (Estados Unidos) 🇺🇸", "New England (Estados Unidos) 🇺🇸", "New York City FC (Estados Unidos) 🇺🇸", "Orlando City (Estados Unidos) 🇺🇸", "Philadelphia U. (Estados Unidos) 🇺🇸", "Portland Timbers (Estados Unidos) 🇺🇸", "Real Salt Lake (Estados Unidos) 🇺🇸", "Red Bulls New York (Estados Unidos) 🇺🇸", "SJ Earthquakes (Estados Unidos) 🇺🇸", "Sounders FC (Estados Unidos) 🇺🇸", "Sporting KC (Estados Unidos) 🇺🇸", "St. Louis City SC (Estados Unidos) 🇺🇸", "Toronto FC (Estados Unidos) 🇺🇸", "Whitecaps FC (Estados Unidos) 🇺🇸",
    "AS Monaco (Francia) 🇫🇷", "Clermont Foot 63 (Francia) 🇫🇷", "FC Lorient (Francia) 🇫🇷", "FC Metz (Francia) 🇫🇷", "FC Nantes (Francia) 🇫🇷", "Le Havre AC (Francia) 🇫🇷", "Losc Lille (Francia) 🇫🇷", "Montpellier HSC (Francia) 🇫🇷", "Olympique Marsella (Francia) 🇫🇷", "OGC Niza (Francia) 🇫🇷", "Olympique Lyon (Francia) 🇫🇷", "París Saint-Germain (Francia) 🇫🇷", "RC Estrasburgo (Francia) 🇫🇷", "RC Lens (Francia) 🇫🇷", "Stade Brestois (Francia) 🇫🇷", "Stade de Reims (Francia) 🇫🇷", "Stade Rennais FC (Francia) 🇫🇷", "Toulouse FC (Francia) 🇫🇷",
    "AC Ajaccio (Francia) 🇫🇷", "Aj Auxerre (Francia) 🇫🇷", "Amiens SC (Francia) 🇫🇷", "Angers SCO (Francia) 🇫🇷", "En Avant Guingamp (Francia) 🇫🇷", "Es Troyes AC (Francia) 🇫🇷", "FC Annecy (Francia) 🇫🇷", "Girondins de Burdeos (Francia) 🇫🇷", "Grenoble Foot 38 (Francia) 🇫🇷", "Laval MFC (Francia) 🇫🇷", "París FC (Francia) 🇫🇷", "Pau FC (Francia) 🇫🇷", "Quevilly-Rouen (Francia) 🇫🇷", "Rodez AF (Francia) 🇫🇷", "SC Bastia (Francia) 🇫🇷", "SM Caen (Francia) 🇫🇷", "US Concarneau (Francia) 🇫🇷", "USL Dunkerque (Francia) 🇫🇷", "Valenciennes FC (Francia) 🇫🇷",
    "Bengaluru FC (India) 🇮🇳", "Chennaiyin FC (India) 🇮🇳", "East Bengal (India) 🇮🇳", "FC Goa (India) 🇮🇳", "Hyderabad FC (India) 🇮🇳", "Jamshedpur FC (India) 🇮🇳", "Kerala Blasters (India) 🇮🇳", "Mohun Bagan SG (India) 🇮🇳", "Mumbai City FC (India) 🇮🇳", "Northeast United (India) 🇮🇳", "Odisha FC (India) 🇮🇳", "Punjab FC (India) 🇮🇳",
    "Bergamo Calcio (Italia) 🇮🇹", "Bolonia (Italia) 🇮🇹", "Cagliari (Italia) 🇮🇹", "Empoli (Italia) 🇮🇹", "Fiorentina (Italia) 🇮🇹", "Frosinone (Italia) 🇮🇹", "Genoa (Italia) 🇮🇹", "Hellas Verona (Italia) 🇮🇹", "Inter de Milán (Italia) 🇮🇹", "Juventus (Italia) 🇮🇹", "Latium (Italia) 🇮🇹", "Lecce (Italia) 🇮🇹", "Milán (Italia) 🇮🇹", "Monza (Italia) 🇮🇹", "Napoli FC (Italia) 🇮🇹", "Roma FC (Italia) 🇮🇹", "Salerno (Italia) 🇮🇹", "Sassuolo (Italia) 🇮🇹", "Torino (Italia) 🇮🇹", "Udinese (Italia) 🇮🇹",
    "Ascoli (Italia) 🇮🇹", "Bari (Italia) 🇮🇹", "Borgocalcio (Italia) 🇮🇹", "Brisigonza (Italia) 🇮🇹", "Catanzaro (Italia) 🇮🇹", "Cittadella (Italia) 🇮🇹", "Como (Italia) 🇮🇹", "Cosenza (Italia) 🇮🇹", "Cremonese (Italia) 🇮🇹", "Feralpisalo (Italia) 🇮🇹", "Módena (Italia) 🇮🇹", "Palermo (Italia) 🇮🇹", "Parma (Italia) 🇮🇹", "Pisa (Italia) 🇮🇹", "Reggiana (Italia) 🇮🇹", "Sampdoria (Italia) 🇮🇹", "Spezia (Italia) 🇮🇹", "Südtirol (Italia) 🇮🇹", "Ternana (Italia) 🇮🇹", "Venezia (Italia) 🇮🇹",
    "Aalesunds FK (Noruega) 🇳🇴", "FK Bodo/Glimt (Noruega) 🇳🇴", "FK Haugesund (Noruega) 🇳🇴", "Hamkam Football (Noruega) 🇳🇴", "Lillestrom SK (Noruega) 🇳🇴", "Molde FK (Noruega) 🇳🇴", "Odds BK (Noruega) 🇳🇴", "Rosenborg BK (Noruega) 🇳🇴", "Sandefjord (Noruega) 🇳🇴", "Sarpsborg 08 (Noruega) 🇳🇴", "SK Brann (Noruega) 🇳🇴", "Stabaek Football (Noruega) 🇳🇴", "Stromsgodset IF (Noruega) 🇳🇴", "Tromso Il (Noruega) 🇳🇴", "Valerenga Fotball (Noruega) 🇳🇴", "Viking FK (Noruega) 🇳🇴",
    "Ajax (Países Bajos) 🇳🇱", "Almere City FC (Países Bajos) 🇳🇱", "AZ (Países Bajos) 🇳🇱", "Excelsior (Países Bajos) 🇳🇱", "FC Twente (Países Bajos) 🇳🇱", "FC Utrecht (Países Bajos) 🇳🇱", "FC Volendam (Países Bajos) 🇳🇱", "Feyenoord (Países Bajos) 🇳🇱", "Fortuna Sittard (Países Bajos) 🇳🇱", "GO Agead Eagles (Países Bajos) 🇳🇱", "Heracles Almelo (Países Bajos) 🇳🇱", "N.E.C. Nijmegen (Países Bajos) 🇳🇱", "PEC Zwolle (Países Bajos) 🇳🇱", "PSV (Países Bajos) 🇳🇱", "RKC Waalwijk (Países Bajos) 🇳🇱", "SC Heerenveen (Países Bajos) 🇳🇱", "Sparta Rotterdam (Países Bajos) 🇳🇱", "Vitesse (Países Bajos) 🇳🇱",
    "Cracovia (Polonia) 🇵🇱", "Górnik Zabrze (Polonia) 🇵🇱", "Jagiellonia (Polonia) 🇵🇱", "Korona Kielce (Polonia) 🇵🇱", "Lech Poznan (Polonia) 🇵🇱", "Legia Warszawa (Polonia) 🇵🇱", "Lódzki KS (Polonia) 🇵🇱", "Piast Gliwice (Polonia) 🇵🇱", "Pogon SZCzecin (Polonia) 🇵🇱", "Puszcza (Polonia) 🇵🇱", "Radomiak Radom (Polonia) 🇵🇱", "Raków (Polonia) 🇵🇱", "Ruck Chorzow (Polonia) 🇵🇱", "Stal Mielec (Polonia) 🇵🇱", "S. Wroclaw (Polonia) 🇵🇱", "Warta Piznan (Polonia) 🇵🇱", "Widzew Lodz (Polonia) 🇵🇱", "Zaglebie Lubin (Polonia) 🇵🇱",
    "Arouca (Portugal) 🇵🇹", "Boavista FC (Portugal) 🇵🇹", "Casa Pia AC (Portugal) 🇵🇹", "Estoril Praia (Portugal) 🇵🇹", "Estrela Amadora (Portugal) 🇵🇹", "Farense (Portugal) 🇵🇹", "FC Famalicao (Portugal) 🇵🇹", "FC Porto (Portugal) 🇵🇹", "FC Vizela (Portugal) 🇵🇹", "GD Chaves (Portugal) 🇵🇹", "Gil Vicente (Portugal) 🇵🇹", "Moreirense FC (Portugal) 🇵🇹", "Portimonense SC (Portugal) 🇵🇹", "Rio Ave FC (Portugal) 🇵🇹", "SC Braga (Portugal) 🇵🇹", "SL Benfica (Portugal) 🇵🇹", "Sporting Portugal (Portugal) 🇵🇹", "Vitória SC (Portugal) 🇵🇹",
    "Daegu FC (República de Corea) 🇰🇷", "Daejeon Citizen (República de Corea) 🇰🇷", "FC Seoul (República de Corea) 🇰🇷", "Gangwon FC (República de Corea) 🇰🇷", "Gwangju FC (República de Corea) 🇰🇷", "Incheon United (República de Corea) 🇰🇷", "Jeju United (República de Corea) 🇰🇷", "Jeonbuk Hyundai (República de Corea) 🇰",
    "🇩🇪 Alemania", "🇦🇷 Argentina", "🇧🇪 Bélgica", "🇶🇦 Catar", "🇭🇷 Croacia", "🇩🇰 Dinamarca", "🏴 Escocia", "🇪🇸 España",
    "🇺🇸 Estados Unidos", "🇫🇮 Finlandia", "🇫🇷 Francia", "🏴 Gales", "🇬🇭 Ghana", "🇭🇺 Hungría", "🏴 Inglaterra",
    "🇬🇧 Irlanda del Norte", "🇮🇸 Islandia", "🇮🇹 Italia", "🇲🇦 Marruecos", "🇲🇽 México", "🇳🇴 Noruega", "🇳🇿 Nueva Zelanda",
    "🇳🇱 Países Bajos", "🇵🇱 Polonia", "🇵🇹 Portugal", "🇮🇪 Irlanda", "🇨🇿 República Checa", "🇷🇴 Rumanía", "🇸🇪 Suecia", "🇺🇦 Ucrania"
]

equipos_fifa25= [
    # Argentina
    "Argentinos Jrs (Argentina ar)", "Atlético Tucumán (Argentina ar)", "Barracas Central (Argentina ar)", "Banfield (Argentina ar)",
    "Belgrano (Argentina ar)", "Boca Juniors (Argentina ar)", "Central Córdoba (Argentina ar)", "Defensa y Justicia (Argentina ar)",
    "Deportivo Riestra (Argentina ar)", "Estudiantes (Argentina ar)", "Gimnasia (Argentina ar)", "Godoy Cruz (Argentina ar)",
    "Huracán (Argentina ar)", "Independiente (Argentina ar)", "Independiente Rivadavia (Argentina ar)", "Instituto Córdoba (Argentina ar)",
    "Lanús (Argentina ar)", "Newell's (Argentina ar)", "Platense (Argentina ar)", "Racing Club (Argentina ar)", "River Plate (Argentina ar)",
    "Rosario Central (Argentina ar)", "San Lorenzo (Argentina ar)", "Sarmiento (Argentina ar)", "Talleres (Argentina ar)", "Tigre (Argentina ar)",
    "Unión (Argentina ar)", "Vélez Sarsfield (Argentina ar)",

    # Australia
    "Adelaide United (Australia au)", "Brisbane Roar (Australia au)", "Central Coast Mariners (Australia au)", "Macarthur FC (Australia au)",
    "Melbourne City (Australia au)", "Newcastle Jets (Australia au)", "Perth Glory (Australia au)", "Sydney FC (Australia au)",
    "Wellington Phoenix (Australia au)", "Western Sydney Wanderers (Australia au)", "Western United (Australia au)",

    # Austria
    "FC Austria Klagenfurt (Austria at)", "Blau-Weiß (Austria at)", "FC Red Bull Salzburg (Austria at)", "FK Austria Viena (Austria at)",
    "Grazer AK (Austria at)", "LASK (Austria at)", "SCR Altach (Austria at)", "SK Rapid Viena (Austria at)", "SK Sturm Graz (Austria at)",
    "TSV Hartberg (Austria at)", "Wolfsberger AC (Austria at)", "WSG Tirol (Austria at)",

    # Bélgica
    "Beerschot (Bélgica be)", "Cercle Brugge (Bélgica be)", "Charleroi (Bélgica be)", "Club Brugge (Bélgica be)", "Dender EH (Bélgica be)",
    "Genk (Bélgica be)", "Gante (Bélgica be)", "Kortrijk (Bélgica be)", "Lovaina (Bélgica be)", "Mechelen (Bélgica be)", "Royal Antwerp FC (Bélgica be)",
    "RSC Anderlecht (Bélgica be)", "Sint-Truiden (Bélgica be)", "Standard Liege (Bélgica be)", "Union SG (Bélgica be)", "Westerlo (Bélgica be)",

    # China
    "Beijing Sinobo Guoan (China cn)", "Cangzhou Lions (China cn)", "Changchun Yatai (China cn)", "Chengdu Rongcheng (China cn)",
    "Henan Jianye (China cn)", "Meizhou Hakka (China cn)", "Nantong Zhiyun (China cn)", "Qingdao Hainiu (China cn)", "Costa oeste de Qingdao (China cn)",
    "Shandong Luneng Taishan (China cn)", "Shanghai Groenlandia Shenhua (China cn)", "Puerto de Shanghai (China cn)", "Ciudad Shenzhen Peng (China cn)",
    "Tianjin TEDA (China cn)", "Tres ciudades de Wuhan (China cn)", "Zhejiang (China cn)",

    # Dinamarca
    "Aarhus GF (Dinamarca dk)", "Brøndby IF (Dinamarca dk)", "FC Copenhague (Dinamarca dk)", "Kolding IF (Dinamarca dk)", "AC Lyngby (Dinamarca dk)",
    "FC Midtjylland (Dinamarca dk)", "FC Nordsælland (Dinamarca dk)", "Randers FC (Dinamarca dk)", "Silkeborg IF (Dinamarca dk)",
    "Soenderjyske Football (Dinamarca dk)", "Vejle Boldklub (Dinamarca dk)", "Viborg FF (Dinamarca dk)",

    # Inglaterra (Premier League)
    "Arsenal (Inglaterra en)", "Aston Villa (Inglaterra en)", "Bournemouth (Inglaterra en)", "Brentford (Inglaterra en)",
    "Brighton & Hove Albion (Inglaterra en)", "Chelsea (Inglaterra en)", "Crystal Palace (Inglaterra en)", "Everton (Inglaterra en)",
    "Fulham (Inglaterra en)", "Ipswich Town (Inglaterra en)", "Leicester City (Inglaterra en)", "Liverpool (Inglaterra en)",
    "Manchester City (Inglaterra en)", "Manchester United (Inglaterra en)", "Newcastle United (Inglaterra en)", "Nottingham Forest (Inglaterra en)",
    "Southampton (Inglaterra en)", "Tottenham (Inglaterra en)", "West Ham (Inglaterra en)", "Wolverhampton (Inglaterra en)",

    # Inglaterra (Championship)
    "Blackburn Rovers (Inglaterra en)", "Bristol City (Inglaterra en)", "Burnley (Inglaterra en)", "Cardiff City (Inglaterra en)",
    "Coventry City (Inglaterra en)", "Derby County (Inglaterra en)", "Hull City (Inglaterra en)", "Leeds United (Inglaterra en)",
    "Luton Town (Inglaterra en)", "Middlesborough (Inglaterra en)", "Millwall (Inglaterra en)", "Norwich City (Inglaterra en)",
    "Oxford United (Inglaterra en)", "Plymouth Argyle (Inglaterra en)", "Portsmouth (Inglaterra en)", "Preston North End (Inglaterra en)",
    "Queens Park Rangers (Inglaterra en)", "Sheffield United (Inglaterra en)", "Sheffield Wednesday (Inglaterra en)", "Stoke City (Inglaterra en)",
    "Sunderland (Inglaterra en)", "Swansea City (Inglaterra en)", "Watford (Inglaterra en)", "West Bromwich Albion (Inglaterra en)",

    # Inglaterra (League One/Two)
    "Barnsley (Inglaterra en)", "Birmingham City (Inglaterra en)", "Blackpool (Inglaterra en)", "Bolton Wanderers (Inglaterra en)",
    "Bristol Rovers (Inglaterra en)", "Burton Albion (Inglaterra en)", "Cambridge United (Inglaterra en)", "Charlton Athletic (Inglaterra en)",
    "Crawley Town (Inglaterra en)", "Exeter City (Inglaterra en)", "Huddersfield Town (Inglaterra en)", "Leyton Orient (Inglaterra en)",
    "Lincoln City (Inglaterra en)", "Mansfield Town (Inglaterra en)", "Northampton Town (Inglaterra en)", "Peterborough United (Inglaterra en)",
    "Reading (Inglaterra en)", "Rotherham United (Inglaterra en)", "Shrewsbury Town (Inglaterra en)", "Stevenage (Inglaterra en)",
    "Stockport County (Inglaterra en)", "Wigan Athletic (Inglaterra en)", "Wrexham (Inglaterra en)", "Wycombe Wanderers (Inglaterra en)",

    # Inglaterra (League Two / Conference)
    "Accrington Stanley (Inglaterra en)", "Barrow (Inglaterra en)", "Bradford City (Inglaterra en)", "Bromley (Inglaterra en)",
    "Carlisle United (Inglaterra en)", "Cheltenham Town (Inglaterra en)", "Chesterfield (Inglaterra en)", "Colchester United (Inglaterra en)",
    "Crewe Alexandra (Inglaterra en)", "Doncaster Rovers (Inglaterra en)", "Fleetwood Town (Inglaterra en)", "Gillingham (Inglaterra en)",
    "Grimsby Town (Inglaterra en)", "Harrogate Town (Inglaterra en)", "Milton Keynes Dons (Inglaterra en)", "Morecambe (Inglaterra en)",
    "Newport County (Inglaterra en)", "Notts County (Inglaterra en)", "Port Vale (Inglaterra en)", "Salford City (Inglaterra en)",
    "Swindon Town (Inglaterra en)", "Tranmere Rovers (Inglaterra en)", "Walsall (Inglaterra en)", "AFC Wimbledon (Inglaterra en)",

    # Inglaterra (Fútbol femenino)
    "Chelsea (Inglaterra en)", "Arsenal (Inglaterra en)", "Aston Villa (Inglaterra en)", "Brighton & Hove Albion (Inglaterra en)",
    "Crystal Palace (Inglaterra en)", "Everton (Inglaterra en)", "Leicester City (Inglaterra en)", "Liverpool (Inglaterra en)",
    "Manchester City (Inglaterra en)", "Manchester United (Inglaterra en)", "Tottenham Hotspur (Inglaterra en)", "West Ham United (Inglaterra en)",

    # Francia
    "Angers SCO (Francia fr)", "AS Saint-Étienne (Francia fr)", "AS Monaco (Francia fr)", "Auxerre (Francia fr)", "Havre AC (Francia fr)",
    "LOSC Lille (Francia fr)", "Montpellier HSC (Francia fr)", "OGC Nice (Francia fr)", "Olympique de Marseille (Francia fr)", "FC Nantes (Francia fr)",
    "Olympique Lyonnais (Francia fr)", "PSG (Paris Saint Germain) (Francia fr)", "Racing Club de Lens (Francia fr)", "RC Strasbourg Alsace (Francia fr)",
    "Stade Brestois 29 (Francia fr)", "Stade de Reims (Francia fr)", "Stade Rennais FC (Francia fr)", "Toulouse FC (Francia fr)",

    # Francia (Segunda)
    "AC Ajaccio (Francia fr)", "Amiens SC (Francia fr)", "Clermont Foot (Francia fr)", "Dunkerque (Francia fr)", "En Avant Guingamp (Francia fr)",
    "FC Annecy (Francia fr)", "FC Lorient (Francia fr)", "FC Martigues (Francia fr)", "FC Metz (Francia fr)", "Girondins de Bordeaux (Francia fr)",
    "Grenoble Foot 38 (Francia fr)", "Laval (Francia fr)", "Paris FC (Francia fr)", "Pau FC (Francia fr)", "Red Star FC (Francia fr)",
    "Rodez Averyron (Francia fr)", "SC Bastia (Francia fr)", "SM Caen (Francia fr)",

    # Francia (Otros)
    "AS Saint-Étienne (Francia fr)", "Dijon (Francia fr)", "Fleury (Francia fr)", "Guingamp (Francia fr)", "Le Havre (Francia fr)",
    "Montpellier HSC (Francia fr)", "Nantes (Francia fr)", "Olympique Lyonnais (Francia fr)", "Paris FC (Francia fr)",
    "PSG (Paris Saint-Germain) (Francia fr)", "Stade de Reims (Francia fr)", "Estrasburgo (Francia fr)",

    # Alemania (Primera)
    "1899 Hoffenheim (Alemania de)", "Bayer Leverkusen (Alemania de)", "Bayern Munich (Alemania de)", "Borussia Dortmund (Alemania de)",
    "Borussia Mönchengladbach (Alemania de)", "Eintracht Frankfurt (Alemania de)", "FC Augsburg (Alemania de)", "FC Heidenheim (Alemania de)",
    "Holstein Kiel (Alemania de)", "Mainz 05 (Alemania de)", "RB Leipzig (Alemania de)", "SC Freiburg (Alemania de)", "SC St. Pauli (Alemania de)",
    "Union Berlin (Alemania de)", "VfB Stuttgart (Alemania de)", "VfL Bochum (Alemania de)", "VfL Wolfsburg (Alemania de)", "Werder Bremen (Alemania de)",

    # Alemania (Segunda)
    "Darmstadt 98 (Alemania de)", "Eintracht Braunschweig (Alemania de)", "SV Elversberg (Alemania de)", "FC Kaiserslautern (Alemania de)",
    "FC Colonia (Alemania de)", "FC Nuremberg (Alemania de)", "Fortuna Düsseldorf (Alemania de)", "Greuther Fürth (Alemania de)", "Hamburger SV (Alemania de)",
    "Hannover 96 (Alemania de)", "Hertha BSC (Alemania de)", "Jahn Regensburg (Alemania de)", "Karlsruher SC (Alemania de)", "Preußen Münster (Alemania de)",
    "SC Paderborn (Alemania de)", "Schalke 04 (Alemania de)", "SSV Ulm (Alemania de)",

    # Alemania (Tercera)
    "Alemannia Aachen (Alemania de)", "Arminia Bielefeld (Alemania de)", "FC Saarbrücken (Alemania de)", "Borussia Dortmund II (Alemania de)",
    "Dynamo Dresden (Alemania de)", "Energie Cottbus (Alemania de)", "Erzgebirge Aue (Alemania de)", "FC Ingolstadt 04 (Alemania de)",
    "FC Viktoria Colonia (Alemania de)", "Hannover 96 II (Alemania de)", "Hansa Rostock (Alemania de)", "Rot-Weiss Essen (Alemania de)",
    "SC Verl (Alemania de)", "SpVgg Unterhaching (Alemania de)", "SV Sandhausen (Alemania de)", "SV Waldhof Mannheim (Alemania de)",
    "TSV 1860 Múnich (Alemania de)", "VfB Stuttgart II (Alemania de)", "VfL Osnabrück (Alemania de)", "Wehen Wiesbaden (Alemania de)",

    # Alemania (Otros)
    "1899 Hoffenheim (Alemania de)", "Bayer Leverkusen (Alemania de)", "Bayern Munich (Alemania de)", "Carl Zeiss Jena (Alemania de)",
    "Eintracht Frankfurt (Alemania de)", "FC Colonia (Alemania de)", "SC Freiburg (Alemania de)", "RB Leipzig (Alemania de)",
    "Rot-Weiss Essen (Alemania de)", "Turbine Potsdam (Alemania de)", "VfL Wolfsburg (Alemania de)", "Werder Bremen (Alemania de)",

    # India
    "ATK Mohun Bagan (India in)", "Bengaluru (India in)", "Chennai (India in)", "Bengala Oriental (India in)", "Goa (India in)",
    "Hyderabad (India in)", "Jamshedpur (India in)", "Kerala Blasters (India in)", "Mohammedan (India in)", "Mumbai City (India in)",
    "NorthEast United (India in)", "Odisha (India in)", "RoundGlass Punjab (India in)",

    # Irlanda
    "Bohemians (Irlanda ie)", "Derry City (Irlanda ie)", "Drogheda (Irlanda ie)", "Dundalk (Irlanda ie)", "Galway United (Irlanda ie)",
    "Shamrock Rovers (Irlanda ie)", "Sligo Rovers (Irlanda ie)", "Shelbourne (Irlanda ie)", "St Patrick's Athletic (Irlanda ie)", "Waterford (Irlanda ie)",

    # Italia (Serie A)
    "Bolonia (Italia it)", "Cagliari (Italia it)", "Como (Italia it)", "Empoli (Italia it)", "Fiorentina (Italia it)", "Génova (Italia it)",
    "Hellas Verona (Italia it)", "Juventus (Italia it)", "Lecce (Italia it)", "AC Monza (Italia it)", "Parma (Italia it)", "Turín (Italia it)",
    "Udinese (Italia it)", "Venecia (Italia it)", "Nápoles (Italia it)", "AS Roma (Italia it)",

    # Italia (Serie B)
    "Bari (Italia it)", "Catanzaro (Italia it)", "Cesena (Italia it)", "Citadella (Italia it)", "Cosenza (Italia it)", "Cremonese (Italia it)",
    "Frosione (Italia it)", "Juve Stabia (Italia it)", "Mantua (Italia it)", "Módena (Italia it)", "Palermo (Italia it)", "Pisa (Italia it)",
    "Reggina (Italia it)", "Reggiana (Italia it)", "Salermitana (Italia it)", "Sampdoria (Italia it)", "Sassuolo (Italia it)", "Spezia (Italia it)",
    "Tirol del Sur (Italia it)",

    # Corea del Sur
    "Daegu FC (Corea kr)", "Daejeon Hana Citizen (Corea kr)", "FC Seúl (Corea kr)", "Gangwon FC (Corea kr)", "Gimcheon Sangmu (Corea kr)",
    "Gwangju FC (Corea kr)", "Incheon United (Corea kr)", "Jeonbuk Hyundai Motors (Corea kr)", "Jeju United (Corea kr)", "Pohang Steelers (Corea kr)",
    "Suwon FC (Corea kr)", "Ulsan Hyundai (Corea kr)",

    # Holanda
    "Ajax (Holanda nl)", "Almere City (Holanda nl)", "AZ (Holanda nl)", "FC Utrecht (Holanda nl)", "Feyenoord (Holanda nl)", "Fortuna Sittard (Holanda nl)",
]


def equiporandom1():
    return random.sample(equiposenv, 2)



@bot.command()
async def equipos(ctx):
    equiposrandom,equiposrandom2 = equiporandom1()
    await ctx.send(f'El equipo 1 es {equiposrandom} y El equipo 2 es {equiposrandom2}')

#Close-TEAM-Command

#----------------------------------

#Open-WIKIPEDIA-Command

# Configuration of the wikipedia API, in spanish version 0.2.6.0.3.2.0.2.5
for openport in range(230499):
    for port_designed in range(2):
        mask = 255.255

wiki_wiki = wikipediaapi.Wikipedia(
    language='es',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='MyDiscordBot/1.0 (https://example.com/contact)'
)

@bot.command()    #Command wiki
async def wiki(ctx, *,search):
    page = wiki_wiki.page(search)
    if page.exists():
        summary = page.summary
        if len(summary) > 2000:
            chunks = [summary[i:i+2000] for i in range(0, len(summary), 2000)]
            for chunk in chunks:
                await ctx.send(chunk)
        else:
            await ctx.send(f"**{page.title}**\n\n{summary}\n\nLeer más: {page.fullurl}")
    else:
        await ctx.send("No se encontró ninguna página con ese título en Wikipedia.")

#Close-WIKIPEDIA-Command


#Open-EQUIPOSX-Command
equipos1estr = [
    "India (India) 🇮🇳",
    "Nueva Zelanda (New Zealand) 🇳🇿",
    "Islas Feroe (Faroe Islands) 🇫🇴",
    "Vietnam (Vietnam) 🇻🇳",
    "Andorra (Andorra) 🇦🇩",
    "San Marino (San Marino) 🇸🇲",
    "Liechtenstein (Liechtenstein) 🇱🇮",
    "Gibraltar (Gibraltar) 🇬🇮",
    "Malasia (Malaysia) 🇲🇾",
    "China Taipéi (Chinese Taipei) 🇹🇼",
    "Maldivas (Maldives) 🇲🇻",
    "Nepal (Nepal) 🇳🇵",
    "Camboya (Cambodia) 🇰🇭",
    "Laos (Laos) 🇱🇦",
    "Sri Lanka (Sri Lanka) 🇱🇰"
]
equipos2estr = [
    "Bolivia (Bolivia) 🇧🇴",
    "Venezuela (Venezuela) 🇻🇪",
    "El Salvador (El Salvador) 🇸🇻",
    "Honduras (Honduras) 🇭🇳",
    "Congo (Congo) 🇨🇬",
    "Cuba (Cuba) 🇨🇺",
    "Guatemala (Guatemala) 🇬🇹",
    "Kazajistán (Kazakhstan) 🇰🇿",
    "Luxemburgo (Luxembourg) 🇱🇺",
    "Nicaragua (Nicaragua) 🇳🇮",
    "Etiopía (Ethiopia) 🇪🇹",
    "Mozambique (Mozambique) 🇲🇿",
    "Tanzania (Tanzania) 🇹🇿",
    "Zambia (Zambia) 🇿🇲",
    "Guinea (Guinea) 🇬🇳"
]
equipos3estr = [
    "Irán (Iran) 🇮🇷",
    "Nigeria (Nigeria) 🇳🇬",
    "Uruguay (Uruguay) 🇺🇾",
    "Perú (Peru) 🇵🇪",
    "Camerún (Cameroon) 🇨🇲",
    "Bosnia y Herzegovina (Bosnia and Herzegovina) 🇧🇦",
    "Jordania (Jordan) 🇯🇴",
    "Rumanía (Romania) 🇷🇴",
    "Ecuador (Ecuador) 🇪🇨",
    "República Checa (Czech Republic) 🇨🇿",
    "Noruega (Norway) 🇳🇴",
    "Suecia (Sweden) 🇸🇪",
    "Serbia (Serbia) 🇷🇸",
    "Paraguay (Paraguay) 🇵🇾",
    "Kenia (Kenya) 🇰🇪"
]
equipos4estr = ["Pingudo4","Pinga4"]

equipos5estr = ["Pingudo5","Pinga5"]

#Función para seleccionar los equipos basados en el número
def equipos_x():
    unoalcinco = random.choice([1, 2, 3, 4, 5])  # Selecciona un número al azar entre 1 y 5
    if unoalcinco == 1:
        equipos = random.sample(equipos1estr, 2)
    elif unoalcinco == 2:
        equipos = random.sample(equipos2estr, 2)
    elif unoalcinco == 3:
        equipos = random.sample(equipos3estr, 2)
    elif unoalcinco == 4:
        equipos = random.sample(equiposenv, 2)
    elif unoalcinco == 5:
        equipos = random.sample(equiposenv, 2)
    return unoalcinco, equipos

@bot.command()
async def equiposx(ctx):
    numero, equipos = equipos_x()  # Elige un numero y los equipos correspondientes
    await ctx.send(f'La cantidad de estrellas para sus equipos son: {numero} ⭐️')
    time.sleep(5)
    await ctx.send(f'Los equipos son {equipos[0]} y {equipos[1]}')


#Close-EQUIPOSX-Command
@bot.command()
async def fifa(ctx, nombre1: str, nombre2: str):
    #Selecciona al azar quién va primero
    primero = random.choice([nombre1, nombre2])
    segundo = nombre2 if primero == nombre1 else nombre1

    #Selecciona equipos diferentes para cada jugador
    equipo1 = random.choice(equiposenv)
    equipo2 = random.choice([e for e in equiposenv if e != equipo1])

    #Envia el mensaje
    mensaje = (
        f"⚽ **{primero.title()}** juega con **{equipo1}**\n"
        f"⚽ **{segundo.title()}** juega con **{equipo2}**"
    )
    await ctx.send(mensaje)


#Close-fifa-command



"""
#INICIO WALL RAND
def wallrand():
    return random.choice(["Veigar", "Mordekaiser", "Heimerdinguer"])

@bot.command()
async def wallpapers(ctx):
    campeon = wallrand()  # Llamamos a la función wallrand
    await ctx.send(f"El wallpaper aleatorio es de: {campeon}")
    time.sleep(3)

    if campeon == "Veigar":
        file = discord.File("C:\\Users\\Agu\\Desktop\\Discord_BOT_Python\\wallpapapers_lol\\veigar\\v1.jpeg")
        await ctx.send(file=file)

    elif campeon == "Mordekaiser":
        file = discord.File("C:\\Users\\Agu\\Desktop\\Discord_BOT_Python\\wallpapapers_lol\\mordekaiser\\1morde.jpeg")
        await ctx.send(file=file)

    elif campeon == "Heimerdinguer":
        file = discord.File("C:\\Users\\Agu\\Desktop\\Discord_BOT_Python\\wallpapapers_lol\\heimer\\1heimer.jpg")
        await ctx.send(file=file)

"""

#Open-CSMAP-Command

mapas_competitivos_cs2 = [
    "Mirage 🕌", "Inferno 🏰", "Nuke ☢️", "Train 🚂", "Dust II 🌵",
    "Ancient 🌲", "Anubis 🏺"
]

def maparandomcs():
    return random.choice(mapas_competitivos_cs2)

@bot.command()
async def csmap(ctx):
    maparandom = maparandomcs()
    await ctx.send(f"El mapa que tocó es: {maparandom} ")

#Close-CSMAP-Command

bot.run("Api discord run")

