import tkinter
# import math
def click(event):
    global Entry_val
    text = event.widget.cget("text")
    if text == "C":
        Entry_val.set("0")
        entry.update()
    elif text == "=":
        if Entry_val.get().isdigit():
            value = Entry_val.get()
        else:
            try:
                exp = Entry_val.get()
                # exp = exp.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
                value = eval(exp)
            except Exception as e:
                value = "Error"
                print (e)
        Entry_val.set(value)
        entry.update()
    else:
        if Entry_val.get() == "0":
            Entry_val.set("")
        Entry_val.set(Entry_val.get()+text)
        entry.update()

def create_button(txt, active_back, active_fore, background, foreground):
    button = tkinter.Button(frame, text=txt, font="arial 20 bold", height=2, width=5, activebackground=active_back, activeforeground=active_fore
                            , bg=background, fg=foreground, relief=tkinter.RIDGE)
    button.pack(padx=5, pady=5, side=tkinter.LEFT)
    button.bind("<Button-1>", click)

root = tkinter.Tk()
root.title("Calculator : By Harsh Vardhan")
root.wm_iconbitmap("Calculator.ico")
root.config(background="#202020")

# set Geometry of screen
root.geometry("430x580")
root.maxsize(430, 580)
root.minsize(430, 580)

# Entry of calculator
entry_frame = tkinter.Frame(root)
entry_frame.pack()
scroll = tkinter.Scrollbar(entry_frame, orient=tkinter.HORIZONTAL)
Entry_val = tkinter.StringVar()
Entry_val.set("0")
entry = tkinter.Entry(entry_frame, textvariable=Entry_val, font="arial 30 bold", xscrollcommand=scroll.set)
entry.pack(padx=10, pady=10, fill="x", ipady=8)
scroll.pack(side=tkinter.BOTTOM, fill="x")
scroll.config(command=entry.xview)

# frame
frame = tkinter.Frame(root, background="#202020")
# create_button("sin", "orange", "white", "orange", "white")
# create_button("cos", "orange", "white", "orange", "white")
# create_button("tan", "orange", "white", "orange", "white")
create_button("C", "orange", "white", "orange", "black")
create_button("(", "orange", "white", "orange", "white")
create_button(")", "orange", "white", "orange", "white")
create_button("%", "orange", "white", "orange", "white")
frame.pack()
# frame-1
frame = tkinter.Frame(root, background="#202020")
create_button("7", "black", "orange", "black", "white")
create_button("8", "black", "orange", "black", "white")
create_button("9", "black", "orange", "black", "white")
create_button("/", "orange", "white", "orange", "white")
frame.pack()
# frame-2
frame = tkinter.Frame(root, background="#202020")
create_button("4", "black", "orange", "black", "white")
create_button("5", "black", "orange", "black", "white")
create_button("6", "black", "orange", "black", "white")
create_button("*", "orange", "white", "orange", "white")
frame.pack()
# frame-3
frame = tkinter.Frame(root, background="#202020")
create_button("1", "black", "orange", "black", "white")
create_button("2", "black", "orange", "black", "white")
create_button("3", "black", "orange", "black", "white")
create_button("+", "orange", "white", "orange", "white")
frame.pack()
# frame-4
frame = tkinter.Frame(root, background="#202020")
create_button(".", "orange", "white", "orange", "white")
create_button("0", "black", "orange", "black", "white")
create_button("=", "orange", "white", "orange", "black")
create_button("-", "orange", "white", "orange", "white")
frame.pack()
root.mainloop()