#Importierungen
import discord

#Variabeln:
call_option = "b!"# Womit der Bot angesprochen werden soll

def run_bot():
    """Startet den Bot"""
    global client

    intents = discord.Intents.default()  
    intents.message_content = True
    client = discord.Client(intents = intents)

run_bot()

@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_message(message):
    """Eine Nachricht wird gepostet. Im folgenden Überprüft der Bot verschiedene Fälle und führt, wenn es gefordert ist, Aktionen aus."""

    if message.author == client.user:#Nachricht vom Bot
        return#Nicht auf eigene Nachricht reagieren
    
    #Hilfefunktion:
    if message.content.startswith(call_option + "help"):
        await message.channel.send("**Help Information:**")#Help Information müssen noch ergänzt werden


    #Funktionen des Bots:

    #BWINF Zeug erklären
    if message.content.startswith(call_option + "explain 1. Runde"):
        await message.channel.send("Hm hab grad kein Bock das alles zu schreiben, guck ma auf https://bwinf.guide/bwinf/hints/round1 vorbei.")
    
    if message.content.startswith(call_option + "explain 2. Runde"):
        await message.channel.send("Boah, lass mich überlegen... Am besten du guckst bei https://bwinf.guide/bwinf/hints/round2 nach...")
    
    #Freundlich sein:
    if message.content.lower() == "hi" or "hallo":
        await message.channel.send("Hi!")

def ask_token():
    """Lol wusste nicht wie ich es sonst lösen soll..."""
    return input("TOKEN:\n")

token = ask_token()
client.run(token)
    

    