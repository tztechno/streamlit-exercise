from ultralytics import YOLO
import streamlit as st
from PIL import Image

# Streamlitアプリの設定
st.title('薬剤カウントツール')
st.write('写真中の薬剤をカウントします')

# タブを作成
tab_titles = ['Count', 'Settings']
tab1, tab2 = st.tabs(tab_titles)
 
with tab2:    
    # モデル選択のセレクトボックスを作成
    st.markdown('###')
    count_model = st.radio('剤型を選択', ['錠剤', '半錠'])
    st.markdown('###')

    # 検出力の閾値スライダーを作成
    threshold = st.slider(
    '検出力を設定（ 1 に近いほど検出しにくい）', 
    value=0.70,
    min_value=0.3,
    max_value=1.00,
    step=0.10
)

# 各タブにコンテンツを追加
with tab1:
    # 画像のアップロード
    uploaded_file = st.file_uploader("画像を選択", type=["jpg", "jpeg", "png"])
    st.warning("なるべく薬剤以外の物体が写らないようにしてください")

    if uploaded_file is not None:
      # 画像の表示
      image = Image.open(uploaded_file)
      st.image(image, caption="アップロードされた画像", use_column_width=True)

      # 物体検出の実行
      if count_model == '半錠':
        model = YOLO('best_halfTablet_240103.pt')
      else:
        model = YOLO('best_231224.pt')
    
      results = model.predict(image,conf=threshold)

      # 物体検出結果の表示
      for r in results:
        im_array = r.plot(line_width=3,labels=False)  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

      #物体検出後の画像を表示
      st.image(im, caption="検出結果",use_column_width=True)
      count_number = len(results[0])
      st.write("検出した個数は",count_number,"個です。")
    else :
       pass
