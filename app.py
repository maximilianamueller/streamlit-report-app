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


st.sidebar.header("Chart Type")
plot_type = st.sidebar.radio("Select plot type:", ["Strip Plot", "Violin Plot", "Histogram"])

# Title
st.title("PDF Report Benchmarking")
st.subheader(f"Distribution of Pages ({benchmark_label})")

# Focal values
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]

# First Plot: Pages
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

# Second Plot: Words
if 'words' in df.columns:
    st.subheader(f"Distribution of Words ({benchmark_label})")
    focal_words = df.loc[df['name'] == focal_company, 'words'].values[0]
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    if plot_type == "Strip Plot":
        sns.stripplot(data=benchmark_df, x='words', size=8, jitter=True, ax=ax2, color='gray')
        ax2.axvline(focal_words, color='red', linestyle='--', label=f"{focal_company} ({focal_words:,} words)")
        ax2.set_xlabel("Number of Words")
        ax2.set_yticks([])

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

    ax2.legend()
    st.pyplot(fig2)

# Table
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf', 'words']].sort_values(by='pagespdf'))

# ---- Bar Charts for Group Averages ----
st.subheader(f"Group Averages ({benchmark_label})")

avg_pages = benchmark_df['pagespdf'].mean()
avg_words = benchmark_df['words'].mean() if 'words' in benchmark_df.columns else None

fig3, ax3 = plt.subplots(figsize=(6, 4))
bars = ["Pages"]
values = [avg_pages]

if avg_words is not None:
    bars.append("Words")
    values.append(avg_words)

sns.barplot(x=bars, y=values, ax=ax3, palette='pastel')
ax3.set_ylabel("Average Count")
ax3.set_title("Average Report Length")
st.pyplot(fig3
# Plot type selection
st.sidebar.header("Chart Type")
plot_type = st.sidebar.radio("Select plot type:", ["Strip Plot", "Violin Plot", "Histogram", "Bar Chart"])

# Title
st.title("PDF Report Benchmarking")
st.subheader(f"Distribution of Pages ({benchmark_label})")

# Focal values
focal_pages = df.loc[df['name'] == focal_company, 'pagespdf'].values[0]

# First Plot: Pages
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

elif plot_type == "Bar Chart":
    avg_pages = benchmark_df['pagespdf'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=["Benchmark Average", "Focal Company"], y=[avg_pages, focal_pages], ax=ax, palette='pastel')
    ax.set_ylabel("Number of Pages")
    ax.set_title("Pages Comparison")

ax.legend()
st.pyplot(fig)

# Second Plot: Words
if 'words' in df.columns:
    st.subheader(f"Distribution of Words ({benchmark_label})")
    focal_words = df.loc[df['name'] == focal_company, 'words'].values[0]
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    if plot_type == "Strip Plot":
        sns.stripplot(data=benchmark_df, x='words', size=8, jitter=True, ax=ax2, color='gray')
        ax2.axvline(focal_words, color='red', linestyle='--', label=f"{focal_company} ({focal_words:,} words)")
        ax2.set_xlabel("Number of Words")
        ax2.set_yticks([])

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
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.barplot(x=["Benchmark Average", "Focal Company"], y=[avg_words, focal_words], ax=ax2, palette='pastel')
        ax2.set_ylabel("Number of Words")
        ax2.set_title("Words Comparison")

    ax2.legend()
    st.pyplot(fig2)
# Table
st.subheader("Benchmark Data")
st.dataframe(benchmark_df[['name', 'country', 'trbceconomicsectorname', 'pagespdf', 'words']].sort_values(by='pagespdf'))

# ---- Bar Charts for Group Averages ----
st.subheader(f"Group Averages ({benchmark_label})")

avg_pages = benchmark_df['pagespdf'].mean()
avg_words = benchmark_df['words'].mean() if 'words' in benchmark_df.columns else None

fig3, ax3 = plt.subplots(figsize=(6, 4))
bars = ["Pages"]
values = [avg_pages]

if avg_words is not None:
    bars.append("Words")
    values.append(avg_words)

sns.barplot(x=bars, y=values, ax=ax3, palette='pastel')
ax3.set_ylabel("Average Count")
ax3.set_title("Average Report Length")
st.pyplot(fig3)