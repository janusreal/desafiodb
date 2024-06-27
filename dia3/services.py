from dia3.models import Tarea, SubTarea

def recuperar_tareas_y_subtareas():
    # recuperar
    tareas = Tarea.objects.filter(eliminada=False)
    return tareas
    
def crear_tarea(descripcion):
    t = Tarea(descripcion=descripcion)
    t.save()
    imprimir_en_pantalla() 
    #funciona
    
def crear_subtarea(descripcion, idtarea):
    t = Tarea.objects.get(id=idtarea)
    st = SubTarea(descripcion=descripcion, tarea=t)
    st.save()
    imprimir_en_pantalla() 
    #funciona

def eliminar_tarea(idtarea):
    t = Tarea.objects.get(id=idtarea)
    t.eliminada = True  
    t.save()
    imprimir_en_pantalla() 
    #funciona

def eliminar_subtarea(idsubtarea):
    st = SubTarea.objects.get(id=idsubtarea)
    st.eliminada = True
    st.save()
    imprimir_en_pantalla() 
    #funciona

def imprimir_en_pantalla():
    tareas = recuperar_tareas_y_subtareas()

    for t in tareas:
        print(f'[{t.id}] {t.descripcion}')
        for sub_tarea in t.subtareas.filter(eliminada=False):
            print(f'... [{sub_tarea.id}] {sub_tarea.descripcion}')
    imprimir_en_pantalla() 
    #funciona
    
             
