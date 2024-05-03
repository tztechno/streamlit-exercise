
col1, col2, col3, col4 = st.columns(4)

with col1:
    remove_newlines = st.checkbox("Newlines")
with col2:
    remove_tabs = st.checkbox("Tabs")
with col3:
    remove_leading_trailing_spaces = st.checkbox("Lead/Trail Spaces")
with col4:
    remove_all_spaces = st.checkbox("All Spaces")
