# 📊 CSRD Report Benchmarking Dashboard

This Streamlit dashboard benchmarks a focal company's sustainability reporting output (PDF length and word count) against peer firms using a variety of comparison groups and interactive visualizations.

---

## 🎯 Purpose

This tool helps researchers and practitioners understand how a firm's CSRD-aligned report compares to others, especially in terms of:
- 📄 **Number of Pages**
- 📝 **Estimated Word Count**

---

## ⚙️ Features

- 🔍 **Select a focal company**
- 🧑‍🤝‍🧑 **Compare to**:
  - All CSRD First Wave
  - Country Peers
  - Sector Peers
  - Market Cap Peers (Small/Mid/Large)
  - Rating Peers (Low/Mid/High)
- 👥 **Or manually select up to 3 peer companies** to benchmark against
- 📊 **Choose from 3 chart types**:
  - **Strip Plot** (interactive scatter with hover + average line)
  - **Bar Chart** (benchmark average vs focal)
  - **Histogram** (disabled if ≤3 peers)
- 📌 Visuals include:
  - 🔴 **Dashed red line** and dot = focal company
  - ⚪ **Grey line** = average of selected peer group
- 📄 Tabular display of benchmark data

---

## 📁 Project Structure

```
📦 benchmark-app/
├── app.py                # Main Streamlit app
├── report_data.csv       # Firm-level input dataset
├── requirements.txt      # Dependencies
└── README.md             # This file
```

---

## 🔢 Data Columns (report_data.csv)

| Column                 | Description                                      |
|------------------------|--------------------------------------------------|
| `name`                 | Company name                                     |
| `country`              | Country of registration                          |
| `trbceconomicsectorname` | Sector (TRBC-style)                           |
| `pagespdf`             | PDF page count                                   |
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

2. **Set up virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install requirements**:
```bash
pip install -r requirements.txt
```

4. **Launch the app**:
```bash
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push `app.py`, `report_data.csv`, and `requirements.txt` to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New app” → select your repo → Deploy

Changes will auto-refresh with each push.

---

## 💡 Future Improvements

- Add more CSRD-specific metrics (e.g. datapoint coverage)
- Add export button for benchmarks (PDF or Excel)
- Implement KPI-level comparisons
- Allow compound filters (e.g. country + sector)

---

## 🧾 License

MIT License. Free to use, adapt, and extend.

---

## 👩‍🔬 Maintainer Notes

- Swap `report_data.csv` to update firms or metrics
- Edit `app.py` to extend logic
- Ask your advisor before pushing changes to the main branch