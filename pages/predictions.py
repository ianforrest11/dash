import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from app import app

from joblib import load
lrpipeline = load('lrpipeline.joblib')

style = {'padding': '0.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict
        Use the player components below to generate a predicted 2018-2019 NBA Salary.  Please note that simulating unrealistic
        scenarios, such as a 7'6" point guard with 100% 3-point accuracy, may skew the results of the prediction.
    
    """), 

    html.Div("""
    
    Predicted Salary:
    
    """,style={'fontWeight':'bold'}),
    html.Div(id='prediction-content', style={'fontWeight':'bold'}), 

    html.Div([
        dcc.Markdown('#### Age'),
        dcc.Slider(
            id='Age', 
            min=18, 
            max=40, 
            step=1, 
            value=22, 
            marks={n: str(n) for n in range(18,41,2)}, 
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Height(in)'),
        dcc.Slider(
            id='Ht', 
            min=60, 
            max=90, 
            step=1, 
            value=75, 
            marks={n: str(n) for n in range(60,91,3)}, 
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Weight(lbs)'),
        dcc.Slider(
            id='Wt', 
            min=170, 
            max=300, 
            step=1, 
            value=220, 
            marks={n: str(n) for n in range(170,301,10)}, 
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Minutes Per Game'),
        dcc.Slider(
            id='MPG', 
            min=0, 
            max=48, 
            step=1, 
            value=32,
            marks={n: str(n) for n in range(0,49,4)}, 
            className='mb-5', 
        ), 
    ], style=style),

     html.Div([
        dcc.Markdown('#### Field Goal Percentage'),
        dcc.Slider(
            id='FGP', 
            min=0, 
            max=1, 
            step=.01, 
            value=.47,
            marks={
                0: {'label': '0%'},
                0.1: {'label': '10%'},
                0.2: {'label': '20%'},
                0.3: {'label': '30%'},
                0.4: {'label': '40%'},
                0.5: {'label': '50%'},
                0.6: {'label': '60%'},
                0.7: {'label': '70%'},
                0.8: {'label': '80%'},
                0.9: {'label': '90%'},
                1: {'label': '100%'}
                  },  
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### 3-Point Percentage'),
        dcc.Slider(
            id='TPP', 
            min=0, 
            max=1, 
            step=.01, 
            value=.37, 
            marks={
                0: {'label': '0%'},
                0.1: {'label': '10%'},
                0.2: {'label': '20%'},
                0.3: {'label': '30%'},
                0.4: {'label': '40%'},
                0.5: {'label': '50%'},
                0.6: {'label': '60%'},
                0.7: {'label': '70%'},
                0.8: {'label': '80%'},
                0.9: {'label': '90%'},
                1: {'label': '100%'}
                  },
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Free-Throw Percentage'),
        dcc.Slider(
            id='FTP', 
            min=0, 
            max=1, 
            step=.01, 
            value=.81, 
            marks={
                0: {'label': '0%'},
                0.1: {'label': '10%'},
                0.2: {'label': '20%'},
                0.3: {'label': '30%'},
                0.4: {'label': '40%'},
                0.5: {'label': '50%'},
                0.6: {'label': '60%'},
                0.7: {'label': '70%'},
                0.8: {'label': '80%'},
                0.9: {'label': '90%'},
                1: {'label': '100%'}
                  },
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Points Per Game'),
        dcc.Slider(
            id='PPG', 
            min=0, 
            max=40, 
            step=.1, 
            value=16, 
            marks={n: str(n) for n in range(0,41,4)}, 
            className='mb-5', 
        ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('#### Rebounds Per Game'),
        dcc.Slider(
            id='RPG', 
            min=0, 
            max=20, 
            step=.1, 
            value=6, 
            marks={n: str(n) for n in range(0,21,4)}, 
            className='mb-5', 
        ),
    ], style=style), 

    html.Div([
        dcc.Markdown('#### Assists Per Game'),
        dcc.Slider(
            id='APG', 
            min=0, 
            max=15, 
            step=.1, 
            value=3, 
            marks={n: str(n) for n in range(0,16,3)}, 
            className='mb-5', 
        ),  
    ], style=style),

    html.Div([
        dcc.Markdown('#### Steals Per Game'),
        dcc.Slider(
            id='SPG', 
            min=0, 
            max=4, 
            step=.1, 
            value=1.5, 
            marks={n: str(n) for n in range(0,5,1)}, 
            className='mb-5', 
        ), 
    ], style=style),

    html.Div([
        dcc.Markdown('#### Blocks Per Game'),
        dcc.Slider(
            id='BPG', 
            min=0, 
            max=4, 
            step=.1, 
            value=1.5, 
            marks={n: str(n) for n in range(0,5,1)}, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Turnovers Per Game'),
        dcc.Slider(
            id='TPG', 
            min=0, 
            max=6, 
            step=.1, 
            value=1.5, 
            marks={n: str(n) for n in range(0,7,1)}, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Point Guard'),
        dcc.Slider(
            id='PG',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Shooting Guard'),
        dcc.Slider(
            id='SG',
            min=0, 
            max=1, 
            step=1, 
            value=1, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Small Forward'),
        dcc.Slider(
            id='SF',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Power Forward'),
        dcc.Slider(
            id='PF',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Center'),
        dcc.Slider(
            id='C',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  },
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Most Valuable Player'),
        dcc.Slider(
            id='MVP',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Former All-Star'),
        dcc.Slider(
            id='FAS',
            min=0, 
            max=1, 
            step=1, 
            value=0, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  }, 
            className='mb-5', 
        )
    ], style=style),

    html.Div([
        dcc.Markdown('#### Current All-Star'),
        dcc.Slider(
            id='CAS',
            min=0, 
            max=1, 
            step=1, 
            value=1, 
            marks={
                0: {'label': 'No'},
                1: {'label': 'Yes'}
                  },
            className='mb-5', 
        )
    ], style=style),

])

# prediction code underneath
@app.callback(
    Output('prediction-content', 'children'),
    [Input('Age', 'value'), Input('Ht', 'value'), Input('Wt', 'value'),
    Input('MPG', 'value'), Input('FGP', 'value'), Input('TPP', 'value'),
    Input('FTP', 'value'), Input('PPG', 'value'), Input('RPG', 'value'), 
    Input('APG', 'value'),Input('SPG', 'value'), Input('BPG', 'value'),
    Input('TPG', 'value'), Input('PG', 'value'), Input('SG', 'value'),
    Input('SF', 'value'), Input('PF', 'value'), Input('C', 'value'),
    Input('MVP', 'value'), Input('FAS', 'value'), Input('CAS', 'value')

    ],
)
def predict(Age, Ht, Wt, MPG, FGP, TPP, 
            FTP, PPG, RPG, APG, SPG, BPG,
            TPG, PG, SG, SF, PF, C, MVP,
            FAS, CAS):
    df = pd.DataFrame(
        columns=['Age', 'Ht(in)', 'Wt(lbs)', 'MPG', 'FG%', '3P%', 'FT%', 'PPG', 'RPG',
       'APG', 'SPG', 'BPG', 'TPG', 'PG?', 'SG?', 'SF?', 'PF?', 'C?', 'mvp?', 'f_allstar?',
       'c_allstar?'], 
        data=[[Age, Ht, Wt, MPG, FGP, TPP, FTP, PPG, RPG, APG, SPG, BPG, TPG, PG, SG, SF, PF, C, MVP ,FAS, CAS]]
    )

    y_pred = lrpipeline.predict(df)[0]
    return f'${y_pred:,.0f} dollars'