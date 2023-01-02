import streamlit as st
def app():
  st.write("수리 수정중")
  name = st.sidebar.selectbox('자료', ['선택하세요','가스켓 교체','샤워스크린 교체','오버홀'])
  
  if name == '오버홀':
    overhaul_1 ='db/overhaul/overhaul_1.jpg'
     st.image(overhaul_1,width=600)
