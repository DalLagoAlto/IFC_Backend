from flask_cors import CORS
from flask import Flask, request, jsonify
import ifcopenshell
import os

app = Flask(__name__)
CORS(app, origins=["https://ifc-frontend.vercel.app"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    errors = validate_ifc(filepath)

    os.remove(filepath)
    return jsonify(errors)

def validate_ifc(filepath):
    errors = []
    ifc_file = ifcopenshell.open(filepath)

    for element in ifc_file.by_type("IfcProduct"):
        if not element.Name:
            errors.append({
                "type": "Metadata",
                "description": f"Object with ID {element.GlobalId} is missing a Name."
            })
        if not element.Description:
            errors.append({
                "type": "Metadata",
                "description": f"Object with ID {element.GlobalId} is missing a Description."
            })
    return errors

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
