// error error error

from ultralytics import YOLO
from PIL import Image

    # 画像のアップロード
    uploaded_file = st.file_uploader("画像を選択", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
      # 画像の表示
      image = Image.open(uploaded_file)
      st.image(image, caption="アップロードされた画像", use_column_width=True)

      # 画像の解析
      model = YOLO('best.pt')
      results = model.predict(image)

      # 物体検出結果の表示
      for r in results:
        im_array = r.plot(line_width=2,labels=False)  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image

      #物体検出後の画像を表示
      st.image(im, caption="検出結果",use_column_width=True)

