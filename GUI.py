# using tkinter as tk(alias)
import tkinter as tk
from logic import Logic
# creating the main frame of the calculator
frame = tk.Tk()
frame.title("Calculator")
frame.geometry("354x460")
frameLabel = tk.Label(frame, text="CALCULATOR", bg='Black', font=("Lucida Calligraphy", 25, 'bold'), fg='White').pack(side=tk.TOP)
frame.config(background='Black')

# creating the entry field for user input
text_in = tk.StringVar()
text_in.set(" ")
e1 = tk.Entry(frame, textvar=text_in, width=40).pack()

#  connecting gui to logic
logic = Logic(text_in)

# creating buttons
but1 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(1), text="1", font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)

but2 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(2), text="2", font=("Courier New", 16, 'bold'))
but2.place(x=10, y=170)

but3 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(3), text="3", font=("Courier New", 16, 'bold'))
but3.place(x=10, y=240)

but4 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(4), text="4", font=("Courier New", 16, 'bold'))
but4.place(x=75, y=100)

but5 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(5), text="5", font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)

but6 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(6), text="6", font=("Courier New", 16, 'bold'))
but6.place(x=75, y=240)

but7 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(7), text="7", font=("Courier New", 16, 'bold'))
but7.place(x=140, y=100)

but8 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(8), text="8", font=("Courier New", 16, 'bold'))
but8.place(x=140, y=170)

but9 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(9), text="9", font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)

but0 = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button(0), text="0", font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)

butdot = tk.Button(frame, padx=47, pady=14, bd=4, bg='white', command=lambda: logic.click_button("."), text=".", font=("Courier New", 16, 'bold'))
butdot.place(x=75, y=310)

butpl = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button("+"), text="+", font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button("-"), text="-", font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butml = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button("*"), text="*", font=("Courier New", 16, 'bold'))
butml.place(x=205, y=240)

butdiv = tk.Button(frame, padx=14, pady=14, bd=4, bg='white', command=lambda: logic.click_button("/"), text="/", font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)

butclear = tk.Button(frame, padx=14, pady=119, bd=4, bg='white', command=logic.clear_button, text="CE", font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=100)

butequal = tk.Button(frame, padx=151, pady=14, bd=4, bg='white', command=logic.equlbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)

frame.mainloop()

