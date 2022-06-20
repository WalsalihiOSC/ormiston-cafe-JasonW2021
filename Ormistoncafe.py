from tkinter import *
from PIL import Image, ImageTk

class Data:
    def __init__(self, item, price): 
        """Sets the values as it goes through a list"""
        self.item = item
        self.price = price
    
    imagess = ["images/burger.png", "images/sandwich_1.png", 
        "images/teriyaki.png","images/hot_dog.png", "images/pasta.png", 
        "images/butterchicken.png", "images/fish_fingers.png",
        "images/taco.png", "images/sandwich_2.png", "images/nuggets.png", 
        "images/fries.png", "images/ice_cream.png"]
    
class GUI:
    global photos, orderlist
    photos = []
    orderlist = []

    def __init__(self, parent):
        """Creates label, entry, button widgets"""  

        self.frame = Frame(parent)
        self.frame.grid()

        self.frame1 = Frame(self.frame)
        self.frame1.grid(column=0,row=0)

        self.frame2 = Frame(self.frame)
        self.frame2.grid(column=0,row=0)   

        self.categories = Frame(self.frame2)
        self.categories.grid(row=1, padx=20)

        self.ordernow = Label(self.frame1, text="ORDER NOW", font=("Arial",20), padx=50, pady=20)
        self.ordernow.grid(row=0)

        self.startbtn = Button(self.frame1, text="START", font=("Arial",15), command=self.start, width=20, height=2, bg="green")
        self.startbtn.grid(column=0, row=1)

        self.newlabel = Label(self.frame1, text="Special", font=("Arial",15), pady=10)
        self.newlabel.grid(column=0, row=4)

        #Adds item and price 
        self.items = []
        h_file = open("ormistoncafeorders.txt")
        self.h_list = h_file.readlines()
        for line in self.h_list:
            tokens = line.split(",")
            self.items.append(Data(tokens[0],tokens[1]))
        
        #Front image
        self.image1 = Image.open("images/front.png")
        self.resize_image = self.image1.resize((280,250))
        self.img = ImageTk.PhotoImage(self.resize_image)
        self.label1 = Label(self.frame1, image=self.img)
        self.label1.image = self.img
        self.label1.grid()

        self.popularmenu = Frame(self.frame2)
        self.popularmenu.grid(row=3)

        self.newmenu = Frame(self.frame2)
        self.newmenu.grid(row=7)

        #Setups the buttons 
        for i in range(len(Data.imagess)): 
            self.image = Image.open(Data.imagess[i])
            self.resize_image = self.image.resize((100,100))
            self.img = ImageTk.PhotoImage(self.resize_image)
            photos.append(self.img)
        
        for i in range(3):
            btns = Button(self.popularmenu, image=photos[i], width=100, height=100, command=(lambda a=i:self.add(self.items[a].item)))
            btns.grid(row=0, column=i)

        x2 = range(3,6)
        for i in x2:
            btns = Button(self.popularmenu, image=photos[i], width=100, height=100, command=(lambda a=i:self.add(self.items[a].item)))
            btns.grid(row=1, column=i-3)

        x3 = range(6,9)
        for i in x3:
            btns = Button(self.newmenu, image=photos[i], width=100, height=100, command=(lambda a=i:self.add(self.items[a].item)))
            btns.grid(row=0, column=i)

        x4 = range(9,12)
        for i in x4:
            btns = Button(self.newmenu, image=photos[i], width=100, height=100, command=(lambda a=i:self.add(self.items[a].item)))
            btns.grid(row=1, column=i-3)

        self.menu = Label(self.frame2, text="MENU", font=("Arial",15))
        self.menu.grid(row=0, column=0, pady=(20,0)) 

        self.popular = Label(self.frame2, text="Popular", font=("Arial",15))
        self.popular.grid(row=2,column=0)

        self.new= Label(self.frame2, text="New", font=("Arial",15))
        self.new.grid(row=6,column=0)

        self.btnframe = Frame(self.frame2)
        self.btnframe.grid(row=8, pady=12)

        self.viewoderbtn = Button(self.btnframe, text="View Order", font=("Arial",13), command = self.next, bg="green")
        self.viewoderbtn.grid(row=8, column=2)

        self.cancelorderbtn = Button(self.btnframe, text="Cancel Order", font=("Arial",13), command = self.cancelorder, bg="red")
        self.cancelorderbtn.grid(row=8, column=0)   

        self.frame2.grid_forget()

        #Page 3
        self.frame3 = Frame(self.frame, padx=30, pady=20)
        self.frame3.grid(column=0,row=0)

        self.checkout = Label(self.frame3, text="Checkout", font=("Arial",20))
        self.checkout.grid(row=0, column=0) 

        self.paybtn = Button(self.frame3, text="Pay", command=self.pay, bg="green", font=("Arial",13),)
        self.paybtn.grid(columnspan=1, row=2)

        self.cancelorderlabel = Button(self.frame3, text="Cancel Order", command = self.cancelorder, bg="red", font=("Arial",13),)
        self.cancelorderlabel.grid(column=0,row=3)

        self.updateorderl = Button(self.frame3, text="Update Order", command = self.updateorder, bg="orange", font=("Arial",13),)
        self.updateorderl.grid(column=1,row=3)

        self.selection= Frame(self.frame3)
        self.selection.grid(row=1)

        self.frame3.grid_forget()

        #Page 4 
        self.frame4 = Frame(self.frame)
        self.frame4.grid(column=0,row=0)

        self.title4 = Frame(self.frame4)
        self.title4.grid(row=0)

        self.payment = Frame(self.frame4)
        self.payment.grid(row=1)

        self.paymentl = Label(self.title4, text="Payment", font=("Arial",13), width=15)
        self.paymentl.grid(row=1)

        self.cashbtn = Button(self.payment, text="Cash", font=("Arial",13), width=15, height=5)
        self.cashbtn.grid(row=2, column=0)

        self.eftpos = Button(self.payment, text="Eftpos", font=("Arial",13), width=15, height=5)
        self.eftpos.grid(row=2, column=1)

        self.btns4 = Frame(self.frame4)
        self.btns4.grid(row=2)

        self.gobackl = Button(self.btns4, text="Go Back", command=self.goback, bg="red", font=("Arial",13))
        self.gobackl.grid(column=0, row=1)

        self.confirm = Button(self.btns4, text="Confirm", bg="green", font=("Arial",13))
        self.confirm.grid(column=1,row=1)

        totalpricel = Label(self.btns4, text="Total: ", font=("Arial",13))
        totalpricel.grid()

        self.totalpricelab = Label(self.frame3, text="")
        self.totalpricelab.grid()

        self.frame4.grid_forget()
    
    def order(self):

        def remove(placeholder):
            orderlist.remove(placeholder)
            self.selection.destroy()
            
        #Displays the items
        self.selection.grid(row=1)

        num_ordered = 0
        total = 0 
        for i in range(len(orderlist)):
            Label(self.selection, image =None).grid(column=0, row=num_ordered)
            Label(self.selection, text=orderlist[i]).grid(column=1, row=num_ordered)
            Label(self.selection, text="$" + "5").grid(column=2, row=num_ordered)
            btn_remove = Button(self.selection, text ="Delete", bg='red', command = lambda:remove(orderlist[i]))
            btn_remove.grid(column=3, row = num_ordered)
            num_ordered +=1

    def start(self):
        '''Go to Page 2'''
        self.frame2.grid()
        self.frame1.grid_forget()

    def add(self, item):
        '''Items Ordered'''
        orderlist.append(str(item))

    def next(self):
        '''Goes to Page 3'''
        self.frame2.grid_forget()
        self.frame3.grid()
        self.order()

    def cancelorder(self):
        '''Cancel order window'''
        self.top1 = Toplevel(root)
        self.top1.geometry("200x100")
        self.top1.title("Edit")
        
        cancellabel= Label(self.top1, text="Cancel Order", font=("Arial",13),)
        cancellabel.grid()

        nobtn = Button(self.top1, text="No", command=self.cancelno, bg="red", font=("Arial",13),)
        nobtn.grid(column=0, row=1)

        yesbtn = Button(self.top1, text="Yes", command=self.cancelyes, bg ="green", font=("Arial",13),)
        yesbtn.grid(column=1, row=1)

    def cancelyes(self):
        '''Cancels order by exiting out of the window'''
        self.top1.destroy()
        root.destroy()

    def cancelno(self):
        '''Exits out of the window'''
        self.top1.destroy()

    def change(self):
        '''Go to Page 3'''
        self.frame2.grid_forget()
        self.frame3.grid()
        
    def updateorder(self):
        '''Go back to Page 2'''
        self.frame2.grid()
        self.frame3.grid_forget()

    def pay(self):
        '''Go to Page 4'''
        self.frame4.grid()
        self.frame3.grid_forget()

    def goback(self):
        ''''Go back to Page 3'''
        self.frame3.grid()
        self.frame4.grid_forget()

#main rountine
root = Tk()
file = GUI(root)
root.geometry("350x600")
root.mainloop()