from flask import Flask, render_template, request, url_for, flash, redirect
from model import prediction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324febgfjt56'

FIELDS = [{'field': 'Age',
             'type': 'select',
             'tool-tip': False,
             'list': {'0': '18-24', '1': '25-34', '2':'35-44', '3':'45-54', '4':'55-64', '5':'65+'},},
            
            {'field': 'Gender',
             'type': 'select',
             'tool-tip': False,
             'list': {'1': 'Male', '0':'Female'},},
            
            {'field': 'Education',
             'type': 'select',
             'tool-tip': False,
             'list': {'0': 'Left school before 16 years', '1':'Left school at 16 years', '2':'Left school at 17 years', '3':'Left school at 18 years', '4':'Some college or university, no certificate or degree', '5':'Professional certificate / diploma', '6':'University degree', '7':'Masters degree', '8':'Doctorate degree'},},
            
            {'field': 'Country',
             'type': 'select',
             'tool-tip': False,
             'list': {'0': 'Other', '1':'Australia', '2':'Canada', '3':'New Zealand', '4':'Republic of Ireland', '5':'UK', '6':'USA'},},

            {'field': 'Ethnicity',
             'type': 'select',
             'tool-tip': False,
             'list': {'0': 'White', '1': 'Asian', '2': 'Black', '3': 'Mixed-Black/Asian', '4': 'Mixed-White/Asian', '5': 'Mixed-White/Black', '6': 'Other'},},
            
            {'field': 'Neuroticism',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - very stable', '1': '2', '2': '3', '3': '4', '4': '5 - subject to anxiety', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - extreme anxiety'},},
            
            {'field': 'Extraversion',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - completely introverted', '1': '2', '2': '3', '3': '4', '4': '5 - subject to extraversion', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - very extroverted'},},
            
            {'field': 'Openness',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - very closed-minded', '1': '2', '2': '3', '3': '4', '4': '5 - subject to curiosity', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - very open-minded'},},
            
            {'field': 'Agreeableness',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - very uncooperative', '1': '2', '2': '3', '3': '4', '4': '5 - subject to cooperation', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - extremely friendly'},},
            
            {'field': 'Conscientiousness',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - completely disorganized', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - high level of self-discipline'},},
            
            {'field': 'Impulsiveness',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - not at all impulsive', '1': '2', '2': '3', '3': '4', '4': '5 - subject to impulsivity', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - very impulsive'},},
            
            {'field': 'Sensation_seeking',
             'type': 'select',
             'tool-tip': True,
             'list': {'0': '1 - not at all attracted by risky things', '1': '2', '2': '3', '3': '4', '4': '5 - subject to new experiences', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10 - very attracted to the unknown'},},
            ]

names = [k['field'] for k in FIELDS]

@app.route('/', methods=['GET', 'POST'])
def index():
    print('GET / Post')
    # print(all([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,7.0,5.0,4.0]))
    fields = FIELDS
    errors = False
    if request.method == "POST":
        values = dict.fromkeys(names, -1)
        for name in names:
            value = request.form[name]
            if value == '' or value == 'null':
                errors = True
            else:
                for f in fields:
                    if f['field'] == name:
                        f['value'] = request.form[name]
                values[name] = float(request.form[name])
        if not any([val==-1 for val in values.values()]):
            proba = prediction(values)
            return render_template('result.html', proba=proba)
            # return values
    return render_template('index.html', fields=fields, errors=errors)
