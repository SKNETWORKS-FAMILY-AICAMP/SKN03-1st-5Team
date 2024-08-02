import streamlit as st

st.title('전국 자동차 등록 현황 및 기업 FAQ 조회시스템')
st.caption('파이문')
st.page_link("./pages/car_registration_state.py", label="전국 자동차 등록 현황", icon="🚗")
st.page_link("./pages/f&q.py", label="기업 FAQ 조회시스템", icon="🤔")