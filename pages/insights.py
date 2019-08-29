import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            Let's take a look at an individual prediction for LeBron James.

            The top graph is a comparison of LeBron's actual 2018-19 salary against
            the XGBoost and linear regression predicted salaries.  The XGBoost prediction
            is slightly closer, but both have an error around $3 million dollars.

            The bottom graph is a Shap plot breakdown of LeBron's XGBoost-predicted salary.
            An average salary is calculated, and then is increased or deacreased by the 
            magnitude of the components. In LeBron's case, his Age, PPG, and MPG had the 
            biggest impact on his Salary Prediction.
           


            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/lebron.png', className='img-fluid'),

        html.Div([
            html.P('LeBron James - Comparison of Actual vs. Predicted Salaries'),
        ],style={'fontSize': 15, 'padding':20}),



        html.Img(src='assets/shap.png', className='img-fluid'),

        html.Div([
            html.P('Shap Analysis - LeBron James XGBoost Predicted Salary'),
        ],style={'fontSize': 15}),

    ]
)

layout = dbc.Row([column1, column2])