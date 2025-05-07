import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

# Load data
df = pd.read_csv("report_data.csv")

# Sidebar - user selections
st.sidebar.header("Focal Company Selection")
focal_company = st.sidebar.selectbox("Select a focal company:", df['name'].dropna().unique())

# Benchmark selection
st.sidebar.header("Benchmark Group")
benchmark_type = st.sidebar.radio(
    "Compare to:",
    ["All Firms", "Country", "Economic Sector", "Market Cap Tercile", "Employee Tercile", "Rating Tercile"]
)

# Determine benchmark group
benchmark_label = "All Firms"
if benchmark_type == "All Firms":
    benchmark_df = df
elif benchmark_type == "Country":
    value = df.loc[df['name'] == focal_company, 'country'].values[0]
    benchmark_df = df[df['country'] == value]
    benchmark_label = f"Country: {value}"
elif benchmark_type == "Economic Sector":
    value = df.loc[df['name'] == focal_company, 'trbceconomicsectorname'].values[0]
    benchmark_df = df[df['trbceconomicsectorname'] == value]
    benchmark_label = f"Sector: {value}"
elif benchmark_type == "Market Cap Tercile":
    value = df.loc[df['name'] == focal_company, 'market_cap_tercile'].values[0]
    label = 'Small' if value == 1 else 'Mid' if value == 2 else 'Large'
    benchmark_df = df[df['market_cap_tercile'] == value]
    benchmark_label = f"Market Cap Group: {label}"
elif benchmark_type == "Employee Tercile":
    value = df.loc[df['name'] == focal_company, 'emp_tercile'].values[0]
    label = 'Small' if value == 1 else 'Mid' if value == 2 else 'Large'
    benchmark_df = df[df['emp_tercile'] == value]
    benchmark_label = f"Employee Size Group: {label}"
elif benchmark_type == "Rating Tercile":
    value = df.loc[df['name'] == focal_company, 'rating_tercile'].values[0]
    label = 'Low' if value == 1 else 'Mid' if value == 2 else 'High'
    benchmark_df = df[df['rating_tercile'] == value]
    benchmark_label = f"ESG Rating Group: {label}"

# Plot type selection
st.sidebar.header("Chart Type")
plot_type = st.sidebar.radio("Select plot type:", ["Strip Plot", "Violin Plot", "Histogram", "Bar Chart"])

# Title
st.title("PDF Report Benchmarking")
st.subheader(f"Distribution of Pages ({benchmark_label})")

# Focal value
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]

# Pages Plot
if plot_type == "Strip Plot":
    benchmark_df['jitter'] = 0.1 * np.random.randn(len(benchmark_df))
    fig = px.scatter(
        benchmark_df.assign(y=benchmark_df['jitter']),
        x="pagespdf",
        y='y', hover_data={"pagespdf": True, "y": False},
        hover_name="name",
        title=f"Distribution of Pages ({benchmark_label})",
        height=400
    )
    focal_point = df[df['name'] == focal_company]
    fig.add_trace(px.scatter(focal_point.assign(y=0), x='pagespdf', y='y', hover_name='name', hover_data={"pagespdf": False, "y": False}).update_traces(marker=dict(color='red', size=10)).data[0])
    fig.add_vline(
        x=focal_pages,
        line_dash="dash",
        line_color="red",
        annotation_text=f"{focal_company} ({focal_pages} pages)",
        annotation_position="top right"
    )
    fig.update_layout(yaxis=dict(visible=False), xaxis_title="Pages")
    st.plotly_chart(fig, use_container_width=True)
else:
    fig, ax = plt.subplots(figsize=(10, 6))
    if plot_type == "Violin Plot":
        sns.violinplot(data=benchmark_df, x='pagespdf', ax=ax, inner="box", color='lightgray')
        ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
        ax.set_xlabel("Number of Pages")
        ax.set_yticks([])
    elif plot_type == "Histogram":
        sns.histplot(benchmark_df['pagespdf'], bins=20, kde=False, ax=ax, color='lightgray')
        ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
        ax.set_xlabel("Number of Pages")
        ax.set_ylabel("Number of Companies")
    elif plot_type == "Bar Chart":
        avg_pages = benchmark_df['pagespdf'].mean()
        sns.barplot(x=["Benchmark Group"], y=[avg_pages], ax=ax, color='lightgray')
        ax.axhline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
        ax.set_ylabel("Number of Pages")
        ax.set_title("Pages Comparison")
    ax.legend()
    st.pyplot(fig)

# Words Plot (unchanged, still static)
if 'words' in df.columns:
    st.subheader(f"Distribution of Words ({benchmark_label})")
    focal_words = df.loc[df['name'] == focal_company, 'words'].values[0]
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    if plot_type == "Strip Plot":
        benchmark_df['jitter_words'] = 0.1 * np.random.randn(len(benchmark_df))
        fig2 = px.scatter(
        benchmark_df.assign(y=benchmark_df['jitter_words']),
            x="words",
            y='y', hover_data={"words": True, "y": False},
            hover_name="name",
            title=f"Distribution of Words ({benchmark_label})",
            height=400
        )
        focal_point2 = df[df['name'] == focal_company]
        fig2.add_trace(px.scatter(focal_point2.assign(y=0), x='words', y='y', hover_name='name', hover_data={"words": False, "y": False}).update_traces(marker=dict(color='red', size=10)).data[0])
        fig2.add_vline(
            x=focal_words,
            line_dash="dash",
            line_color="red",
            annotation_text=f"{focal_company} ({focal_words:,} words)",
            annotation_position="top right"
        )
        fig2.update_layout(
            yaxis=dict(visible=False),
            xaxis_title="Words"
        )
        st.plotly_chart(fig2, use_container_width=True)
    elif plot_type == "Violin Plot":
        sns.violinplot(data=benchmark_df, x='words', ax=ax2, inner="box", color='lightgray')
        ax2.axvline(focal_words, color='red', linestyle='--', label=f"{focal_company} ({focal_words:,} words)")
        ax2.set_xlabel("Number of Words")
        ax2.set_yticks([])
    elif plot_type == "Histogram":
        sns.histplot(benchmark_df['words'], bins=20, kde=False, ax=ax2, color='lightgray')
        ax2.axvline(focal_words, color='red', linestyle='--', label=f"{focal_company} ({focal_words:,} words)")
        ax2.set_xlabel("Number of Words")
        ax2.set_ylabel("Number of Companies")
    elif plot_type == "Bar Chart":
        avg_words = benchmark_df['words'].mean()
        sns.barplot(x=["Benchmark Group"], y=[avg_words], ax=ax2, color='lightgray')
        ax2.axhline(focal_words, color='red', linestyle='--', label=f"{focal_company} ({focal_words:,} words)")
        ax2.set_ylabel("Number of Words")
        ax2.set_title("Words Comparison")
    ax2.legend()
    st.pyplot(fig2)

# Data Table
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf', 'words']].sort_values(by='pagespdf'))