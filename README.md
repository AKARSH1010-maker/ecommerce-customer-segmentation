# 📊 E-commerce Customer Segmentation Dashboard

An interactive **Streamlit dashboard** for e-commerce data cleaning, sales analytics, and **RFM-based customer segmentation**.  
This project analyzes customer behavior, identifies top-performing products, tracks sales trends, and generates **business insights** through a modern premium UI.

---

# LIVE DEMO 
 https://ecommerce-customer-segmentation1.streamlit.app/
 
---
#  Features

- Data cleaning and preprocessing
- Missing value handling
- Sales trend analysis
- Top-selling product analysis
- RFM-based customer segmentation
- Business insights and recommendations
- Upload your own CSV dataset
- Download processed data
- Premium modern UI dashboard
- Interactive filters (segment, month, country)

---

#  Project Workflow

1. Load raw or cleaned e-commerce dataset  
2. Clean data and handle missing values  
3. Generate analytics and sales insights  
4. Perform RFM customer segmentation  
5. Visualize trends and segments  
6. Display insights in dashboard  
7. Allow CSV upload & download processed outputs  

---

# 📁 Project Structure

```
ecommerce-customer-segmentation/
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── data_cleaning.py
│   ├── rfm_analysis.py
│   ├── clustering.py
│   ├── insights.py
│   └── visualization.py
│
├── outputs/
│   ├── cleaned_data.csv
│   ├── customer_segments.csv
│   ├── monthly_sales.csv
│   ├── top_items_per_month.csv
│   └── charts/
│
├── notebooks/
│   └── analysis.ipynb
│
├── data/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Dashboard Modules

## 1. Sales Analytics
- Monthly sales trend
- Revenue tracking
- Product performance
- Top selling products

## 2. Customer Segmentation
- RFM-based segmentation
- Frequency vs Monetary plot
- Segment distribution
- High-value customer identification

## 3. Business Insights
- Most common customer segment
- Best sales month
- Loyalty reward suggestion
- Re-engagement recommendation

## 4. Data Download
- Download customer segments
- Download cleaned dataset

---

# 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

# ▶️ Run Locally

## Clone repository
```bash
git clone https://github.com/AKARSH1010-maker/ecommerce-customer-segmentation.git
cd ecommerce-customer-segmentation
```

## Create virtual environment
```bash
python -m venv .venv
```

## Activate environment (Windows)
```bash
.venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run dashboard
```bash
streamlit run dashboard/app.py
```

---

# 🌐 Deployment

Deploy easily using **Streamlit Community Cloud**

Main file path:

```
dashboard/app.py
```

---

# 🔮 Future Improvements

- Auto-generate analytics from uploaded CSV
- Add advanced filters
- Add KPI cards
- Add export to PDF
- Add interactive drill-down charts
- Add customer lifetime value prediction

---

#  Author

*Akarsh Singh Sisoudia*

---
