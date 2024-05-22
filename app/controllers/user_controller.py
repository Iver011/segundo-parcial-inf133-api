from flask import Blueprint,request,jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

user=Blueprint("user",__name__)

@user.route("/register",methods=["POST"])
def register():
    data=request.json
    name=data.get("name")
    email=data.get("email")
    password=data.get("password")
    
    role=data.get("role")

    if not name or not password:
        return jsonify({"error":"Se requiere nombre de usuario y contraseña"}),400
    user=User.find_by_username(name)
    if user:
        return jsonify({"error":"El nombre de usuario ya existe"}), 400
    new_user=User(name,role,email,password)
    new_user.save()
    return jsonify({"message":"El usuario se creo exitosamente"}),201

@user.route("/login",methods=["POST"])
def login():
    data = request.json
    email=data.get("email")
    password=data.get("password")
    print(email)    
    user=User.find_by_username(email)
    print(user)
    if user and check_password_hash(user.password_hash,password):
        access_token=create_access_token(
            identity={"email":email,"roles":user.roles}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error":"Credenciales invalidas"}),401