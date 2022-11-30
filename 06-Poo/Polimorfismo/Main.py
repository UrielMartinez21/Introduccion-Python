# Polimorfismo = Las clases heredadas puedes sobreescribir metodos del padre
from Persona import Persona,Atleta,Ciclista

persona=Persona("Alex")
persona.moverse()

atleta=Atleta("Juan")
atleta.moverse()

ciclista=Ciclista("Pedro")
ciclista.moverse()