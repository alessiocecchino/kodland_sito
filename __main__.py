from flask import Flask
import random
from funzioni import gen_password, lancio_moneta
lista_fatti = [
    "La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi",
    f"Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone",
    "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna",
    f"Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro.",
    "Un modo per combattere la dipendenza tecnologica è cercare attività che portino piacere e migliorino l'umore",
    "Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti",
    "Elon Musk è anche favorevole alla regolamentazione dei social network e alla protezione dei dati personali degli utenti. Sostiene che i social network raccolgono un'enorme quantità di informazioni su di noi, che possono essere utilizzate per manipolare i nostri pensieri e comportamenti",
    "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme"
]   

app = Flask(__name__)
@app.route("/")
def home():
    return open("home.html")
@app.route("/random_facts")
def fatti_curiosi():
    return open("random_facts.html").read().format(fatto=random.choice(lista_fatti))

@app.route("/password_generator")
def password_generator():
    password = gen_password()
    return open("password_generator.html").read().format(password=password)

@app.route("/lancio_moneta")
def moneta():
    moneta = lancio_moneta()
    return open("lancio_moneta.html").read().format(moneta=moneta)

@app.route("/random_image")
def random_image():
    return open("random_image.html")

app.run(debug=True)