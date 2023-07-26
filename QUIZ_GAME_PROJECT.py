import tkinter as tk
from tkinter import filedialog

# Global variables
file_path = ""
questions = []
question_index = 0
score = 0
option_var = None

def convert_line_to_question(line):
    # Split the line into question and options
    parts = line.split(';')
    question = parts[0]
    options = parts[1:-1]  # Exclude the last element (correct answer)
    correct_answer = parts[-1].strip()

        # Format the question and options
    formatted_question = f"Q: {question.strip()}?"
    formatted_options = [option.strip() for option in options]

    return formatted_question, formatted_options, correct_answer

def check_answer():
    global score
    selected_option = option_var.get()
    correct_answer = questions[question_index][2]  # Index 2 contains the correct answer

    if selected_option == correct_answer:
        score += 1

    next_question()

def next_question():
    global question_index
    question_index += 1
    if question_index < len(questions):
        display_question(question_index)
    else:
        show_score()

def display_question(question_index):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Get the current question
    question, options, _ = questions[question_index]

    # Create a label to display the question
    question_label = tk.Label(window, text=question,font=("calibri",18))
    question_label.pack()

    # Create Radiobuttons for each option
    global option_var
    option_var = tk.StringVar()
    for option in options:
        radiobutton = tk.Radiobutton(window, text=option, variable=option_var, value=option,font=("calibri",18))
        radiobutton.pack(anchor=tk.W)

    # Create a button to move to the next question
    if question_index < len(questions) - 1:
        next_button = tk.Button(window, text="Next", command=check_answer,font=("calibri",18))
        next_button.pack()
    else:
        score_button = tk.Button(window, text="Show Score", command=check_answer,font=("calibri",18))
        score_button.pack()
def back():
     # Clear the window
    for widget in window.winfo_children():
        widget.destroy()
    window.destroy()
    main()

def show_score():
        # Clear the window
        for widget in window.winfo_children():
            widget.destroy()

        # Display the score
        score_label = tk.Label(window, text=f"Your score is : {score}/{len(questions)}",font=("calibri",20),fg="white",bg="blue")
        score_label.place(x=570,y=275)
        #main()
        l10=tk.Label(window,text="<----BACK TO HOME PAGE PRESS BELOW",font=("calibri",18),fg="black",bg="orange")
        l10.place(relx=0,rely=0,anchor='nw')
        b10= tk.Button(window, text="BACK", command=back,font=("calibri",18))
        b10.place(x=30,y=60)
        l11=tk.Label(window,text="FOR EXIT---->",font=("calibri",18),fg="black",bg="orange")
        l11.place(relx=1,rely=0,anchor='ne')
        b11= tk.Button(window, text="EXIT", command=exit,font=("calibri",18))
        b11.place(x=1300,y=50)
def set_file_path(option):
    global file_path, questions, question_index, score, window  # Include window as a global variable
    if option == 1:
        file_path = "C:/Users/gunti/OneDrive/Pictures/Desktop/internship/Myth.txt"
    elif option == 2:
        file_path = "C:/Users/gunti/OneDrive/Pictures/Desktop/internship/Coding_fundamental.txt"
    elif option == 3:
        file_path = "C:/Users/gunti/OneDrive/Pictures/Desktop/internship/Math.txt"

    questions.clear()
    with open(file_path, 'r') as file:
        for line in file:
            question, options, correct_answer = convert_line_to_question(line)
            questions.append((question, options, correct_answer))

    # Start with the first question
    question_index = 0
    score = 0
    display_question(question_index)

def main():
    global window  # Include window as a global variable
    def fun1():
        set_file_path(1)

    def fun2():
        set_file_path(2)

    def fun3():
        set_file_path(3)

    window = tk.Tk()
    window.title("Home page")
    window.minsize(width=100, height=300)

    l1 = tk.Label(window, text="Welcome to QUIZ GAME!!!", font=("calibri", 18), fg="green", bg="yellow")
    l1.pack()
    l2 = tk.Label(window, text="Please select one of the following topics", font=("calibri", 18), fg="black", bg="red")
    l2.place(x=520, y=70)

    b1 = tk.Button(window, text="Mythology", font=("calibri", 18), fg="green", bg="yellow", command=fun1)
    b1.place(x=597, y=130)

    b2 = tk.Button(window, text="Coding fundamentals", font=("calibri", 18), fg="green", bg="yellow", command=fun2)
    b2.place(x=575, y=200)

    b3 = tk.Button(window, text="Math", font=("calibri", 18), fg="green", bg="yellow", command=fun3)
    b3.place(x=620, y=270)

    window.mainloop()

if __name__ == "__main__":
    main()
