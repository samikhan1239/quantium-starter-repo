import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

# Add vertical line for price increase
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)

# Add annotation text
fig.add_annotation(
    x="2021-01-15",
    y=df["sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=2
)

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "marginBottom": "30px"
        }
    ),

    dcc.Graph(
        figure=fig
    )

], style={
    "padding": "20px"
})

# Run app
if __name__ == "__main__":
    app.run(debug=True)