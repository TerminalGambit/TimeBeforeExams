from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    exam_dates = [
        "09/01/2024 13:00 Base de données",
        "10/01/2024 13:00 Outils Formels de l'Informatique",
        "15/01/2024 08:00 Programmation en C et structures de données",
        "17/01/2024 08:00 Introduction à l'intelligence artificielle"
    ]

    current_date = datetime.now()
    time_left_list = []

    for exam_date in exam_dates:
        exam_datetime = datetime.strptime(exam_date, "%d/%m/%Y %H:%M")
        time_left = exam_datetime - current_date
        time_left_list.append(f"Time left until {exam_date[11:]}: {time_left}")

    return render_template('index.html', time_left_list=time_left_list)

if __name__ == '__main__':
    app.run(debug=True)
