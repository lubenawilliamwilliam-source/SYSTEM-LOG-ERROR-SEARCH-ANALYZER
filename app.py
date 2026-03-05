from flask import Flask, render_template, request
import os

app = Flask(__name__)

LOG_FILE = "logs/sample.log"

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    if request.method == 'POST':
        keyword = request.form['keyword']

        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as file:
                for line in file:
                    if keyword.lower() in line.lower():
                        errors.append(line.strip())
        else:
            errors.append("Log file not found.")

    return render_template('index.html', errors=errors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
