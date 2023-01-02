import streamlit as st

def app():
  st.write("개념 수정중")
  img='db/Mans_Machine_Concepts.png'
  
  name = st.sidebar.selectbox('자료', ['선택하세요','보일러','그룹헤드', '히팅코일','버큠벨브','3way','2way','1way','수위감지봉','지글러','펌프','모터','콘덴서','열교환기','압력스위치','메인보드'])
  if name == '선택하세요':
    st.image(img,width=600)
  
  if name == '보일러':
    st.write("보일러")
    
