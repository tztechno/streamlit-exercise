####################################################################

uploaded_file = st.sidebar.file_uploader("Choose a Markdown file", type=["md"])

    if uploaded_file is not None:
        markdown_text = uploaded_file.read().decode("utf-8")
        st.markdown(f"### {uploaded_file.name}")
        st.markdown(markdown_text)

####################################################################

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(uploaded_file)

####################################################################
