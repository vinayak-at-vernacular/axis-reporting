from project import server
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt


@server.route("/")
def hello_world():
    return jsonify(hello="world")

app = dash.Dash(__name__, server=server)

app.layout = html.Div(
    children=[
       html.P('hi')
    ]
)

@server.route("/dash")
def my_dash_app():
    return app.index()

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000,debug=True)
