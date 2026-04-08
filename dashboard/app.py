import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")
sns.set_style("whitegrid")

st.set_page_config(
    page_title="E-commerce Customer Segmentation Dashboard",
    layout="wide"
)

# -----------------------------
# Premium Light UI Styling
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f8f6f1 0%, #eef3f8 100%);
        color: #1f2937;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Light top header bar */
    header,
    .stApp header,
    div[data-testid="stHeader"] {
        background: #f8f6f1 !important;
        background-color: #f8f6f1 !important;
        box-shadow: none !important;
        border-bottom: 1px solid #e5e7eb !important;
    }

    div[data-testid="stToolbar"] {
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }

    div[data-testid="stDecoration"] {
        background: none !important;
        background-color: transparent !important;
        background-image: none !important;
        box-shadow: none !important;
        height: 0 !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: 1400px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f7f2e9 0%, #edf3fa 100%);
        border-right: 1px solid #d9e2ec;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: #243b53 !important;
    }

    h1, h2, h3 {
        color: #1e3a5f !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px;
    }

    p {
        color: #374151;
        font-size: 16px;
    }

    div[data-testid="metric-container"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 2px 8px rgba(31, 41, 55, 0.04);
    }

    div[data-testid="metric-container"] label {
        color: #6b7280 !important;
        font-weight: 600 !important;
    }

    div[data-testid="metric-container"] > div {
        color: #1e3a5f !important;
    }

    .stDownloadButton > button,
    .stButton > button {
        background: #ffffff !important;
        color: #1e3a5f !important;
        border: 1px solid #d9e2ec !important;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(31, 41, 55, 0.06) !important;
    }

    .stDownloadButton > button:hover,
    .stButton > button:hover {
        background: #edf3fa !important;
        color: #1e3a5f !important;
        box-shadow: 0 2px 8px rgba(31, 41, 55, 0.08) !important;
    }

    div[data-baseweb="notification"] {
        background: #edf4fb !important;
        border: 1px solid #cfdceb !important;
        border-radius: 14px !important;
        color: #1e3a5f !important;
    }

    .stSelectbox > div > div,
    .stFileUploader > div {
        border-radius: 12px !important;
    }

    /* Selectbox - trigger button */
    .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
        border: 1px solid #d9e2ec !important;
        border-radius: 12px !important;
    }

    .stSelectbox [data-baseweb="select"] > div * {
        color: #1e3a5f !important;
    }

    /* Selectbox - popover dropdown menu */
    [data-baseweb="popover"] {
        background-color: #ffffff !important;
        border-radius: 14px !important;
        border: 1px solid #d9e2ec !important;
        box-shadow: 0 8px 24px rgba(31, 41, 55, 0.10) !important;
    }

    [data-baseweb="popover"] ul {
        background-color: #ffffff !important;
        border-radius: 14px !important;
    }

    [data-baseweb="popover"] li {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
    }

    [data-baseweb="popover"] li:hover {
        background-color: #edf3fa !important;
        color: #1e3a5f !important;
    }

    /* Sidebar selectbox inputs */
    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
        border: 1px solid #d9e2ec !important;
        border-radius: 10px !important;
    }

    section[data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] > div * {
        color: #1e3a5f !important;
    }

    /* File uploader box */
    .stFileUploader > div {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
        border: 1px solid #d9e2ec !important;
        border-radius: 14px !important;
    }

    .stFileUploader > div * {
        color: #1e3a5f !important;
    }

    .stFileUploader [data-testid="stFileUploaderDropzone"] {
        background-color: #ffffff !important;
        border-radius: 14px !important;
    }

    section[data-testid="stSidebar"] .stFileUploader > div,
    section[data-testid="stSidebar"] .stFileUploader [data-testid="stFileUploaderDropzone"] {
        background-color: #ffffff !important;
        border: 1px solid #d9e2ec !important;
        border-radius: 14px !important;
    }

    /* Dropdown menu list container */
    [data-baseweb="menu"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
    }

    [data-baseweb="menu"] li {
        background-color: #ffffff !important;
        color: #1e3a5f !important;
    }

    [data-baseweb="menu"] li:hover {
        background-color: #edf3fa !important;
    }

    hr {
        border: none;
        border-top: 1px solid #dbe4ee;
        margin: 1.5rem 0;
    }

    [data-testid="stExpander"] {
        background: white;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: none !important;
    }

    /* File uploader - remove dark overlay */
    .stFileUploader,
    .stFileUploader > div,
    .stFileUploader section,
    .stFileUploader [data-testid="stFileUploaderDropzone"] {
        background-color: #ffffff !important;
        box-shadow: none !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 14px !important;
        color: #1e3a5f !important;
    }

    .stFileUploader [data-testid="stFileUploaderDropzone"] button {
        background: #ffffff !important;
        color: #1e3a5f !important;
        border: 1px solid #d9e2ec !important;
        box-shadow: none !important;
    }

    /* Chart containers - light cards */
    .stPlotlyChart,
    .stPyplot {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 14px !important;
        box-shadow: 0 2px 6px rgba(31, 41, 55, 0.04) !important;
        padding: 8px !important;
    }

    /* Element containers - remove dark shadows */
    .element-container {
        box-shadow: none !important;
    }

    /* Block container children - no dark backgrounds */
    .block-container div {
        box-shadow: none;
    }

    /* Markdown blocks - ensure light */
    .stMarkdown {
        color: #1e3a5f !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    /* Metric container override */
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 16px !important;
        box-shadow: 0 2px 6px rgba(31, 41, 55, 0.04) !important;
        color: #1e3a5f !important;
    }

    /* Generic dark overlay catch-all */
    [data-baseweb="notification"],
    [data-baseweb="toast"] {
        background: #ffffff !important;
        box-shadow: 0 2px 8px rgba(31, 41, 55, 0.06) !important;
        color: #1e3a5f !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar Upload + Filters
# -----------------------------
st.sidebar.title("Filters")
st.sidebar.header("Upload Your Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload E-commerce CSV File",
    type=["csv"]
)

# -----------------------------
# Load Data
# -----------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Custom dataset uploaded successfully!")
else:
    df = pd.read_csv("outputs/cleaned_data.csv")
    st.sidebar.info("Using default cleaned dataset")

rfm = pd.read_csv("outputs/customer_segments.csv")
monthly_sales = pd.read_csv("outputs/monthly_sales.csv")
top_items_per_month = pd.read_csv("outputs/top_items_per_month.csv")

# -----------------------------
# Sidebar Filters
# -----------------------------
segment_filter = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + list(rfm["Segment"].dropna().unique())
)

