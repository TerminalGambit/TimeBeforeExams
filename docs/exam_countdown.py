from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    exam_dates = [
        {"date": "09/01/2024", "time": "13:00", "subject": "Base de données"},
        {"date": "10/01/2024", "time": "13:00", "subject": "Outils Formels de l'Informatique"},
        {"date": "15/01/2024", "time": "08:00", "subject": "Programmation en C et structures de données"},
        {"date": "17/01/2024", "time": "08:00", "subject": "Introduction à l'intelligence artificielle"}
    ]

    current_date = datetime.now()
    time_left_list = []

    for exam in exam_dates:
        exam_datetime_str = f"{exam['date']} {exam['time']}"
        exam_datetime = datetime.strptime(exam_datetime_str, "%d/%m/%Y %H:%M")
        time_left = exam_datetime - current_date
        time_left_list.append(f"Time left until {exam['subject']} at {exam['time']} on {exam['date']}: {time_left}")

    return render_template('index.html', time_left_list=time_left_list)

if __name__ == '__main__':
    app.run(debug=True)
