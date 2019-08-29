import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [

        html.Img(src='assets/elilr.png', className='img-fluid'),

        html.Div([
            html.P('Linear Regression Model - Permutation Importances'),
        ],style={'fontSize': 11})

    ]
)

column2 = dbc.Col(
    [

        html.Img(src='assets/elixgb.png', className='img-fluid'),

        html.Div([
            html.P('XGBoost Regression Model - Permutation Importances'),
        ],style={'fontSize': 11})

    ]
)

column3 = dbc.Col(
    dcc.Markdown("""
       
       Two models were trained as part of the study: an XGBoost Regression model and a
       linear regression model.  The images above display the permutation importances for
       both.  
       
       Without getting too technical, permutation importances measure the impact of a given feature on a model's overall projection.
       Green features are valuable components for predicting NBA Salaries, while yellow and red
       features are neutral/negative predictors.  The darker a feature's shade, the more important
       it is in coming up with a prediction.

       Similar predictions were made.  Age, minutes per game (MPG), and points per game
       (PPG) were identified as important predictive components of both models.

       There are key variances, however.  The linear regression model indicates current
       all-star status as the most important indicator of salary, while the XGBoost
       regression model identifies it as somewhat neutral.

       Interestingly enough, features created as a part of the study, such as 'c_allstar?', are 
       just as important to the models' predictions as  actual statistical features, such as points 
       per game.
        


    
    """)
)

layout = [
            dbc.Row([column1, column2]),
            dbc.Row([column3])
]