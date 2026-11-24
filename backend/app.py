from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Flask backend is running"}), 200

@app.route('/submit', methods=['POST'])
def submit():
    # Accept JSON from Express axios or direct form data
    data = request.get_json(silent=True) or request.form.to_dict()

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    course = data.get('course', '').strip()
    message = data.get('message', '').strip()

    if not name or not email or not course:
        return jsonify({"error": "Name, Email, and Course are required"}), 400

    # Example data processing (similar to Assignment 2)
    processed = {
        "student_name": name.title(),
        "contact_email": email.lower(),
        "enrolled_course": course.upper(),
        "remarks": message if message else "None provided"
    }

    return jsonify({
        "status": "success",
        "message": f"Data received and processed for {processed['student_name']}",
        "processed_data": processed
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)