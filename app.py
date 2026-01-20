from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import re
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def send_email(receiver, file_path):
    sender = "kritigoyal0108@gmail.com"
    password = "ymuj hlxl wizw zvam"

    msg = EmailMessage()
    msg['Subject'] = "TOPSIS Result"
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("Please find attached TOPSIS result file.")

    with open(file_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename="result.csv")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    file = request.files['file']
    weights = request.form['weights']
    impacts = request.form['impacts']
    email = request.form['email']

    # Email validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template("index.html", message="Invalid email format")

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    # Validation
    if len(weights) != len(impacts):
        return render_template("index.html", message="Weights and impacts count mismatch")

    for i in impacts:
        if i not in ['+', '-']:
            return render_template("index.html", message="Impacts must be + or -")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    data = pd.read_csv(filepath)
    matrix = data.iloc[:, 1:].values.astype(float)

    # TOPSIS
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    norm_matrix = matrix / norm
    weighted = norm_matrix * weights

    ideal_best, ideal_worst = [], []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))
    score = dist_worst / (dist_best + dist_worst)
    data['Topsis Score'] = score
    data['Rank'] = pd.Series(score).rank(ascending=False)


    result_path = os.path.join(RESULT_FOLDER, "result.csv")
    data.to_csv(result_path, index=False)

    send_email(email, result_path)

    return render_template("index.html", message="Result sent to your email")

if __name__ == '__main__':
    app.run(debug=True)
