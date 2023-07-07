import streamlit as st
file ("https://docs.google.com/spreadsheets/d/1J1CxpNd1P14nA2Zp6e91FmBnhOzKL7hW/edit?usp=drive_link&ouid=108392908131352352066&rtpof=true&sd=true")
st.write(
    list(st.session_state.keys())
)
var = st.session_state["my_dataframe"]

mean_n_rooms_by_age = \
    st.session_state["my_dataframe"].groupby("housing_median_age").total_rooms.mean()

st.write(mean_n_rooms_by_age)

st.bar_chart(mean_n_rooms_by_age)
