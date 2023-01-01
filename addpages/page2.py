import streamlit as st
def app():
  st.write("설치 수정중")
  name = st.sidebar.selectbox('자료', ['선택하세요','전기','급수', '배수'])
