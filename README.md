# ☕ Coffee Shop Sales Dashboard Project

**Author:** Ambrose Henry

---

## 📌 Overview

This project analyzes a coffee shop’s sales data to uncover:
- Daily and seasonal trends
- Best-selling coffee products
- Customer payment preferences
- Sales forecasts

The insights are delivered through:
- 📊 An interactive web dashboard (Dash)
- 📄 Automated PDF, Word, and PowerPoint reports

---

## ✅ Features

- Cleaned & analyzed sales data (`index.csv`)
- Visualized trends, top products, and payment breakdowns
- Time series forecasting with Prophet
- Interactive dashboard built with Plotly Dash
- Auto-generated professional reports (PDF, Word, PPTX)

---

## 📂 Project Structure

```plaintext
Coffee-Sales-Dashboard/
│
├── data/
│   └── index.csv            # Coffee shop sales dataset
│
├── dashboard/
│   └── coffee_dash_app.py   # Interactive Dash dashboard
│
├── reports/
│   ├── create_pdf.py        # Generate PDF report
│   ├── create_word.py       # Generate Word report
│   ├── create_ppt.py        # Generate PowerPoint report
│
├── run_all.py               # Run all report generators at once
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignore temp files & outputs
├── README.md                # Project documentation (this file)

run the dependencies
pip install -r requirements.txt

 Run the Dashboard
python dashboard/coffee_dash_app.py
