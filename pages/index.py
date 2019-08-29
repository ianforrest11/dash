import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Components of NBA Salaries
            
            NBA Basketball Players are well compensated compared to the general population. 
            During the 2018-19 season, they earned an average salary of $7,080,000.  
            However, this number is somewhat misleading.

            Some clarity is provided by the Standard Deviation, which is around $8 million dollars 
            away from the mean.  In other words, there are substantial differences
            between the salaries going into that $7,080,000 number.

            But what exactly determines an NBA Player's salary? Well-known players like 
            LeBron James are extremely talented and thus earn a lot of money.  Likewise, 
            less-talented/well-known players earn substantially less money.  Unfortunately
            such statements are generalities.
            
            What if there was a way to identify specific components that make up a player's salary?
            Instead of saying 'LeBron James has a high salary because he's good,' wouldn't it be nice 
            to identify the specific characteristics that make up that salary?  Is his high salary more
            attributed to his points per game average or his status as a Most Valuable Player?

            This study attempts to analyze the impact of various player components on NBA salaries
            for the 2018-2019 NBA season.  

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

        html.Img(src='assets/PPGPDP.png', className='img-fluid'),

        html.Div([
            html.P('The above image displays a partial dependence plot of points per game (PPG) as a predictor of NBA player salary for the 2018-19 season.  Each blue line represents a group of players with similar PPG statistics, while the dark green line represents the average for the league as a whole. The graph indicates that points per game is a mixed component for determining salary.  For players with high PPG averages, it is a good predictor.  For players with low PPG averages, it is a poor/negative predictor.'),
        ],style={'fontSize': 10})

    ]
)

layout = dbc.Row([column1, column2])