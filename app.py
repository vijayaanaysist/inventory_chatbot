from flask import Flask, request, jsonify
from inventory import get_stock, low_stock_items, get_supplier, reorder_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "Inventory Chatbot API is running!"@app.route("/chat", methods=["POST"])
def webhook():
    req = request.get_json()

    intent = req.get("queryResult", {}).get("intent", {}).get("displayName", "")
    text = req.get("queryResult", {}).get("queryText", "").lower()

    print("Intent:", intent)
    print("Text:", text)

    # Extract item name (simple logic)
    item = text.replace("how many", "").replace("stock", "").replace("supplier for", "").strip()

    if intent == "Check_Stock":
        response = get_stock(item)

    elif intent == "Low_Stock":
        response = str(low_stock_items())

    elif intent == "Supplier_Info":
        response = str(get_supplier(item))

    elif intent == "Reorder_Items":
        response = str(reorder_alert().to_dict(orient="records"))

    else:
        response = "Not available"

    return jsonify({
        "fulfillmentText": response
    })