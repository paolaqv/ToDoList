# app/gestion_tareas.py
from .modelo_tareas import Tarea
from datetime import datetime

class GestionTareas:
    def __init__(self):
        self.tareas = []
        self.ultimo_id = 0
    
    def agregar_tarea(self, descripcion, fecha_inicio_str):
        self.ultimo_id += 1
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')  # Convertir string a datetime
        tarea = Tarea(self.ultimo_id, descripcion, fecha_inicio)
        self.tareas.append(tarea)
        return tarea
    
    def eliminar_tarea(self, id):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id]
    
    def marcar_completada(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.completada = not tarea.completada
                return tarea
        return None

    def modificar_tarea(self, id, nueva_descripcion, nueva_fecha_inicio):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.descripcion = nueva_descripcion
                tarea.fecha_inicio = datetime.strptime(nueva_fecha_inicio, '%Y-%m-%d')
                return tarea
        return None
    
    def obtener_tareas(self, completadas=None):
        if completadas is None:
            return self.tareas
        else:
            return [tarea for tarea in self.tareas if tarea.completada == completadas]
        
    def obtener_tarea_por_id(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea
        return None



# Crea una instancia de GestionTareas aquí
gestor = GestionTareas()