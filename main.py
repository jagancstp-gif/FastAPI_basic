"""
main.py
========
A minimal FastAPI app with two endpoints:

    GET /              -> a simple welcome JSON message
    GET /greet/{name}  -> greets whoever's name is passed in the URL path

RUN IT
------
    pip install fastapi uvicorn
    uvicorn main:app --reload

Then open:
    http://127.0.0.1:8000/                -> root welcome message
    http://127.0.0.1:8000/greet/Jagan     -> path-parameter greeting
    http://127.0.0.1:8000/docs            -> interactive Swagger UI docs
"""

from fastapi import FastAPI

app = FastAPI(title="Greeting API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to GEN AI learning!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Nice to meet you."}


#if __name__ == "__main__":
    # Allows running directly with `python main.py` as an alternative to
    # the `uvicorn main:app --reload` command.
 #   import uvicorn
  #  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)