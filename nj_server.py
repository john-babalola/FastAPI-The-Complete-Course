from fastapi import FastAPI

catalog = {
    "tomato": {
        "units": "boxes",
        "qty": 1000
    },
    "wine": {
        "units": "bottles",
        "qty": 500
    }
}

app = FastAPI(title="New Jersey API server") # This is the API server

@app.get("/warehouse/{product}")
def load_truck(product, order_qty):
    return {
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product]["units"]
    }

