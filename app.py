
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("report_data.csv")

# Sidebar - user selections
st.sidebar.header("Focal Company Selection")
focal_company = st.sidebar.selectbox("Select a focal company:", df['name'].dropna().unique())

benchmark_type = st.sidebar.radio("Benchmark by:", ["Country", "Economic Sector"])
benchmark_value = None

if benchmark_type == "Country":
    country = df.loc[df['name'] == focal_company, 'country'].values[0]
    benchmark_value = country
    benchmark_df = df[df['country'] == country]
elif benchmark_type == "Economic Sector":
    sector = df.loc[df['name'] == focal_company, 'trbceconomicsectorname'].values[0]
    benchmark_value = sector
    benchmark_df = df[df['trbceconomicsectorname'] == sector]

# Title
st.title("PDF Report Page Distribution")

# Histogram plot
st.subheader(f"Distribution of Pages ({benchmark_type}: {benchmark_value})")

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(benchmark_df['pagespdf'], bins=20, kde=False, ax=ax, color='lightgray')
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]
ax.axvline(focal_pages, color='red', linestyle='--', label=f"{focal_company} ({focal_pages} pages)")
ax.set_xlabel("Number of Pages in PDF Report")
ax.set_ylabel("Number of Companies")
ax.legend()

st.pyplot(fig)

# Table for transparency
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf']].sort_values(by='pagespdf'))
