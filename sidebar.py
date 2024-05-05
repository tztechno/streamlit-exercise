
st.sidebar.write(f'f(x) = A * x^4 + B * x^3 + C * x^2 + D * x')

a = st.sidebar.slider('A', value=1, min_value=-10, max_value=10, step=1)
b = st.sidebar.slider('B', value=1, min_value=-10, max_value=10, step=1)
c = st.sidebar.slider('C', value=1, min_value=-10, max_value=10, step=1)
d = st.sidebar.slider('D', value=1, min_value=-10, max_value=10, step=1)
