
from flask import Flask
from pydantic import BaseModel
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from werkzeug.wrappers import request


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='API teste')
spec.register(server)

class pessoa(BaseModel):
    id: int
    nome: str
    idade: str

@server.get('/pessoas')
#@spec.validate(resp=Response(HTTP_200=pessoa))
def pegar_pessoas():
    return 'Programaticamente Falando'

@server.post('/pessoas') 
@spec.validate(body=Request(pessoa), resp=Response(HTTP_200=pessoa))  
def inserir_pessoa():
    """Insere uma pessoa no banco de dados"""
    body = request.context.body.dict()
    return body


server.run()