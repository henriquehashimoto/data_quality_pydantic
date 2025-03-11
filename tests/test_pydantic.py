from datetime import date
from pydantic import BaseModel, PositiveInt, validate_call

# Cria a validação como uma classe com os tipos obrigatórios
class Delivery(BaseModel):
    timestamp: date
    dimensions: tuple[int, int]

# Chamando minha classe com os valores que irei passar para testar se esta correto
m = Delivery(timestamp='2025-02-02', dimensions=['10', '20'])
print(m)


#============================
# Testando argumentos e retorno de função
#============================
class NumPositivo(BaseModel):
    numero: PositiveInt

@validate_call(validate_return=True)
def calc(x: NumPositivo, y: NumPositivo) -> NumPositivo:
    return NumPositivo(numero=x.numero + y.numero)

# Criando instâncias de NumPositivo para passar à função
x = NumPositivo(numero=3)
y = NumPositivo(numero=5)
print(calc(x, y))