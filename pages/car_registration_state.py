import streamlit as st
import numpy as np

st.title('전국 자동차 등록 현황')

# 커넥션 객체 생성
conn = st.connection("car_db", type="sql", autocommit = True) #connection. 뒤에있는것이 이름

sql = """
    select
        *
    from car_data
    where 1=1
    and usages = '0'
    and gun_gu = '계'
;
"""

df = conn.query(sql, ttl=3600)
tab1, tab2 = st.tabs(["📈 자가용", "📈 공업용"])
if not df.empty:
    st.dataframe(df)

    car_column1 = 'city' 
    number_of_cars_column1 = 'own_car' 
    
    car_column2 = 'city' 
    number_of_cars_column2 = 'offical_car' 
    
    data1 = df.set_index(car_column1)[number_of_cars_column1]
    data2 = df.set_index(car_column2)[number_of_cars_column2]

    tab1.subheader("지역별 자가용 보유 현황")
    tab1.line_chart(data1)

    tab2.subheader("지역별 공업용 보유 현황")
    tab2.line_chart(data2)

else:
    tab1.subheader("No data available to display.")
    tab2.subheader("No data available to display.")
