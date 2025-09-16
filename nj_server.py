print(">>> Running from:", __file__)


from fastapi import FastAPI, HTTPException

catalog = {
    "tomato": {
        "units": "boxes",
        "qty": 1000
    },
    "wine": {
        "units": "bottles",
        "qty": 500
    },
    "beans": {
        "units": "bags",
        "qty": 500
    }
}

app = FastAPI(title="New Jersey API server") # This is the API server

@app.get("/warehouse/{product}")
async def load_truck(product: str, order_qty: int):

    available_qty = catalog[product]["qty"]

    if int(order_qty) > int(available_qty):
        raise HTTPException(
            status_code=400,
            detail=f"Sorry, only {available_qty} units are available. Please try again."
        )

    catalog[product]["qty"] -= int(order_qty)

    return {
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product]["units"],
        "remaining_qty": catalog[product]["qty"]
    }

# the code to be used for the command line is as follows:
# unicorn <fastapi python file name>:app --reload --host 0.0.0.0 --port 8000
# The --reload flag is to ensure the webpage reloads everytime we change the code in the
# fastapi python file.
