import tkinter as tk
# tk._test()

def print_button_action():
  print ("Hallo Welt!")

root = tk.Tk()
root.title("Titel")

# size
root.geometry("400x400")
root.minsize(width=250 , height=250)
root.maxsize(width=600 , height=600)
root.resizable(width=False, height=True)

label = tk.Label(root, text="Hello World", bg="#82FF90", fg="black").pack(side="right", expand=True, fill="both")
# label.pack()


quit_button = tk.Button(root, text ="Quit", command=root.destroy).pack()
s_button = tk.Button(root, text="print", command=print_button_action).pack()

root.mainloop()
