import streamlit as st
st.title("Hello Streamlit")
st.header("Calculate % Growth")
initial = st.number_input("Initial investment in USD")
yr = st.number_input("Growth Period in years")
growth = st.number_input("Growth Rate in %")
rate = st.number_input("Rate in %")
terminal_value = 0
current_val = initial
for year in range(int(yr)):
   current_val += growth * current_val
   terminal_value = current_val

# perform cashflow projections for the next 5 years
st.write(f'Terminal value of {initial} after {yr} years at a growth rate of {growth} is {terminal_value} and modified app.py to show {rate}')