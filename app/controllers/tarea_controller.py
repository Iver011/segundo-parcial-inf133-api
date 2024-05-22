#listar plnatas, listar por id, crear dulce,actualizar dulce, borrar dulce
from flask import Blueprint,request,jsonify
from views.tarea_view import render_tarea_detail,render_tarea_list
from utils.decorators import jwt_required,roles_required
from models.tarea_model import Tarea

tarea=Blueprint("tarea",__name__)

@tarea.route("/tareas",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","member"])
def get_tareas():
    tareas=Tarea.get_all()
    return jsonify(render_tarea_list(tareas))

@tarea.route("/tareas/<int:id>",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","member"])
def get_tarea(id):
    tarea=Tarea.get_by_id(id)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404
    return jsonify(render_tarea_detail(tarea))

@tarea.route("/tareas",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_tarea():
    data=request.json
    title=data.get("title")
    description=data.get("description")
    status=data.get("status")
    created_at=data.get("created_at")
    assigned_to=data.get("assigned_to")
    
    if not title or description is None or not status or not created_at or not assigned_to:
        return jsonify({"error":"Faltan atributos requeridos"}),400
    
    tarea=Tarea(title,description,status,created_at,assigned_to)
    tarea.save()
    return jsonify(render_tarea_detail(tarea)),201

@tarea.route("/tareas/<int:id>",methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_tarea(id):
    tarea=Tarea.get_by_id(id)
    if not tarea:
        return jsonify({"error":"Tarea no encontrada"}),404
    data=request.json
    title=data.get("title")
    description=data.get("description")
    status=data.get("status")
    created_at=data.get("created_at")
    assigned_to=data.get("assigned_to")

    tarea.update(title,description,status,created_at,assigned_to)
    return jsonify(render_tarea_detail(tarea)),200

@tarea.route("/tareas/<int:id>",methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_tarea(id):
    tarea=Tarea.get_by_id(id)
    if not tarea:
        return jsonify({"Error":"Tarea no encontrada"}),404
    
    tarea.delete()
    return "", 204