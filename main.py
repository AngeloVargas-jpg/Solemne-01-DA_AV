from datetime import datetime

import ntplib
from fastapi import FastAPI

app = FastAPI()


@app.get("/time")
def get_time():
    try:
        client = ntplib.NTPClient()
        # Servidor oficial de SHOA
        response = client.request("ntp.shoa.cl", version=3)

        fecha_hora = datetime.fromtimestamp(response.tx_time)
        salida = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

        return {"Hora_Oficial_Chile": salida}
    except Exception as e:
        return {"error": f"No se pudo obtener la hora desde NTP: {e}"}