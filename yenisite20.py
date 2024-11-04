from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/arın">bu butona basarak en iyi siteye gidebilirsin</a> <a href="/safir">bu butona basarak en iyi siteye gidebilirsin</a>'

@app.route("/arın")
def arın():
    return '<h1>1-0</h1> <a href="/">bu butona basarak en iyi siteye gidebilirsin</a>'

liste = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]


@app.route("/safir")
def safir():
    return  f'<h1> {random.choice(liste)} </h1>'

@app.route("/<x>")
def yazim(x):
    yazi_tura=["yazi","tura"]
    yt = random.choice(yazi_tura)
    if yt== x:
        return '<h1>Bildin</h1>'
    else:
        return '<h1>Bilemedin</h1>'




app.run(debug=True)
