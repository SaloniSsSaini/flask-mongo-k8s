from flask import Blueprint, request, jsonify
from datetime import datetime
from app.db import collection

data_bp = Blueprint("data_bp", __name__)

@data_bp.route("/")
def index():
    return f"Welcome to the Flask app! The current time is: {datetime.now()}"

@data_bp.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        payload = request.get_json()
        collection.insert_one(payload)
        return jsonify({"status": "Data inserted"}), 201

    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200
