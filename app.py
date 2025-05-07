import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("report_data.csv")

# Sidebar - user selections
st.sidebar.header("Focal Company Selection")
focal_company = st.sidebar.selectbox("Select a focal company:", df['name'].dropna().unique())

# Benchmark selection
st.sidebar.header("Benchmark Group")
benchmark_type = st.sidebar.radio("Compare to:", ["All Firms", "Country", "Economic Sector"])

if benchmark_type == "All Firms":
    benchmark_df = df
    benchmark_label = "All Firms"
elif benchmark_type == "Country":
    country = df.loc[df['name'] == focal_company, 'country'].values[0]
    benchmark_df = df[df['country'] == country]
    benchmark_label = f"Country: {country}"
else:  # Economic Sector
    sector = df.loc[df['name'] == focal_company, 'trbceconomicsectorname'].values[0]
    benchmark_df = df[df['trbceconomicsectorname'] == sector]
    benchmark_label = f"Sector: {sector}"

# Plot type selection
st.sidebar.header("Chart Type")
plot_type = st.sidebar.radio("Select plot type:", ["Strip Plot", "Violin Plot", "Histogram"])

# Title
st.title("PDF Report Page Comparison")
st.subheader(f"Distribution of Pages ({benchmark_label})")

# Focal value
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

if plot_type == "Strip Plot":
    sns.stripplot(data=benchmark_df, x='pagespdf', size=8, jitter=True, ax=ax, color='gray')
    ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
    ax.set_xlabel("Number of Pages")
    ax.set_yticks([])

elif plot_type == "Violin Plot":
    sns.violinplot(data=benchmark_df, x='pagespdf', ax=ax, inner="box", color='lightgray')
    ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
    ax.set_xlabel("Number of Pages")
    ax.set_yticks([])

elif plot_type == "Histogram":
    sns.histplot(benchmark_df['pagespdf'], bins=20, kde=False, ax=ax, color='lightgray')
    ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
    ax.set_xlabel("Number of Pages")
    ax.set_ylabel("Number of Companies")

ax.legend()
st.pyplot(fig)

# Table
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf']].sort_values(by='pagespdf'))