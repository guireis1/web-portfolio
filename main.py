from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/portfolio1")
def portifolio1():
    return render_template("portfolio-item1.html")

@app.route("/portfolio2")
def portifolio2():
    return render_template("portfolio-item2.html")

@app.route("/portfolio3")
def portifolio3():
    return render_template("portfolio-item3.html")

@app.route("/portfolio4")
def portifolio4():
    return render_template("portfolio-item4.html")

@app.route("/portfolio5")
def portifolio5():
    return render_template("portfolio-item5.html")

@app.route("/portfolio6")
def portifolio6():
    return render_template("portfolio-item6.html")
    
if __name__ == "__main__":
    app.run(debug=True)