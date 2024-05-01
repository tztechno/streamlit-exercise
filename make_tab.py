
import streamlit as st

st.title('title')
st.write('write')

tab_titles = ['TAB1', 'TAB2']
tab1, tab2 = st.tabs(tab_titles)
 
with tab2:    
    st.markdown('markdown')

with tab1:
    st.warning("warning")


