# app.py
from flask import Flask, render_template, request
from model import generate_results

app = Flask(__name__)

@app.route('/')
def upload_page():
    return render_template('upload_page.html')

@app.route('/results', methods=['POST'])
def display_results():
    if request.method == 'POST':
        # Save uploaded file
        uploaded_file = request.files['file']
        uploaded_file.save('data.json')

        # Generate results using model.py
        results = generate_results()

        return render_template('results_page.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
