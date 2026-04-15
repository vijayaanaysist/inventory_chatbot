import pandas as pd

df = pd.read_csv("inventory.csv")

def get_stock(item):
    result = df[df["item_name"].str.lower() == item.lower()]
    if not result.empty:
        qty = int(result["quantity"])
        return f"{item} stock available: {qty}"
    return "Item not found"

def low_stock_items():
    low = df[df["quantity"] <= df["threshold"]]
    return low[["item_name", "quantity", "threshold"]].to_dict(orient="records")

def get_supplier(item):
    result = df[df["item_name"].str.lower() == item.lower()]
    if not result.empty:
        return {
            "supplier": result["supplier"].values[0],
            "contact": result["contact"].values[0]
        }
    return "Supplier not found"

def reorder_alert():
    df["reorder_needed"] = df["quantity"] <= df["threshold"]
    return df[df["reorder_needed"] == True]