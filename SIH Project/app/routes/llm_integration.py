from flask import Blueprint, request, jsonify, current_app

from openai import OpenAI

llm_bp = Blueprint("llm_integration", __name__)

@llm_bp.route('/complete', methods = ['POST'])

def llm_complete():
    body = request.get_json(silent=True)
    if not body or "prompt" not in body:
        return jsonify({"error":"Missing 'prompt' in JSON"}), 400
    user_prompt = body['prompt']

    api_key = current_app.config.get["OPENAI_API_KEY"]

    if not api_key:
        return jsonify({"error" : "Missing OpenAI API Key in Config"}), 500
    client = OpenAI(api_key=api_key)

    try:
        llm_response = client.response.create(
            model = 'gpt-4.1-mini',
            input = user_prompt
        )

        completion_text = llm_response.output_text
    except Exception as e:
        return jsonify({"error" : "LLM request failed", "details" : str(e)}),500
    
    return jsonify({
        "prompt" : user_prompt,
        "response" : completion_text
    })