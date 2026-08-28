
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
