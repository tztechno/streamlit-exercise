st.divider()

file = st.file_uploader("画像を選択")
if file is not None:

    try:
        hc = hcd.load(file.getvalue())
      
    except Exception as e:
        st.error("ファイルの読み込みに失敗しました。未対応のファイルです。", icon="🚨")
        st.stop()

    st.success("正常にデータを読み込めました。", icon="✅")
    st.download_button("データをダウンロード", bytes(hc), file_name="converted.png")
