import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly_express as px

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(r"data/suicides.csv")

fig = px.line(df, x="year", y="country")

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for Python.
    """
        ),
        dcc.Graph(id="suicides", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