month_filter = st.sidebar.selectbox(
    "Month",
    ["All"] + list(monthly_sales["Month"].dropna().unique())
)

country_filter = st.sidebar.selectbox(
    "Country",
    ["All"] + list(df["Country"].dropna().unique())
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df.copy()
filtered_rfm = rfm.copy()
filtered_monthly_sales = monthly_sales.copy()
filtered_top_items_per_month = top_items_per_month.copy()

if country_filter != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country_filter]

if segment_filter != "All":
    filtered_rfm = filtered_rfm[filtered_rfm["Segment"] == segment_filter]

if month_filter != "All":
    filtered_monthly_sales = filtered_monthly_sales[
        filtered_monthly_sales["Month"] == month_filter
    ]
    filtered_top_items_per_month = filtered_top_items_per_month[
        filtered_top_items_per_month["Month"] == month_filter
    ]

# -----------------------------
# Premium Header Banner
# -----------------------------
st.markdown("""
<div style="
    background: linear-gradient(135deg, #1e3a5f, #355c7d, #c9a227);
    padding: 30px 34px;
    border-radius: 24px;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    margin-bottom: 28px;
">
    <h1 style="margin:0; color:white; font-size:42px; font-weight:800;">
        📊 E-commerce Customer Segmentation Dashboard
    </h1>
    <p style="margin-top:10px; font-size:18px; color:#f8f9fb;">
        Advanced sales analytics, RFM-based customer segmentation, product insights, and strategic business recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹ {filtered_df['TotalPrice'].sum():,.2f}")
col2.metric("Total Customers", filtered_df["CustomerID"].nunique())
col3.metric("Total Products", filtered_df["Description"].nunique())
col4.metric("Transactions", filtered_df["InvoiceNo"].nunique())

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Sales Charts
# -----------------------------
st.markdown("## 📈 Sales Analytics")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div style="
        background:white;
        padding:18px;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(31, 41, 55, 0.08);
        border:1px solid #e8edf3;
    ">
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(
        filtered_monthly_sales["Month"],
        filtered_monthly_sales["TotalPrice"],
        marker="o",
        linewidth=2.5
    )
    plt.xticks(rotation=45)
    ax.set_title("Monthly Sales Trend", fontsize=15, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="
        background:white;
        padding:18px;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(31, 41, 55, 0.08);
        border:1px solid #e8edf3;
    ">
    """, unsafe_allow_html=True)

    top_products = (
        filtered_df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
    ax.set_title("Top Selling Products", fontsize=15, fontweight="bold")
    ax.set_xlabel("Quantity Sold")
    ax.set_ylabel("Product")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Top Item Per Month
# -----------------------------
st.markdown("## 🏆 Top Selling Item Per Month")

st.markdown("""
<div style="
    background:white;
    padding:18px;
    border-radius:20px;
    box-shadow:0 8px 24px rgba(31, 41, 55, 0.08);
    border:1px solid #e8edf3;
">
""", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(10, 4.5))
sns.barplot(
    data=filtered_top_items_per_month,
    x="Month",
    y="Quantity",
    ax=ax
)
plt.xticks(rotation=45)
ax.set_title("Top Selling Item Per Month", fontsize=15, fontweight="bold")
plt.tight_layout()
st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Customer Segmentation
# -----------------------------
st.markdown("## 👥 Customer Segmentation")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div style="
        background:white;
        padding:18px;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(31, 41, 55, 0.08);
        border:1px solid #e8edf3;
    ">
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.scatterplot(
        data=filtered_rfm,
        x="Frequency",
        y="Monetary",
        hue="Segment",
        ax=ax
    )
    ax.set_title("Frequency vs Monetary by Segment", fontsize=15, fontweight="bold")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="
        background:white;
        padding:18px;
        border-radius:20px;
        box-shadow:0 8px 24px rgba(31, 41, 55, 0.08);
        border:1px solid #e8edf3;
    ">
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.countplot(
        data=filtered_rfm,
        x="Segment",
        ax=ax
    )
    plt.xticks(rotation=20)
    ax.set_title("Customer Segment Count", fontsize=15, fontweight="bold")
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Auto Business Insights
# -----------------------------
st.markdown("## 💡 Business Insights")

top_segment = rfm["Segment"].value_counts().idxmax()
best_month = monthly_sales.loc[
    monthly_sales["TotalPrice"].idxmax()
]["Month"]

st.info(f"Most customers belong to **{top_segment}** segment")
st.info(f"Highest sales occurred in **{best_month}**")
st.info("High Value Customers should receive loyalty rewards")
st.info("At Risk Customers should receive re-engagement offers")

# -----------------------------
# Download Button
# -----------------------------
st.markdown("## ⬇ Download Data")

d1, d2 = st.columns(2)

with d1:
    st.download_button(
        "Download Customer Segments",
        rfm.to_csv(index=False),
        file_name="customer_segments.csv",
        mime="text/csv"
    )

with d2:
    st.download_button(
        "Download Cleaned Data",
        df.to_csv(index=False),
        file_name="cleaned_data.csv",
        mime="text/csv"
    )