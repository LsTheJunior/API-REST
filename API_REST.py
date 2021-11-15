
from flask import Flask, jsonify, request
from pydantic import BaseModel
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from tinydb import TinyDB, database, Query
from typing import Optional


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='API teste')
spec.register(server)
database = TinyDB('database.json')

class pessoa(BaseModel):
    id: Optional[int]
    nome: str
    idade: str

@server.get('/pessoas')
#@spec.validate(resp=Response(HTTP_200=pessoa))
def buscar_pessoas():
    """Retorna todas as pessoas da base de dados"""
    return jsonify(database.all())

@server.post('/pessoas') 
@spec.validate(body=Request(pessoa), resp=Response(HTTP_200=pessoa))  
def inserir_pessoa():
    """Insere uma pessoa no banco de dados"""
    body = request.context.body.dict()
    return body


server.run()
