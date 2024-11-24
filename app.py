import streamlit as st
from db_manager import connect_db, add_transaction
from reports import get_monthly_summary
from visualizations import plot_monthly_expense

st.title("Personal Financial Tracker")

# transaction form
st.header("Add a Transaction")
date = st.date_input("Date")
type = st.selectbox("Type", ["Income", "Expense"])
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.01)
description = st.text_area("Description")
if st.button("Add Transaction"):
    add_transaction(date, type, category, amount, description)
    st.success("Transaction succesfully added!")

st.header("Monthly Summary")
month = st.selectbox("Month", ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
year = st.selectbox("Year", ["2025", "2024", "2023", "2022"])
if st.button("Show Summary"):
    summary = get_monthly_summary(month, year)
    st.write(summary)
    plot_monthly_expense(month, year)