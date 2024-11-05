from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "chocolate_house.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/flavors", methods=["POST"])
def add_flavor():
    data = request.json
    query_db("INSERT INTO seasonal_flavors (flavor_name, start_date, end_date) VALUES (?, ?, ?)",
             (data["flavor_name"], data.get("start_date"), data.get("end_date")))
    return jsonify({"message": "Flavor added!"}), 201

@app.route("/flavors", methods=["GET"])
def list_flavors():
    flavors = query_db("SELECT * FROM seasonal_flavors")
    return jsonify(flavors), 200

@app.route("/inventory", methods=["POST"])
def add_ingredient():
    data = request.json
    query_db("INSERT INTO ingredient_inventory (ingredient_name, quantity, unit) VALUES (?, ?, ?)",
             (data["ingredient_name"], data["quantity"], data["unit"]))
    return jsonify({"message": "Ingredient added!"}), 201

@app.route("/inventory", methods=["GET"])
def list_ingredients():
    ingredients = query_db("SELECT * FROM ingredient_inventory")
    return jsonify(ingredients), 200

@app.route("/suggestions", methods=["POST"])
def add_suggestion():
    data = request.json
    query_db("INSERT INTO customer_suggestions (customer_name, suggested_flavor, allergy_concerns) VALUES (?, ?, ?)",
             (data["customer_name"], data["suggested_flavor"], data.get("allergy_concerns")))
    return jsonify({"message": "Suggestion added!"}), 201

@app.route("/suggestions", methods=["GET"])
def list_suggestions():
    suggestions = query_db("SELECT * FROM customer_suggestions")
    return jsonify(suggestions), 200

if __name__ == "__main__":
    app.run(debug=True)
