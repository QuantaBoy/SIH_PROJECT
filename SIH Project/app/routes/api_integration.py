from flask import Blueprint,jsonify, request 

import requests 

api_bp = Blueprint("api_integration", __name__)

@api_bp.route('/joke',methods=['GET'])
def get_joke():
    category =  request.args.get("category", "programming")

    external_api = "https://official-joke-api.appspot.com/jokes/programming/random"

    response = requests.get(external_api,timeout = 5)

    if response.status_code != 200:
        return jsonify({
            "error" : "Failed to Fetch external API", 
            "status_code" : response.status_code
        }),502
    
    joke_data = response.json()

    return jsonify({
        "source" : "external API",
        "joke" : joke_data
    })