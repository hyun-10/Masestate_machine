import streamlit as st
def app():
  st.write("수리 수정중")
  name = st.sidebar.selectbox('자료', ['선택하세요','가스켓 교체','샤워스크린 교체','오버홀','필터'])
  
  if name == '오버홀':
    overhaul_1 ='db/overhaul/overhaul_1.jpg'
    overhaul_2 ='db/overhaul/overhaul_2.jpg'
    overhaul_3 ='db/overhaul/overhaul_3.jpg'
    overhaul_4 ='db/overhaul/overhaul_4.jpg'
    st.image(overhaul_1,width=300)
    st.image(overhaul_2,width=300)
    st.image(overhaul_3,width=300)
    st.image(overhaul_4,width=300)
    
  if name == '필터':
    names = st.sidebar.selectbox('자료', ['선택하세요','동파'])
    if names == '동파':
      freeze_and_burst_1 = 'db/freeze and burst/filter/freeze and burst_filter_1.jpg'
      st.image(freeze_and_burst_1,width=300)
