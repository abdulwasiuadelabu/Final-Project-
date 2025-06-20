import csv
from pymongo import MongoClient

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = int(age)
        self.gender = gender
        self.income = float(income)
        self.expenses = expenses  # Dictionary

    def to_dict(self):
        data = {
            'Age': self.age,
            'Gender': self.gender,
            'Income': self.income
        }
        data.update(self.expenses)
        return data

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['SurveyDatabase']
collection = db['Users']

# Fetch data
records = collection.find()

# Convert to User objects
users = []
for r in records:
    user = User(r['Age'], r['Gender'], r['Income'], r['Expenses'])
    users.append(user)

# Save to CSV
with open('survey_data.csv', 'w', newline='') as file:
    fieldnames = ['Age', 'Gender', 'Income', 'Utilities', 'Entertainment', 'School_fees', 'Shopping', 'Healthcare']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow(user.to_dict())

print("✅ Data exported to survey_data.csv")

