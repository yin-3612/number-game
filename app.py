import streamlit as st
import random

st.title("🎯 数当てゲーム")

# 答えと試行回数をセッションに保存
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1, 100)
    st.session_state.tries = 0

# 入力を受け取る
guess = st.number_input("1〜100の間で数字を入力してください", min_value=1, max_value=100, step=1)

# ボタンが押されたら判定
if st.button("判定！"):
    st.session_state.tries += 1
    if guess == st.session_state.answer:
        st.success(f"🎉 正解！{st.session_state.tries}回で当たりました！")
        if st.button("もう一度遊ぶ"):
            st.session_state.answer = random.randint(1, 100)
            st.session_state.tries = 0
    elif guess < st.session_state.answer:
        st.info("もっと大きい数字です。")
    else:
        st.info("もっと小さい数字です。")
