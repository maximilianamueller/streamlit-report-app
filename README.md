# 📊 Sustainability Report Benchmarking Dashboard

This Streamlit-based dashboard benchmarks a focal company's sustainability reporting (e.g., report length and word count) against peer firms using a variety of comparison groups and visualization types.

---

## 🎯 Purpose

This tool is built for researchers and practitioners to analyze how comprehensive a firm’s report is compared to its peers. It focuses on:
- **Number of Pages** (`pagespdf`)
- **Estimated Word Count** (`words`)

---

## ⚙️ Features

- **Select a focal company**
- **Compare to**:
  - All CSRD First Wave
  - Country Peers
  - Sector Peers
  - Market Cap Peers (Small/Mid/Large)
  - Rating Peers (Low/Mid/High)
- **Chart types**:
  - Strip Plot (interactive with red dot + tooltip)
  - Violin Plot (clean, hover disabled)
  - Histogram
  - Bar Chart (benchmark average + red line for focal)

---

## 📁 File Structure

```
📦 benchmark-app/
├── app.py                # Main Streamlit app
├── report_data.csv       # Input data with company-level metrics
├── requirements.txt      # Dependencies for local or Streamlit Cloud
└── README.md             # This file
```

---

## 🔍 Data Columns (report_data.csv)

| Column                 | Description                                      |
|------------------------|--------------------------------------------------|
| `name`                 | Company name                                     |
| `country`              | Country of registration                          |
| `trbceconomicsectorname` | Sector (TRBC-style naming)                   |
| `pagespdf`             | PDF page count of the sustainability report      |
| `words`                | Estimated word count                             |
| `market_cap_tercile`   | Market cap tercile (1=Small, 3=Large)            |
| `rating_tercile`       | ESG rating tercile (1=Low, 3=High)               |

---

## 🚀 Run Locally

1. **Clone the repo**:
```bash
git clone https://github.com/YOUR_ORG/benchmark-app.git
cd benchmark-app
```

2. **Create and activate a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the app**:
```bash
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push all files (`app.py`, `report_data.csv`, `requirements.txt`) to GitHub.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click “New app” → select your repo.
4. Deploy. Done!

The app auto-refreshes when changes are pushed.

---

## 🧪 Ideas for Future Work

Here are things your team can improve or add:

- 📌 Add KPI-level benchmarking (e.g., ESRS datapoint coverage)
- 🔄 Add ability to select **multiple filters** (e.g., same country + sector)
- 📈 Add **historical report growth** (multi-year data support)
- 📤 Add **downloadable summary reports**
- 🔐 Add **login access** for internal vs. public view
- 📊 Add KPI scatter plots (pages vs. emissions, etc.)

---

## 🤝 Handover Notes

PhD students: This app is production-ready and fully functional.
You can:
- Edit or replace `report_data.csv`
- Modify `app.py` to add features
- Clone the repo to create your own dashboard variants

Start with `app.py`, and let Streamlit rerun on save (`streamlit run app.py`).

---

## 🧾 License

MIT License. Use and extend freely.

---

## 🙋 Need Help?

Contact your project advisor or team lead.

---