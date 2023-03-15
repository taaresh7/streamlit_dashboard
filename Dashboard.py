import streamlit as st
import utils
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

#utils.add_logo("logo.png")

utils.set_page_container_style()
st.markdown("# :chart_with_upwards_trend: Dashboard")


res = {"total_client": 1, "total_models_trained": 1, "total_models_running": 1,
        "total_training_data_processed": 1, "total_test_data_processed": 1}

# columns
data_col = ["Clients",
            "Models trained",
            "Models Running",
            "Training Data",
            "Testing Data",]

# 2 for total number of clients
data =  [2] + [v for v in res.values()]

# make 5 st columns
cols = st.columns(len(data_col))

# colors for each column
bg_list = ["#495057", "#c2be5d" ,"#886ab5", "#a83b3b", "#1b612c"]

# for each column
for i, col in enumerate(cols):

    # integer data in large font
    text = f'<span style="font-size:170%" >{str(data[i])}</span>'
    # add a break in html to get to next line
    text = text + "<br> " + data_col[i]
    bg = bg_list[i]   # color for this column
    # now column name in custom css
    text_css = f"""<span style = "background: #fff ; border-left: 10px solid {bg};
                color: black; overflow: hidden;position: relative;box-shadow: 1px 1px 3px rgba(0,0,0,0.75);
                ;display: inline-block;float: left;padding: 1em;border-radius: 0.3em;
                font-family: sans-serif;  width: 30%; height: 100%; min-width: 100%;
                margin-left: 0em;margin-top: 0.5em; font-size:100%;">{text}</span>"""

    col.markdown(text_css,unsafe_allow_html=True)

# add some spacing
st.markdown("")
st.markdown("")

# divide into 2 columns
colplot1, colplot2 = st.columns([8,3])

# plotting using plotly
from plotly.graph_objs import *

# pie chart
trace1 = {
  "hole": 0.6,
  "type": "pie",
  "labels": ["Training data", "Testing data "],
  "values": [res.get("total_training_data_processed"), res.get("total_test_data_processed")],
  "showlegend": False
}

fig = Figure(data= trace1)
fig.update_layout(margin = dict(l=0,r=0,t=13,b=0),   height=200)

import plotly.express as px
import pandas as pd
import numpy as np

# simple line chart
dates_ , num_models= [], []
for i in range(28):
    dates_.append(f"{i+1}/08/2022" )
    num_models.append(np.random.randint(0,7))
d = pd.DataFrame({"Date":dates_, "Models":num_models})
d["Date"] = pd.to_datetime(d["Date"], dayfirst = True)
d["Num_models"] = np.cumsum(d["Models"])


colplot2.markdown("##### Train and Test Data Processed", )
colplot2.plotly_chart(fig, theme="streamlit", use_container_width=True)

import plotly.graph_objects as go

# stacked histogram

fig3 = go.Figure()

fig3.update_layout(margin = dict(l=0,r=160,t=20,b=40),  bargap = 0.6)
fig3.add_trace(go.Bar(
    y=['Object detection', 'Image segmentation', 'Classification'],
    x=[5, 5, 10],
    name='Running',
    orientation='h',
    marker=dict(
        color='rgba(30, 194, 12, 0.8)',
        line=dict(color='rgba(18, 105, 8, 1.0)', width=1)
    )
))
fig3.add_trace(go.Bar(
    y=['Object detection', 'Image segmentation', 'Classification'],
    x=[2, 4, 1],
    name='Training',
    orientation='h',
    marker=dict(
        color='rgba(66, 97, 235, 0.8)',
        line=dict(color='rgba(44, 62, 145, 1.0)', width=1)
    )
))

fig3.add_trace(go.Bar(
    y=['Object detection', 'Image segmentation', 'Classification'],
    x=[12,15,18],
    name='Stopped',
    orientation='h',
    marker=dict(
        color='rgba(227, 79, 61 0.8)',
        line=dict(color='rgba(125, 27, 15, 1.0)', width=1)
    )
))

fig3.update_layout(barmode='stack', height=220,yaxis = dict(tickfont = dict(size=16)))


colplot1.markdown("##### Projects")

colplot1.plotly_chart(fig3, theme="streamlit", use_container_width=True)

colplot21, colplot22 = st.columns([6,4])

fig2 = px.line(d, x="Date", y="Num_models")


colplot21.markdown("##### Total Models trained over time")
colplot21.plotly_chart(fig2, theme="streamlit", use_container_width=True)
