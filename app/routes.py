from flask import render_template, request, redirect, url_for
from app import app
from .gestion_tareas import gestor


@app.route('/')
def index():
    filtro = request.args.get('filtro', 'todas')
    
    if filtro == 'completadas':
        tareas = gestor.obtener_tareas(completadas=True)
    elif filtro == 'pendientes':
        tareas = gestor.obtener_tareas(completadas=False)
    else:
        tareas = gestor.obtener_tareas()
    
    return render_template('index.html', tareas=tareas)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha_inicio = request.form['fecha_inicio']
        gestor.agregar_tarea(descripcion, fecha_inicio)
        return redirect(url_for('index'))
    return render_template('agregar_tarea.html')


@app.route('/eliminar/<int:id>')
def eliminar(id):
    gestor.eliminar_tarea(id)
    return redirect(url_for('index'))


@app.route('/completar/<int:id>')
def completar(id):
    gestor.marcar_completada(id)
    return redirect(url_for('index'))


@app.route('/modificar/<int:id>', methods=['GET'])
def mostrar_modificar(id):
    tarea = gestor.obtener_tarea_por_id(id) 
    if tarea:
        return render_template('modificar_tarea.html', tarea=tarea)
    return redirect(url_for('index'))


@app.route('/modificar/<int:id>', methods=['POST'])
def procesar_modificar(id):
    nueva_descripcion = request.form['descripcion']
    nueva_fecha_inicio = request.form['fecha_inicio']
    gestor.modificar_tarea(id, nueva_descripcion, nueva_fecha_inicio)
    return redirect(url_for('index'))


