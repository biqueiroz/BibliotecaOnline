from django import template
from datetime import datetime

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    # este é uma forma de fazer
    #if isinstance(value1, datetime) and isinstance(value2, datetime):
    #    return (value1 - value2).days
    #return " Ainda emprestado"
    # este é uma outra forma de fazer
    if all((isinstance(value1, datetime), isinstance(value2, datetime))):
        dias = (value1 - value2).days
        texto = 'Dias'
        if dias == 1:
            texto = 'Dia'
        return f"{dias} {texto}."
    return " Ainda emprestado."