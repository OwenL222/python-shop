from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import json
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-this")
Session(app)

# Sample product data (in a real app, this would come from a database)
products = [
    {"id": 1, "name": "Product 1", "price": 19.99, "description": "Description for Product 1"},
    {"id": 2, "name": "Product 2", "price": 29.99, "description": "Description for Product 2"},
    {"id": 3, "name": "Product 3", "price": 39.99, "description": "Description for Product 3"},
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 