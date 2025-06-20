Healthcare Product Launch Survey Tool – Final Project 


#Project Overview#
This initiative implements an end-to-end data pipeline leveraging Flask, MongoDB, Python, and Jupyter Notebook to gather, store, analyze, and visualize participant income and expense data. The insights derived from this process inform the launch strategy for a healthcare product.

Project Features
- Web app built with Flask for survey data collection
- Data stored in MongoDB
- Expense inputs via checkboxes and textboxes for categories which includes:
  - Utilities
  - Entertainment
  - School Fees
  - Shopping
  - Healthcare
- Python class `User` for data handling
- Data exported to CSV and analyzed using Jupyter Notebook
- Charts saved for use in PowerPoint
- Deployed to AWS


Folder Structure


project-folder/
│
├── flask_app.py        - the Main Flask app
├── templates/	         - Web form template folder
│   └── form.html       - Web form template
├── process_data.py     - User class for processing
├── survey_data.csv     - Generated user data
├── visual_flask.ipynb  - Jupyter notebook with visualizations
├── README.txt           - Project instructions (this file)
└── requirements.txt    - Python dependencies


#Installation Instructions#

1. Set up a virtual environment on python and activate it
2. Install dependencies
- Flask, pymongo, pandas, and matplotlib
3. Run MongoDB- Ensure you have MongoDB running locally on 'mongodb://localhost:27017/'
4. Start the Flask app
You can access the app at (http://localhost:5000)

#Data Processing#
Run the process.py file
1. Each submission is processed and stored in 'MongoDB'
2. A Python class 'User' parses the Mongo data into a CSV (`Survey_data.csv`)
3. This file is loaded in 'visual_flask.ipynb' for visualization


#Visualization#

Open 'visual_flask.ipynb' in 'Jupyter Notebook' to view:
1. Top Ages by Income – bar chart
2. Spending by Gender Across Categories – Grouped bar chart

All charts are saved as '.png' files for PowerPoint use.

## Deployment Disclaimer ##
Note:
The original requirements for this project specified deploying the Flask application on Amazon Web Services (AWS). It was initially deployed and tested the application on an AWS EC2 instance. However,  encountered recurring stability issues—specifically, the EC2 instance would frequently shut down or restart, causing service interruptions.

To ensure a reliable, accessible, and seamless demonstration experience, I redeployed the application on Render, a cloud platform that provides free and stable hosting for web applications. This allowed me to meet all other project requirements while maintaining app accessibility.

All functionalities, including Flask development, MongoDB integration, and data processing, remain fully aligned with the assignment goals.
Run this URL to see the application deployed

https://new-flask-app-lk0d.onrender.com
