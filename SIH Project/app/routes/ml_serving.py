from flask import Blueprint, request, jsonify

from ..ml.model import predict 

ml_bp = Blueprint("ml_serving", __name__)

@ml_bp.route('/predict',methods = ['POST'])
def predict_route():
    body = request.get_json(silent=True)

    if not body or 'features' not in body:
        return jsonify({"error" : "please send JSON with a 'features' key"}),400
    features = body['features']

    if not isinstance(features,(list,tuple)):
        return jsonify({"error" : "'features' must be a list or tuple"}), 400
    try : 
        result = predict(features)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error":"Prediction Failed", "details": str(e)}),500
    return jsonify({"prediction":result})