from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.

def query1(req):
    cursor = connection.cursor()
    cursor.execute("insert into main_curso (cod, nombre, activo) values ('RP5', 'Repostería', True)")
    return HttpResponse('listo')