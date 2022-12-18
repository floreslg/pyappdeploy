from flask import Flask
import dash

server = Flask(__name__)
dash_app = dash.Dash(
    __name__,
    server=server
)
dash_app.layout = dash.html.Div("Hello")

app = dash_app.server
if __name__=='__main__':
    app.run()