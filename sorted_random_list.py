from tkinter import *
root=Tk()
root.title("Sorted Random List")
root.geometry("500x500")
root.configure(bg="yellow")
def sortGenerate():
    btn1["text"]="Generated Random Numbers"
    random_number=random.sample(range(0,10),5)
    label_random["text"]="Random_Numbers: "+str(random_number)
    label_random.place(relx=0.5,rely=0.5,anchor=CENTER)
    random_number.sort()
    labeL_random_sort["text"]="Sorted Random Numbers: "+str(random_number)
    labeL_random_sort.place(relx=0.5,rely=0.6,anchor=CENTER)
btn1=Button(root,text="Generate Random Numbers",bg="#4267e2",fg="white",command=sortGenerate)
btn1.place(relx=0.5,rely=0.4,anchor=CENTER)
label_random=Label(root)
labeL_random_sort=Label(root)
root.mainloop()