
###################################################################

ボタンを押すことでユーザーが参加する
ボタンを押すことで関数が実行される

###################################################################

if st.button("Classify"):
    label = classify_news(news_text)
    st.write(f"The category of this news is: {label}")

###################################################################

if st.button("Shuffle"):
    shuffled_paths = shuffle_images(paths)
    for i in range(3):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(shuffled_paths[i], use_column_width=True)
        with col2:
            st.image(shuffled_paths[i+3], use_column_width=True)
        with col3:
            st.image(shuffled_paths[i+6], use_column_width=True)

###################################################################

if st.button("Predict Your Fortune"):
    times, fortune, name, images = predict()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(images[0], caption=name[0], use_column_width=True)
        st.write(f'Your {times[0]} is {name[0]}.')
        st.write(f'{fortune[0]}.')
    with col2:
        st.image(images[1], caption=name[1], use_column_width=True)
        st.write(f'Your {times[1]} is {name[1]}.')
        st.write(f'{fortune[1]}.')
    with col3:
        st.image(images[2], caption=name[2], use_column_width=True)
        st.write(f'Your {times[2]} is {name[2]}.')
        st.write(f'{fortune[2]}.')

  ###################################################################
