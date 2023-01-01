import streamlit as st

from add_pages import pages
from addpages import page1 as p1
from addpages import page2 as p2
from addpages import page3 as p3

app = pages()



app.add_page('에스프레소 머신 개념',p1.app)
app.add_page('에스프레소 머신 설치',p2.app)
app.add_page('에스프레소 머신 개념',p3.app)

app.run()
