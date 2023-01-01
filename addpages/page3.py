import streamlit as st
def app():
  st.write("수리 수정중")
  name = st.sidebar.selectbox('자료', ['선택하세요','가스켓 교체','샤워스크린 교체'])
