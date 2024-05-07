############################################################################

st.sidebar.write(f'f(x) = A * x^4 + B * x^3 + C * x^2 + D * x')

a = st.sidebar.slider('A', value=1, min_value=-10, max_value=10, step=1)
b = st.sidebar.slider('B', value=1, min_value=-10, max_value=10, step=1)
c = st.sidebar.slider('C', value=1, min_value=-10, max_value=10, step=1)
d = st.sidebar.slider('D', value=1, min_value=-10, max_value=10, step=1)

############################################################################

# Sidebarの選択肢を定義する
options = ["Option 1", "Option 2", "Option 3"]
choice = st.sidebar.selectbox("Select an option", options)

# Mainコンテンツの表示を変える
if choice == "Option 1":
    st.write("You selected Option 1")
elif choice == "Option 2":
    st.write("You selected Option 2")
else:
    st.write("You selected Option 3")

############################################################################
