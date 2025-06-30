from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

attendance_data = {
    "CS101": [
        {"seat": "11127098", "name": "胡坤廷", "status": "present"},
        {"seat": "11127114", "name": "游智評", "status": "absent"},
        {"seat": "11127115", "name": "林侑禛", "status": "late"},
    ],
    "AI201": [
        {"seat": "11127020", "name": "張三", "status": "present"},
        {"seat": "11127021", "name": "李四", "status": "late"},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

@app.route('/api/attendance')
def api_attendance():
    course_id = request.args.get('course_id')
    return jsonify(attendance_data.get(course_id, []))

if __name__ == '__main__':
    app.run(debug=True)
