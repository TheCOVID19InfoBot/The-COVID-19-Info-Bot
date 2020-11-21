from flask import Flask
from threading import Thread

# keeps the bot running 24/7 (used with https://uptimerobot.com)
app = Flask('')

@app.route('/')
def home():
    return f'================================================================================= <br>Discord Bot Name: The COVID-19 Info Bot<br>Hosting Platform: Repl.it <br><br>Founder/Coder: Donald Lee<br>Researcher: Rosa Chen<br>Graphic Designer: Matthew Quock<br>Beta Tester and Feature Requestor: Kenny Kwan<br><br>For more information, check out: https://thecovid19infobot.github.io/index.html <br>================================================================================='
 
def run():
  app.run(host = '0.0.0.0', port = 8080)

def keepAlive():
    keep_alive_thread = Thread(target=run)
    keep_alive_thread.start()