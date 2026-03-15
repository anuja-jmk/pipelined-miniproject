from dash import Dash, html, dcc, Input, Output, State
import calculator

app = Dash(__name__)
server = app.server 
app.layout = html.Div([
    
    html.H1("Scientific Calculator"),

    dcc.Dropdown(
        id="operation",
        options=[
            {"label": "Square Root", "value": "sqrt"},
            {"label": "Factorial", "value": "fact"},
            {"label": "Natural Log", "value": "log"},
            {"label": "Power", "value": "pow"},
        ],
        placeholder="Select Operation"
    ),

    dcc.Input(id="num1", type="number", placeholder="Enter first number"),
    dcc.Input(id="num2", type="number", placeholder="Enter second number (if needed)"),

    html.Button("Calculate", id="btn"),

    html.H3(id="result")
])


@app.callback(
    Output("result", "children"),
    Input("btn", "n_clicks"),
    State("operation", "value"),
    State("num1", "value"),
    State("num2", "value"),
)
def calculate(n_clicks, operation, num1, num2):

    if not n_clicks:
        return ""

    try:
        if operation == "sqrt":
            result = calculator.square_root(num1)

        elif operation == "fact":
            result = calculator.factorial(int(num1))

        elif operation == "log":
            result = calculator.natural_log(num1)

        elif operation == "pow":
            result = calculator.power_function(num1, num2)

        else:
            return "Select an operation"

        return f"Result: {result}"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)