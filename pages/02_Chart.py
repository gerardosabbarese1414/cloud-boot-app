import streamlit as st

st.write(
    list(st.session_state.keys())
)
var = st.session_state["my_dataframe"]

mean_n_rooms_by_age = \
    st.session_state["my_dataframe"].groupby("housing_median_age").total_rooms.mean()

st.write(mean_n_rooms_by_age)

st.bar_chart(mean_n_rooms_by_age)