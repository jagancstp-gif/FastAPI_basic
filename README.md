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
