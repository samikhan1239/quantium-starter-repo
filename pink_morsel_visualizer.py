import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort values
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#f4f4f4",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#333",
                "marginBottom": "30px"
            }
        ),

        html.Div([

            html.Label(
                "Filter by Region:",
                style={
                    "fontSize": "20px",
                    "fontWeight": "bold"
                }
            ),

            dcc.RadioItems(
                id="region-filter",

                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],

                value="all",

                inline=True,

                style={
                    "marginTop": "10px",
                    "marginBottom": "20px"
                }
            ),

        ]),

        dcc.Graph(id="sales-chart")

    ]
)

# Callback function
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create graph
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Sales Data - {selected_region.title()} Region",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    # Add price increase line
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)