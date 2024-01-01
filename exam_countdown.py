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
        # Extracting the date and time separately
        date_str, time_str, subject = exam_date.split(' ', 2)
        exam_datetime = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")
        time_left = exam_datetime - current_date
        time_left_list.append(f"Time left until {time_str} {subject}: {time_left}")

    return render_template('index.html', time_left_list=time_left_list)

if __name__ == '__main__':
    app.run(debug=True)
