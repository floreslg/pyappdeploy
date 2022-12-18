from flask import Flask
import dash

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server
)
app.layout = dash.html.Div("Hello")

if __name__=='__main__':
    app.run_server()