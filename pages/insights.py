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

            ## Example Prediction
        
            Let's take a look at an individual prediction for LeBron James.

            The top graph is a comparison of LeBron's actual 2018-19 salary against
            his salaries predicted by the models.  The XGBoost prediction
            is slightly closer, but both have a mean average error of around $3 million dollars.

            The bottom graph is a Shap plot breakdown of LeBron's XGBoost-predicted salary.
            The average salary calculated by the model is increased or decreased by a player's 
            individual components. In LeBron's case, his Age, PPG, and MPG had the biggest 
            impacts on his predicted salary.
            
            LeBron James is an outlier in this particular dataset, indicated by the discrepancy
            between components that increase his predicted salary (red) and those that decrease it (blue).


            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src='assets/lebron.png', className='img-fluid')





    ]
)

column3 = dbc.Col(
    [

        html.Img(src='assets/shap.png', className='img-fluid'),

        html.Div([
            html.P('Shap Analysis - LeBron James XGBoost Predicted Salary'),
        ],style={'fontSize': 12})

    ]
)


layout = [
            dbc.Row([column1, column2]),
            dbc.Row([column3])
]