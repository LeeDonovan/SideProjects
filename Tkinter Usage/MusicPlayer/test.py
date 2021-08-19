from tkinter import *

tk = Tk()
frame = Frame(tk, borderwidth=10)
frame.pack(fill=BOTH, expand=3)
label = Label(frame, text="Hello There")
label.pack(fill=X, expand=1)

button = Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()