def render_tarea_list(tareas):
    return [
        {
            "id":tarea.id,
            "title":tarea.title,
            "description":tarea.description,
            "status":tarea.status,
            "created_at":tarea.create_at,
            "assigned_to":tarea.assigned_to
        }
        for tarea in tareas
    ]

def render_tarea_detail(tarea):
    return {
            "id":tarea.id,
            "title":tarea.title,
            "description":tarea.description,
            "status":tarea.status,
            "created_at":tarea.created_at,
            "assigned_to":tarea.assigned_to

        }