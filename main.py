from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Servicio REST de Consulta de Cuenta",
    description="Servicio que expone la consulta de información básica de una cuenta bancaria de forma desacoplada.",
    version="1.0.0"
)


cuentas_mock = {
    "123456": {
        "cuenta": "123456",
        "titular": "Carlos Gómez",
        "saldo": 4250000,
        "estado": "activa",
        "moneda": "COP"
    },
    "789012": {
        "cuenta": "789012",
        "titular": "Laura Martínez",
        "saldo": 980000,
        "estado": "bloqueada",
        "moneda": "COP"
    }
}


@app.get("/")
def inicio():
    return {"mensaje": "Servicio REST de cuentas funcionando correctamente"}


@app.get(
    "/api/cuentas/{numero_cuenta}",
    tags=["Cuentas"],
    summary="Consultar cuenta",
    description="Consulta la información básica de una cuenta bancaria a partir de su número.",
    responses={
        200: {
            "description": "Consulta realizada correctamente"
        },
        404: {
            "description": "La cuenta no fue encontrada"
        }
    }
)
def consultar_cuenta(numero_cuenta: str):
    cuenta = cuentas_mock.get(numero_cuenta)

    if cuenta is None:
        raise HTTPException(
            status_code=404,
            detail=f"La cuenta {numero_cuenta} no fue encontrada"
        )

    return cuenta
