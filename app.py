from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        city = request.form["city"]

        return render_template(
            "result44.html",
            name=name,
            city=city
        )

    return render_template("index44.html")

if __name__ == "__main__":
    app.run(debug=True)
