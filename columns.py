
# 2列のカラムを作成
col1, col2 = st.columns(2)

# col1にテキストを表示
with col1:
    st.header("Column 1")
    st.write("This is column 1.")

# col2にDataFrameを表示
with col2:
    st.header("Column 2")
    # DataFrameを表示
    st.write(df)
