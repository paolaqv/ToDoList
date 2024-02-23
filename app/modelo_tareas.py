# app/modelo_tareas.py

from datetime import datetime  # Importamos datetime para trabajar con fechas

class Tarea:
    def __init__(self, id, descripcion, fecha_inicio, completada=False):
        self.id = id
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio  
        self.completada = completada
