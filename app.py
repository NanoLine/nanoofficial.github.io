from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
    return render_template("home.html")
@app.route('/about')
def About():
    return render_template("about.html")
@app.route('/contact')
def Contact():
    return render_template("contact.html")
@app.route('/purchase')
def Purchase():
    return render_template("purchase.html")

if(__name__=="__main__"):
    app.run()