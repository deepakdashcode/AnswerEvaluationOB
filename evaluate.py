from use_gemini import getOutput

def getMarks(st: str):
    s = st.index('[')
    e = st.index(']')
    return int(st[s + 1: e]), s


with open('questions.txt') as f:
    ques = f.read().strip().split('\n')


def getResponse(ques: str, ans: str, mark: int):
    prompt = (f'I want you to help me evaluate the answers of my students and provide appropriate marks. Ignore '
              f'Grammatical Errors'
              f'The Question is'
              f'{ques}'
              f'\n'
              f'And the answer written is'
              f'{ans}'
              f'\n'
              f'The total marks are {mark}'
              f'How much should he get. Simply Give me a number. No explanations required')
    return getOutput(prompt)


questions = []
marks = []
for q in ques:
    mark, e = getMarks(q)

    questions.append(q[:e])
    marks.append(mark)

with open('answers.txt') as f:
    answers = f.read().split('\n\n\n')


for i in range(len(questions)):
    print(f'Question\n{questions[i]}'
          f'\n'
          f'Answer written is\n'
          f'{answers[i]}'
          f'\n'
          f'Total Marks = {marks[i]}\n')

    if answers[i] == 'N/A':
        print('Questions not answered. Marks Awarded is 0')
        continue

    print(getResponse(questions[i], answers[i], marks[i]))
