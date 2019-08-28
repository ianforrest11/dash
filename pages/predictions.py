import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from app import app

from joblib import load
lrpipeline = load('lrpipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions'),
        dcc.Markdown('### Age'),
        dcc.Slider(
            id='Age', 
            min=18, 
            max=45, 
            step=1, 
            value=25, 
            marks={n: str(n) for n in range(18,45,1)}, 
            className='mb-5', 
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Predicted Salary', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

# prediction code underneath
@app.callback(
    Output('prediction-content', 'children'),
    [Input('Age', 'value')],
)
def predict(Age):
    df = pd.DataFrame(
        columns=['Age', 'Ht(in)', 'Wt(lbs)', 'MPG', 'FG%', '3P%', 'FT%', 'PPG', 'RPG',
       'APG', 'SPG', 'BPG', 'TPG', 'PG?', 'SG?', 'SF?', 'PF?', 'C?', 'mvp?',
       'f_allstar?', 'c_allstar?'], 
        data=[[Age, 78, 232, 17.8, 0.465, 0.361, 0.690, 6.4, 3.2, 1.4, 0.5, 0.1, 0.8, 0, 1, 0, 0, 0, 0 ,0, 0]]
    )
    y_pred = lrpipeline.predict(df)[0]
    return f'{y_pred:.0f} dollars'
    #return Age