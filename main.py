from fastapi import FastAPI

app = FastAPI(title="API Paludarium Connecté")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API du Paludarium !"}

# Route qui simule les relevés des capteurs en temps réel
@app.get("/api/capteurs/live")
def get_donnees_capteurs():
    return {
        "temperature_air": 25.5,
        "humidite": 82.0,
        "niveau_eau": "Normal",
        "temperature_eau": 24.0,
        "luminosite": 800
    }