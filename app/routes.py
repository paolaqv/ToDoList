#
from flask import render_template, request, redirect, url_for
from app import app
from .gestion_tareas import gestor


@app.route('/')
def index():
    # Obtenemos el parámetro 'filtro' de la URL,
    # si no existe, se usa 'todas' como predeterminado.
    filtro = request.args.get('filtro', 'todas')
     # Si el filtro es 'completadas', obtenemos solo las tareas completadas.
    if filtro == 'completadas':
        tareas = gestor.obtener_tareas(completadas=True)
                # Si el filtro es 'pendientes', obtenemos solo las tareas pendientes.
    elif filtro == 'pendientes':
        tareas = gestor.obtener_tareas(completadas=False)
    else:
        #sino hay filtro o es todas, se moestrara todas las tareas
        tareas = gestor.obtener_tareas()
    
    #render_template toma index.html y agrega los datos de tareas cada vez que lo usas con ayudad de jinja2.
    return render_template('index.html', tareas=tareas)


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    # Si el método es POST, significa que el formulario ha sido enviado.
    if request.method == 'POST':
        #se toma los datos
        descripcion = request.form['descripcion']
        fecha_inicio = request.form['fecha_inicio']
        #y se los manda al metodo agregar_tarea
        gestor.agregar_tarea(descripcion, fecha_inicio)
        #y se lo redirige a index
        return redirect(url_for('index'))
    #si es get se muestra el formulario
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


