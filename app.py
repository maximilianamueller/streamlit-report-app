import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv("report_data.csv")

# Sidebar - user selections
st.sidebar.header("Focal Company Selection")
focal_company = st.sidebar.selectbox("Select a focal company:", df['name'].dropna().unique())

# Benchmark selection
st.sidebar.header("Benchmark Group")
benchmark_type = st.sidebar.radio(
    "Compare to:",
    ["All CSRD First Wave", "Country Peers", "Sector Peers", "Market Cap Peers", "Rating Peers"]
)

# Peer selection
peer_selection = st.sidebar.multiselect(
    "Or choose up to 3 specific peer companies:",
    options=df["name"].dropna().unique(),
    default=[],
    max_selections=3
)

# Determine benchmark group
benchmark_label = "All CSRD First Wave"
if peer_selection:
    benchmark_df = df[df["name"].isin(peer_selection)]
    benchmark_label = f"Selected Peers ({len(benchmark_df)} firms)"
elif benchmark_type == "All CSRD First Wave":
    benchmark_df = df
elif benchmark_type == "Country Peers":
    value = df.loc[df['name'] == focal_company, 'country'].values[0]
    benchmark_df = df[df['country'] == value]
    benchmark_label = f"Country Peers: {value}"
elif benchmark_type == "Sector Peers":
    value = df.loc[df['name'] == focal_company, 'trbceconomicsectorname'].values[0]
    benchmark_df = df[df['trbceconomicsectorname'] == value]
    benchmark_label = f"Sector Peers: {value}"
elif benchmark_type == "Market Cap Peers":
    value = df.loc[df['name'] == focal_company, 'market_cap_tercile'].values[0]
    label = 'Small' if value == 1 else 'Mid' if value == 2 else 'Large'
    benchmark_df = df[df['market_cap_tercile'] == value]
    benchmark_label = f"Market Cap Group: {label}"
elif benchmark_type == "Rating Peers":
    value = df.loc[df['name'] == focal_company, 'rating_tercile'].values[0]
    label = 'Low' if value == 1 else 'Mid' if value == 2 else 'High'
    benchmark_df = df[df['rating_tercile'] == value]
    benchmark_label = f"ESG Rating Group: {label}"

# Plot type selection
st.sidebar.header("Chart Type")
plot_type = st.sidebar.radio("Select plot type:", ["Strip Plot", "Bar Chart", "Histogram"])

# Title
st.title("CSRD Report Benchmarking")

# Focal values
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]
focal_words = df.loc[df['name'] == focal_company, 'words'].values[0]

# PAGES Plot
st.subheader(f"Distribution of Pages ({benchmark_label})")
if plot_type == "Strip Plot":
    benchmark_df['jitter'] = 0.1 * np.random.randn(len(benchmark_df))
    fig = px.scatter(benchmark_df.assign(y=benchmark_df['jitter']),
                     x="pagespdf", y="y", hover_name="name",
                     hover_data={"pagespdf": True, "y": False})
    fig.add_vline(x=benchmark_df["pagespdf"].mean(), line_color="lightgrey", line_width=1, opacity=0.6)
    fig.add_trace(px.scatter(df[df['name'] == focal_company].assign(y=0),
                              x="pagespdf", y="y", hover_name="name",
                              hover_data={"pagespdf": False, "y": False})
                  .update_traces(marker=dict(color='red', size=10)).data[0])
    fig.add_vline(x=focal_pages, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig.update_layout(yaxis=dict(visible=False), xaxis_title="Pages")
elif plot_type == "Histogram":
    fig = px.histogram(benchmark_df, x="pagespdf", nbins=20, hover_name="name")
        fig.add_vline(x=benchmark_df["pagespdf"].mean(), line_color="lightgrey", line_width=1, opacity=0.6)
    fig.add_vline(x=focal_pages, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig.update_layout(xaxis_title="Pages", yaxis_title="Number of Companies")
elif plot_type == "Bar Chart":
    avg_pages = benchmark_df["pagespdf"].mean()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=["Benchmark Group"], y=[avg_pages], marker_color="lightgray", name="Average"))
    fig.add_hline(y=focal_pages, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig.update_layout(yaxis_title="Pages")
st.plotly_chart(fig, use_container_width=True)

# WORDS Plot
st.subheader(f"Distribution of Words ({benchmark_label})")
if plot_type == "Strip Plot":
    benchmark_df['jitter_words'] = 0.1 * np.random.randn(len(benchmark_df))
    fig2 = px.scatter(benchmark_df.assign(y=benchmark_df['jitter_words']),
                      x="words", y="y", hover_name="name",
                      hover_data={"words": True, "y": False})
    fig2.add_vline(x=benchmark_df["words"].mean(), line_color="lightgrey", line_width=1, opacity=0.6)
    fig2.add_trace(px.scatter(df[df['name'] == focal_company].assign(y=0),
                               x="words", y="y", hover_name="name",
                               hover_data={"words": False, "y": False})
                   .update_traces(marker=dict(color='red', size=10)).data[0])
    fig2.add_vline(x=focal_words, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig2.update_layout(yaxis=dict(visible=False), xaxis_title="Words")
elif plot_type == "Histogram":
    fig2 = px.histogram(benchmark_df, x="words", nbins=20, hover_name="name")
        fig2.add_vline(x=benchmark_df["words"].mean(), line_color="lightgrey", line_width=1, opacity=0.6)
    fig2.add_vline(x=focal_words, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig2.update_layout(xaxis_title="Words", yaxis_title="Number of Companies")
elif plot_type == "Bar Chart":
    avg_words = benchmark_df["words"].mean()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=["Benchmark Group"], y=[avg_words], marker_color="lightgray", name="Average"))
    fig2.add_hline(y=focal_words, line_dash="dash", line_color="red", name=f"{focal_company}", showlegend=True)
    fig2.update_layout(yaxis_title="Words")
st.plotly_chart(fig2, use_container_width=True)

# Table
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf', 'words']].sort_values(by='pagespdf'))