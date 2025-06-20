import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='templates')

# Connecting to MongoDB
mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')
client = MongoClient(mongo_connection_string)
db = client['SurveyDatabase']
collection = db['Users']

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        age = int(request.form.get('Age', 0))
        gender = request.form.get('gender', 'Not Specified')
        income = float(request.form.get('income'))

        expenses = {}
        categories = ['Utilities', 'Entertainment', 'School_fees', 'Shopping', 'Healthcare']
        for cat in categories:
            value = request.form.get(cat)
            if value:
                expenses[cat] = float(value)

        user_data = {
            'Age': age,
            'Gender': gender,
            'Income': income,
            'Expenses': expenses
        }

        collection.insert_one(user_data)
        return redirect('/success')

    return render_template('form.html')

@app.route('/success')
def success():
    return 'Survey Submitted Successfully! Thank you.'

if __name__ == '__main__':
    app.run(debug=True)




