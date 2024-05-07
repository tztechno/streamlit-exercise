
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Warningの非表示
st.set_option('deprecation.showPyplotGlobalUse', False)

# グラフを描画する
def plot_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot()

# グラフを表示するボタンを表示する
if st.button('Plot graph'):
    plot_graph()
