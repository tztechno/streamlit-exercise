

import streamlit as st
import time

# ボタンを押したら3秒間出力を待つ
if st.button('start'):
    with st.spinner('processiong...'):
        time.sleep(3)
        st.write('end!')
