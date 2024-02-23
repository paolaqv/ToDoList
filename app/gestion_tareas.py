#importacion de la clase tarea
from .modelo_tareas import Tarea
from datetime import datetime

#clase que manejara la gestion de tareas
class GestionTareas:
    #constructor de la clase
    def __init__(self):
        #lista donde se almacena las tareas
        self.tareas = []
        #variable para el ultimo id de una tarea
        self.ultimo_id = 0
    
    #metodo para agregar una tarea
    def agregar_tarea(self, descripcion, fecha_inicio_str):
        #asignamos un "id" a la nueva tarea de manera incremental
        self.ultimo_id += 1 
        #pasamos la fecha de string a datetime
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')  
        #la instancia encapsula la informacion de una tarea creda
        tarea = Tarea(self.ultimo_id, descripcion, fecha_inicio)
        #agregamos la tarea a la lista
        self.tareas.append(tarea)
        return tarea
    
    #metodo para obtener una tarea  por su "id"
    def obtener_tarea_por_id(self, id):
        #recorremos la lista
        for tarea in self.tareas:
            if tarea.id == id:
                return tarea #se devuelve la tarea
        return None #??
    
    def eliminar_tarea(self, id):
        #obtenemos la id de la tarea
        tarea = self.obtener_tarea_por_id(id)
        #si la obtenemos la tarea y no este completada
        if tarea and not tarea.completada:
            #generemos la nueva lista sin la tarea que elegimos
            self.tareas = [tarea for tarea in self.tareas 
                                     if tarea.id != id]
            return True  # Indica que la tarea se eliminó
        return False  
    
    #metodo que busca el id de la tarea, encuentra que es completada es "false"
    #y lo cambia a "true"
    def marcar_completada(self, id):
        for tarea in self.tareas:
            if tarea.id == id:
                #aqui
                tarea.completada = not tarea.completada
                return tarea
        return None

    #metodo para modificar una tarea donde se guardan las modificaciones de 
    #la tarea mediante su id
    def modificar_tarea(self, id, nueva_descripcion, nueva_fecha_inicio):
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.descripcion = nueva_descripcion
                tarea.fecha_inicio = datetime.strptime(nueva_fecha_inicio, '%Y-%m-%d')
                return tarea
        return None
    
    #metodo para el filtrado mediante el estado de la tarea
    def obtener_tareas(self, completadas=None):
        #sino se recibio ningun parametro en completadas
        if completadas is None:
            #entonces se devuelve todas las tareas completadas y pendientes
            return self.tareas
        else:
            #pero si tiene un valor true o false , 
            #entonces solo se devuelven las tareas con ese estado
            return [tarea for tarea in self.tareas 
                    if tarea.completada == completadas]
        
   



#instancia de GestionTareas para acceder a los metodos en routes.py
gestor = GestionTareas()