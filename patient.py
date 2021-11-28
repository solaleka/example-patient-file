import dash
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import json

with open(r'C:\Users\shafi\Downloads\Patient File\fixed_patient.json') as patient_json:
  data = json.load(patient_json)

family_name = data['name'][0]['family']
given_name = data['name'][0]['given']
gender = data['gender'].capitalize()
conditions = data['conditions']
num_of_conditions = len(data['conditions'])
organization_name = data['managingOrganization'].get('display')

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        
        html.H1(children="Patient Record"),
        html.P(children="------------------------------------------------"),
        html.P(children="Name of Patient: " + given_name[0] + " " + family_name[0]),
        html.P(children="Organization Name: " + organization_name),
        html.P(children="Gender: " + gender),
        html.P(children="Number of Conditions They Have: " + str(num_of_conditions)),
        html.P(children="List of all Conditions:"),
        html.P(children="- " + conditions[0]),
        html.P(children="- " + conditions[1]),
        html.P(children="- " + conditions[2]),
        
    ])

if __name__ == '__main__':
    app.run_server(debug=True)