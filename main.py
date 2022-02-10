from flask import Flask
from threading import Thread
import nextcord
from flask import jsonify
from nextcord.ext import commands
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix = '?', intents=intents)
app = Flask('')
import os
@app.route('/')
def home():
    return "Hello. I am alive!"

@app.route('/vscode/<user_id>')
def vscode(user_id):
    member = bot.get_guild(941320065444360242).get_member(int(user_id))
    if member.activity.name.lower() == 'visual studio code':
        return jsonify(
            {
                "schemaVersion": 1,
                "label": "coding",
                "message": member.activity.state.split(': ')[1],
                "color": "blue"
            }
        )
    
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.command()
async def henlo(ctx):
    await ctx.send('hi')

keep_alive()
bot.run(os.environ['token'])