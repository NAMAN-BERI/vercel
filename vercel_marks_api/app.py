from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the marks data from the JSON file
with open('marks.json', 'r') as file:
    data = json.load(file)

# Convert the data into a dictionary for quick lookups
marks_dict = {student['name']: student['marks'] for student in data}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get names from query parameters
    marks = [marks_dict.get(name, None) for name in names]  # None if name not found
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
