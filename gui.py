import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from use_gemini import getOutput

def getResponse(ques: str, ans: str, mark: int):
    prompt = (
        f'I want you to help me evaluate the answers of my students and provide appropriate marks\n'
        f'The Question is:\n{ques}\n'
        f'And the answer written is:\n{ans}\n'
        f'The total marks are {mark}\n'
        f'How much should he get. Simply Give me a number. No explanations required'
    )
    # Mock function since use_gemini is not provided
    return getOutput(prompt)

def solve():
    question = question_entry.get("1.0", "end-1c")
    marks = int(marks_entry.get("1.0", "end-1c").strip())
    ans = answer_entry.get("1.0", "end-1c")
    marks_obtained = getResponse(question, ans, marks)
    result_label.config(text=marks_obtained)

# Create the main window
window = tk.Tk()
window.title('Answer Evaluation')

# Set the background color of the window
window.configure(bg='#708090')  # Change the color code as needed

# Create a styled frame with padding
frame = tk.Frame(window, bg="#333333", width=1000, height=800 )  # Change the color code as needed
frame.grid(row=0, column=0, padx=10, pady=10)

custom_font = tkfont.Font(family="Verdana", size=16,weight="bold") 
button_font = tkfont.Font(family="Verdana", size=8,weight="bold")
marks_font =  tkfont.Font(family="Verdana", size=10,weight="bold")
# Create and place widgets in the frame

# Set the relative width of the frame
frame.grid_propagate(False)  # Prevents the frame from adjusting its size based on the widgets inside
frame.update_idletasks()  # Force update to compute the frame size
rel_width = 0.8  # Adjust as needed
rel_height = 0.8  # Adjust as needed
window_width = window.winfo_width()
window_height = window.winfo_height()
frame_width = frame.winfo_width()
frame_height = frame.winfo_height()

# Set the size of the frame based on the relative width and height
frame.grid(row=0, column=0, padx=(window_width - rel_width * window_width) // 2,
           pady=(window_height - rel_height * window_height) // 2)

question_label = tk.Label(frame, text='Enter the Question ?', foreground='red', bg="#8b9dc3",font=custom_font, anchor="center")  # Change the color code as needed
question_label.grid(row=0, column=0, pady=10, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)  # Use sticky=tk.W+E+N+S to center text vertically


question_entry = Text(frame, width=1000, height=8)
question_entry.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

marks_label = tk.Label(frame, text='Enter Total Marks below :', foreground='black', bg = "#aec7e8",font=marks_font, anchor="center")  # Change the color code as needed
marks_label.grid(row=2, column=0, pady=10, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

marks_entry = tk.Text(frame, width=5, height=1, bg = "#aec7e8")
marks_entry.place(relx=0.5, rely=0.45, anchor="center")

# Insert initial text in the center
initial_text = ""
marks_entry.insert("1.0", initial_text)
marks_entry.tag_add("center", "1.0", "end")
marks_entry.tag_configure("center", justify='center')


answer_label = tk.Label(frame, text='Enter the Answer !', foreground='green',bg="#8b9dc3",font=custom_font, anchor="center",width=10)  # Change the color code as needed
answer_label.grid(row=4, column=0, pady=18, padx=5, sticky=tk.W+tk.E+tk.N+tk.S)

answer_entry = Text(frame, width=1000, height=8)
answer_entry.grid(row=5, column=0, pady=5, padx=5, sticky=tk.W)

evaluate_button = tk.Button(frame, text='Evaluate', command=solve, anchor="center",font=button_font)
evaluate_button.grid(row=6, column=0, pady=10, padx=5,sticky=tk.W+tk.E+tk.N+tk.S)

result_label = tk.Label(frame, text="", font=('Arial', 12), bg='#ffffff',anchor="center")  # Change the color code as needed
result_label.grid(row=7, column=0, pady=10, padx=5,  sticky=tk.W+tk.E+tk.N+tk.S)

# Center components in the middle
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)
frame.rowconfigure(5, weight=1)
frame.rowconfigure(6, weight=1)
frame.rowconfigure(7, weight=1)

# Center the frame in the window
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Start the Tkinter main loop
window.mainloop()
