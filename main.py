# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
import csv

app = FastAPI()

@app.get("/save")
async def save_data(param1: str, param2: str, param3: str, param4: str, param5: str):
    # Guardar los parámetros en un archivo CSV
    with open("data.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([param1, param2, param3, param4, param5])

    return {"message": "Datos recibidos y guardados en CSV."}

@app.get("/show")
async def show_data():
    try:
        with open("data.csv", mode="r") as file:
            return PlainTextResponse(file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

