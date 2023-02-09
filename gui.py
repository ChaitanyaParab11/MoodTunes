import customtkinter as ck
import tkinter as tk


def combine_funcs(*funcs):
    def inner_combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
  
    return inner_combined_func
 

def fun1():
    label_2.pack(side="right", fill="both", expand=True)

  
def fun2():
    label_3.pack(side="right", fill="both", expand=True)



ck.set_appearance_mode("system")
ck.set_default_color_theme("blue")


root = ck.CTk()
root.geometry("900x500")
root.title(" MoodTunes ")
root.iconbitmap("favicon.ico")


frame1 = ck.CTkFrame(root, width=400, height=200)
label1 = ck.CTkLabel(frame1, text=" hii")
label1_1 = ck.CTkLabel(frame1, text=" hello ")
label_3 = ck.CTkLabel(frame1, text=" Changed ")
label_2 = ck.CTkLabel(frame1, text="Current song: ")
label1.pack()
label1_1.pack() 

Trainbutton = ck.CTkButton(frame1, text="Change Song", command=combine_funcs(lambda: fun1(),lambda: fun2()))
Trainbutton.pack()


frame1.pack(side="right", fill="both", expand=True)


root.mainloop()
