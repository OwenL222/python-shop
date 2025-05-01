from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import json
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-this")
Session(app)

# Product catalog
products = [
    {
        "id": 1,
        "name": "Premium Coffee Beans",
        "price": 24.99,
        "description": "Freshly roasted Arabica coffee beans from Colombia, 1lb bag"
    },
    {
        "id": 2,
        "name": "Organic Green Tea",
        "price": 18.99,
        "description": "High-quality Japanese Sencha green tea, 50 tea bags"
    },
    {
        "id": 3,
        "name": "Artisan Chocolate Bar",
        "price": 9.99,
        "description": "72% dark chocolate bar made with single-origin cacao"
    },
    {
        "id": 4,
        "name": "Gourmet Cookie Set",
        "price": 15.99,
        "description": "Assorted handmade cookies, pack of 12"
    },
    {
        "id": 5,
        "name": "Natural Honey",
        "price": 12.99,
        "description": "Raw, unfiltered wildflower honey, 16oz jar"
    }
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        session["cart"].append(product)
        session.modified = True
    return redirect(url_for("index"))

@app.route("/cart")
def view_cart():
    cart = session.get("cart", [])
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):
    if "cart" in session and 0 <= index < len(session["cart"]):
        session["cart"].pop(index)
        session.modified = True
    return redirect(url_for("view_cart"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port) 