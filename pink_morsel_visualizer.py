import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort data by date
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(

    style={
        "backgroundColor": "#f4f4f4",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        # Dashboard Header
        html.H1(
            id="dashboard-header",
            children="Soul Foods Pink Morsel Sales Dashboard",

            style={
                "textAlign": "center",
                "color": "#333",
                "marginBottom": "30px"
            }
        ),

        # Region Filter Section
        html.Div([

            html.Label(
                "Filter by Region:",

                style={
                    "fontSize": "20px",
                    "fontWeight": "bold",
                    "marginBottom": "10px",
                    "display": "block"
                }
            ),

            dcc.RadioItems(
                id="region-picker",

                options=[
                    {"label": " All", "value": "all"},
                    {"label": " North", "value": "north"},
                    {"label": " East", "value": "east"},
                    {"label": " South", "value": "south"},
                    {"label": " West", "value": "west"},
                ],

                value="all",

                inline=True,

                style={
                    "marginBottom": "20px",
                    "fontSize": "18px"
                }
            ),

        ],

        style={
            "backgroundColor": "white",
            "padding": "20px",
            "borderRadius": "10px",
            "boxShadow": "0px 2px 8px rgba(0,0,0,0.1)",
            "marginBottom": "20px"
        }),

        # Sales Graph
        dcc.Graph(
            id="sales-graph"
        )

    ]
)

# Callback for updating graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value")
)

def update_chart(selected_region):

    # Filter data based on selected region
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create line chart
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

    # Add vertical line for price increase date
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    # Add annotation
    fig.add_annotation(
        x="2021-01-15",
        y=filtered_df["sales"].max(),
        text="Price Increase",
        showarrow=True,
        arrowhead=2
    )

    # Improve graph styling
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
        title_x=0.5
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)