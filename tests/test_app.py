import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from app import app


def test_pagina_inicial():

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200

    assert b"TechFlow Solutions" in resposta.data