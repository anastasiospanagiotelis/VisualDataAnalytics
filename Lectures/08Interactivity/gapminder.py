from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id="scatter-plot"),
    html.P("Select a year:"),
    dcc.Slider(1952,2007,5,
        value = 1952,
        id='year-slider',
        marks={i: '{}'.format(i) for i in range(1952,2007,5)}
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    Input("year-slider", "value"))
def update_plot(year):
    gm = px.data.gapminder() # replace with your own data source
    gmy = gm[gm['year']==year]
    fig =  px.scatter(
      gmy,
      y='lifeExp',
      x='gdpPercap',
      size='pop', 
      color= 'continent', 
      hover_data = ['country'],
      log_x=True, 
      log_y = True,
      title = 'Health v Wealth across the world in '+str(year)
      )
    return fig


app.run_server(debug=True)
