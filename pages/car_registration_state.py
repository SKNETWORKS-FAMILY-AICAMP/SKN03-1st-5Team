import streamlit as st
import numpy as np
import pandas as pd

st.title('전국 자동차 등록 현황')

##커넥션 객체 생성
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
tab1, tab2, tab3 = st.tabs(["🚗 자가용", "🚚 법인용", "🚥 종합 현황"])
if not df.empty:
    st.dataframe(df)

    car_column = 'city' 
    number_of_cars_column1 = 'own_car'
    number_of_cars_column2 = 'offical_car'
    total = 'total' 

    data1 = df.set_index(car_column)[number_of_cars_column1]
    data2 = df.set_index(car_column)[number_of_cars_column2]
    data3 = df.set_index(car_column)[[number_of_cars_column1 ,number_of_cars_column2, total]]

    tab1.subheader("지역별 법인용 차 보유 현황")
    tab1.line_chart(data = data1, color='#df7aaf')

    tab2.subheader("지역별 자가차 보유 현황")
    tab2.line_chart(data = data2, color = '#bada55')

    tab3.subheader('지역별 종합 보유 현황')
    tab3.line_chart(data=data3, color = ['#bada55','#df7aaf','#7aa5c1'] )

else:
    tab1.subheader("No data available to display.")
    tab2.subheader("No data available to display.")
    tab3.subheader("No data available to display.")