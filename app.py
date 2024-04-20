import os
from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)
app.static_folder = 'viz'

def get_visualizations(folder):
    visualizations = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                relative_path = os.path.relpath(os.path.join(root, file), folder)
                visualizations.append(relative_path)
    return visualizations

@app.route('/')
def index():
    viz_folder = 'viz'
    visualizations = get_visualizations(viz_folder)
    return render_template('index.html', visualizations=visualizations)

@app.route('/paths')
def get_paths():
    viz_folder = 'viz'
    paths = []
    for root, dirs, files in os.walk(viz_folder):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), viz_folder)
            paths.append(relative_path)
    return jsonify(paths)

@app.route('/<path:filepath>')
def serve_static(filepath):
    return send_from_directory(app.static_folder, filepath)

if __name__ == '__main__':
    app.run(debug=True)