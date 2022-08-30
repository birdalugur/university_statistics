import os
from name_shortener import shorten
import plotly.express as px
import pandas as pd
from plotly.offline import plot

if not os.path.exists('charts'):
    os.mkdir("charts")


def plot_OLS(data: pd.DataFrame, text_column: str, text_to_color: str, chart_name: str):
    data['color'] = data[text_column].str.contains(text_to_color).replace({True: 'Bilgi University', False: 'Other'})

    data['university_y'] = data['university_y'].apply(shorten)

    fig = px.scatter(data, x='value_x', y='value_y', color='color',
                     text=data['university_y'], trendline="ols")

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        plot_bgcolor='rgb(247, 249, 249 )'
    )
    fig.update_traces(textposition="bottom right")

    plot(fig, filename=f'charts/{chart_name}.html', auto_open=False)
