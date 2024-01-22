import streamlit as st
from use_gemini import getOutput


def getResponse(ques: str, ans: str, mark: int):
    prompt = (f'I want you to help me evaluate the answers of my students and provide appropriate marks'
              f'The Question is\n'
              f'{ques}'
              f'\n'
              f'And the answer written is\n'
              f'{ans}'
              f'\n'
              f'The total marks are {mark}\n'
              f'Be a little liberal with the markings, and also analyze it with respect to organizational behaviour if possible\n'
              f'How much should he get. Simply Give me a number. After that explain the points where he could have improved')
    return getOutput(prompt)


ques = st.text_area(
    label='Question',
    placeholder='Enter the Question'
)

marks = st.number_input(
    label='Marks',
    placeholder='Marks',
    step=0.1
)

ans = st.text_area(
    label='Answer',
    placeholder='Enter the Answer'
)

def solve():
    st.write(getResponse(ques, ans, int(marks)))
submitButton = st.button('Submit')
if submitButton:
    solve()
