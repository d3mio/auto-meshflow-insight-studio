import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title='MeshFlow Insight Studio', layout='wide', initial_sidebar_state='expanded')

st.title('MeshFlow Insight Studio')
st.write('Real-time Microservice Traffic & Policy Visualizer')

# Generate random data for visualization
nodes = ['Service A', 'Service B', 'Service C', 'Service D', 'Service E']
edges = [('Service A', 'Service B'), ('Service A', 'Service C'), ('Service B', 'Service D'), ('Service C', 'Service E'), ('Service D', 'Service E')]

traffic_data = pd.DataFrame(np.random.randint(0, 100, size=(100, len(nodes))), columns=nodes)

# Sidebar controls
with st.sidebar:
    st.header('Policy Controls')
    rate_limit = st.slider('Rate Limit (requests/second)', 1, 100, 50)
    circuit_breaker = st.checkbox('Enable Circuit Breaker')
    st.markdown('---')
    st.markdown('### Live Metrics')
    metric_col1, metric_col2 = st.columns(2)
    metric_col1.metric('Requests/sec', np.random.randint(0, 100))
    metric_col2.metric('Error Rate', f'{np.random.randint(0, 10)}%')

# Main layout
col1, col2 = st.columns(2)

with col1:
    st.header('Microservice Traffic')
    st.line_chart(traffic_data)

with col2:
    st.header('Dependency Graph')
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', linewidths=1, font_size=15, arrows=True)
    st.pyplot(fig)

st.markdown('---')
st.header('Recent Traffic Logs')
st.dataframe(traffic_data.tail(10))