from flask import Flask, request, jsonify
from inventory import get_stock, low_stock_items, get_supplier, reorder_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "Inventory Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "").lower()

    if "stock" in msg:
        item = msg.replace("how many", "").replace("stock", "").strip()
        return jsonify({"response": get_stock(item)})

    elif "low" in msg:
        items = low_stock_items()
        return jsonify({"response": items if items else "No low stock items"})

    elif "reorder" in msg:
        return jsonify({"response": reorder_alert().to_dict(orient="records")})

    elif "supplier" in msg:
        item = msg.replace("supplier for", "").strip()
        return jsonify({"response": get_supplier(item)})

    else:
        return jsonify({"response": "I can help with stock, low stock, reorder, or suppliers."})

if __name__ == "__main__":
    app.run(debug=True)