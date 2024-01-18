from tkinter import *
from use_gemini import getOutput

def getResponse(ques: str, ans: str, mark: int):
    prompt = (f'I want you to help me evaluate the answers of my students and provide appropriate marks'
              f'The Question is'
              f'{ques}'
              f'\n'
              f'And the answer written is'
              f'{ans}'
              f'\n'
              f'The total marks are {mark}'
              f'How much should he get. Simply Give me a number. No explanations required')
    return getOutput(prompt)


window = Tk()
window.title('Answer Evaluation')
# window.minsize(width=800, height=600)
l1 = Label(window, text='Enter the Question', foreground='blue')
l1.place(x=10, y=30)
v = StringVar()

e1 = Text(window, width=50, height=10)
e1.pack()
markEntry = Text(window, width=5, height=1)
markEntry.pack()
e2 = Text(window, width=50, height=10)
e2.bind('<Control-x>', lambda e: 'break')  # disable cut
e2.bind('<Control-c>', lambda e: 'break')  # disable copy
e2.bind('<Control-v>', lambda e: 'break')  # disable paste
e2.bind('<Button-3>', lambda e: 'break')  # disable right-click
e2.pack()

def solve():
    question=e1.get("1.0","end-1c")
    marks = int(markEntry.get("1.0","end-1c").strip())
    ans = e2.get("1.0","end-1c")
    MarksObtained = getResponse(question, ans, marks)
    lb.config(text=MarksObtained)

b1 = Button(window, text='Evaluate',command=solve)
b1.pack()

lb = Label(window, text="", font=('Aerial', 12))
lb.pack()

window.mainloop()
