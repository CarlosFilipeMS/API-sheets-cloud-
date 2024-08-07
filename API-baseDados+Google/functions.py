from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth import get_current_user
from google.oauth2.service_account import Credentials
import gspread
from fastapi.responses import JSONResponse


router = APIRouter()

class Pagina1(BaseModel):
    nome: str
    sobrenome: str
    cidade: str

class Pagina2(BaseModel):
    id_fixo: str
    orderld: str
    date: str


# Função normal que costumamos usar pra mandar dados, etc
@router.post("/compraswpp")
async def add(dados: Pagina1):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)
        client = gspread.authorize(credentials)
        sheet = client.open('nome_planilha').worksheet("nome_pagina")
        # PADRÃO -> NOME DA PLANILHA -> NOME DA PÁGINA
        data = [dados.nome, dados.sobrenome, dados.cidade]

        sheet.append_row(data)
    except Exception as error:
        return JSONResponse(content={"Error": str(error)}, status_code=400)
    else:
        return {"Success": "Nova linha adicionada"}
    

@router.post("/disparosRastreio")
async def add(dados: Pagina2):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)
        client = gspread.authorize(credentials)
        sheet = client.open('nome_planilha').worksheet("nome_pagina")
        # PADRÃO -> NOME DA PLANILHA -> NOME DA PÁGINA
        data = [dados.id_fixo, dados.orderld, dados.date]

        sheet.append_row(data)
    except Exception as error:
        return JSONResponse(content={"Error": str(error)}, status_code=400)
    else:
        return {"Success": "Nova linha adicionada"}
    