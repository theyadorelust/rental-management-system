from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Canon Camera",
        "category": "Photography",
        "price_per_day": 500,
        "quantity": 3
    },
    {
        "id": 2,
        "name": "Projector",
        "category": "Electronics",
        "price_per_day": 800,
        "quantity": 2
    },
    {
        "id": 3,
        "name": "Mountain Bike",
        "category": "Sports",
        "price_per_day": 400,
        "quantity": 5
    }
]


@app.route("/")
def home():
    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)