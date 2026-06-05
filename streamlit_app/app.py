import streamlit as st
import pandas as pd


# PAGE CONFIG
st.set_page_config(
    page_title="Demand Forecasting Dashboard",
    layout="wide"
)


# LOAD DATA
df = pd.read_csv(
    "processed_data/inventory_recommendations.csv"
)


# TITLE
st.title(
    "Demand Forecasting & Inventory Optimization"
)

st.write(
    "AI-powered demand forecasting and inventory planning dashboard."
)


# KPI SECTION
st.subheader("Business KPIs")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

# Total Products
col1.metric(
    "Total Products",
    df["item"].nunique()
)

# Total Stores
col2.metric(
    "Total Stores",
    df["store"].nunique()
)

# Reorder Required
col3.metric(
    "Reorder Required",
    (df["inventory_status"] == "Reorder Required").sum()
)

# Healthy Inventory
col4.metric(
    "Healthy Inventory",
    (df["inventory_status"] == "Healthy").sum()
)

# Inventory Risk %
risk_percent = round(
    (
        (df["inventory_status"] == "Reorder Required").sum()
        / len(df)
    ) * 100,
    2
)

col5.metric(
    "Inventory Risk %",
    f"{risk_percent}%"
)

# Average Forecast
avg_forecast = round(
    df["forecast_demand"].mean(),
    2
)

col6.metric(
    "Avg Forecast",
    avg_forecast
)

# Highest Risk Store
risk_store = (
    df[df["inventory_status"] == "Reorder Required"]
    ["store"]
    .value_counts()
    .idxmax()
)

col7.metric(
    "Highest Risk Store",
    risk_store
)


# BUSINESS INSIGHT
st.info(
    f"""
    Inventory Risk Analysis:

    {risk_percent}% of store-item combinations currently require replenishment.
    Store {risk_store} has the highest number of products needing inventory action.
    """
)


# FILTERS
st.subheader("Filters")

selected_store = st.selectbox(
    "Select Store",
    sorted(df["store"].unique())
)

filtered_df = df[
    df["store"] == selected_store
]


# INVENTORY RECOMMENDATIONS TABLE
st.subheader("Inventory Recommendations")

st.dataframe(
    filtered_df[
        [
            "store",
            "item",
            "forecast_demand",
            "reorder_point",
            "inventory_status"
        ]
    ],
    use_container_width=True
)


# INVENTORY STATUS BREAKDOWN
st.subheader(
    "Inventory Status Breakdown"
)

status_counts = (
    df["inventory_status"]
    .value_counts()
)

status_df = status_counts.reset_index()

status_df.columns = [
    "Inventory Status",
    "Count"
]

st.dataframe(
    status_df,
    use_container_width=True
)

st.bar_chart(
    status_counts
)


# FORECAST DISTRIBUTION


st.subheader(
    "Forecast Demand Distribution"
)

st.bar_chart(
    filtered_df
    .set_index("item")["forecast_demand"]
)


# FOOTER
st.markdown("---")

st.caption(
    "Built using Streamlit, XGBoost, FastAPI and Time Series Forecasting"
)