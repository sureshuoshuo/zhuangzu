from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/Wordcloud.html')
def Wordcloud():  # put application's code here
    return render_template("Wordcloud.html")

@app.route('/topic.html')
def topic():  # put application's code here
    return render_template("topic.html")

@app.route('/feeling.html')
def feeling():  # put application's code here
    return render_template("feeling.html")

@app.route('/network.html')
def network():  # put application's code here
    return render_template("network.html")

if __name__ == '__main__':
    app.run()
