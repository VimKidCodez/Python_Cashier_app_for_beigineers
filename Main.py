from tkinter import *
root = Tk()
root.title("Cashier app")
root.geometry("400x500")

zero = 0

def add():
	t =tea_entry.get()
	j = juice_entry.get()
	b = bun_entry.get()
	p = Popstackle_entry.get()
	#print(int(t)*1+int(j)*8+int(b)*9+int(p)*12)
	ans = int(t)*1+int(j)*8+int(b)*9+int(p)*12
	Label_ans = Label(root,text="Sum:",font=("word","15"))
	Label_ans.place(x=90,y=400)
	answer.delete(0)
	answer.insert(0,str(ans))
	answer.place(x=150,y=400)

def clear():
	tea_entry.delete(0)
	tea_entry.insert(0,zero)
	juice_entry.delete(0)
	juice_entry.insert(0,zero)
	bun_entry.delete(0)
	bun_entry.insert(0,zero)
	Popstackle_entry.delete(0)
	Popstackle_entry.insert(0,zero)
	answer.delete(0,END)


# Ui look
Heading = Label(root,text ="Cashier app",fg = "blue",font = ("word",27))
Heading.place(x=100,y=0)

tea = Label(root,text ="Tea($1)",fg = "black",font = ("word",17))
tea.place(x=10,y=60)


juice = Label(root,text ="Juice($8)",fg = "black",font = ("word",17))
juice.place(x=10,y=120)

Bun = Label(root,text ="Bun($9)",fg = "black",font = ("word",17))
Bun.place(x=10,y=180)

Popstackle = Label(root,text ="Popstakle($12)",fg = "black",font = ("word",17))
Popstackle.place(x=10,y=240)

#--------------------------------------------------------------------------

# Entry boxes

tea_entry = Entry(root)
tea_entry.place(x=190,y=62,width=190,height=30)
tea_entry.insert(0,zero)

juice_entry = Entry(root)
juice_entry.place(x=190,y=122,width=190,height=30)
juice_entry.insert(0,zero)

bun_entry = Entry(root)
bun_entry.place(x=190,y=182,width=190,height=30)
bun_entry.insert(0,zero)

Popstackle_entry = Entry(root)
Popstackle_entry.place(x=190,y=242,width=190,height=30)
Popstackle_entry.insert(0,zero)

#---------------------------------------------------------------------------

# Add button

Button_of_add = Button(root,text="Checkout",command =add,font=("word","15"))
Button_of_add.place(x=150,y=300)


# Clear button

Button_of_clear = Button(root,text="Clear",command =clear,font=("word","15"))
Button_of_clear.place(x=150,y=350)

# Entry of answer entry
answer = Entry(root,font=("word","15"))

root.mainloop()
