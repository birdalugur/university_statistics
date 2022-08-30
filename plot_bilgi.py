import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from plotly.offline import plot

path = "bilgi sıralama.xlsx"

data = pd.read_excel(path)

fig = go.Figure()

cols = data.columns

cols = cols[1:]

for col in cols:
    fig.add_trace(go.Scatter(x=data['yıl'], y=data[col],
                             mode='lines',
                             name=col))

plot(fig)
