from Tkinter import*
import random
import time
import datetime
import os
from __builtin__ import str

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#===============================================================================
#                  TIME
#===============================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('TimesNewRoman',50,'bold'),text="JIET GROUP OF INSTITUTION,JODHPUR.",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('TimesNewRoman',20,'bold'),text="LACKYARD RESTAURANT ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo=Label(Tops,font=('TimesNewRoman',10,'bold'),text="Project>>>   Submitted to - Mr. BHARAT SINGH                  Submitted by - ROHIT KANSARA",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=2,column=0)

lblInfo=Label(Tops,font=('arial',15,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=3,column=0)

#===============================================================================
def Ref():
    x=random.randint(1,500876)
    randomRef=str(x)
    rand.set(randomRef)

    if (Fries.get()==""):
        CoFries=0
        CoFries_1=str(CoFries)
    else:
        CoFries=int(Fries.get())
        CoFries_1=str(CoFries)

    
    if (Noodles.get()==""):
        CoNoodles=0
        CoNoodles_1=str(CoNoodles)
    else:
        CoNoodles=int(Noodles.get())
        CoNoodles_1=str(CoNoodles)


    if (Soup.get()==""):
        CoSoup=0
        CoSoup_1=str(CoSoup)
    else:
        CoSoup=int(Soup.get())
        CoSoup_1=str(CoSoup)


    if (Burger.get()==""):
        CoBurger=0
        CoBurger_1=str(CoBurger)
    else:
        CoBurger=int(Burger.get())
        CoBurger_1=str(CoBurger)

        
    if (Sandwich.get()==""):
        CoSandwich=0
        CoSandwich_1=str(CoSandwich)
    else:
        CoSandwich=int(Sandwich.get())
        CoSandwich_1=str(CoSandwich)

     
    if (Drinks.get()==""):
        CoD=0
        CoD_1=str(CoD)
    else:
        CoD=int(Drinks.get())
        CoD_1=str(CoD)
    
    if (Name.get()==""):
        Name_1="No Name"
    else:
        Name_1=str(Name.get())
    
    if (Contact.get()==""):
        Cont="Not Given"
        Contact_1=str(Cont)
    else:
        Cont=int(Contact.get())
        Contact_1=str(Cont)    
                   
    CostofFries =CoFries * 100
    CostofDrinks=CoD * 65
    CostofSoup = CoSoup * 140
    CostofBurger = CoBurger* 260
    CostofSandwich=CoSandwich * 300
    CostofNoodles=CoNoodles*120
    
    CostofFries_1=str(CostofFries)
    CostofDrinks_1=str(CostofDrinks)
    CostofNoodles_1=str(CostofNoodles)
    CostofSoup_1=str(CostofSoup)
    CostofBurger_1=str(CostofBurger)
    CostofSandwich_1=str(CostofSandwich)
    
    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich))
    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich) * 0.2)
    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich)
    Ser_Charge= ((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich)/99)
    Service = "Rs", str ('%.2f' % Ser_Charge)
    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))
    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
    Service_ChargeAmount=str(Service)
    CostofMealAmount=str(CostofMeal)
    PaidTaxAmount=str(PaidTax)
    TotalAmout=str(OverAllCost)
#====================================Invoice File===============================
    f=open("invoice.txt","w")
    f.write("LACKYARD RESTURANT\nJODHPUR.\nCONTACT : 0291-123456")
    f.write("\n\nBill No.")
    f.write(randomRef)
    f.write("\nCustomer Name  : ")
    f.write(Name_1)
    f.write("\nContact Number : ")
    f.write(Contact_1)
    f.write("\n\n\nS.No.\t Food Name\tQty\tPrice\tAmount")
    f.write("\n1.\t  Fries   \t ")
    f.write(CoFries_1)
    f.write("\t 140\t ")
    f.write(CostofFries_1)
    f.write("\n2.\t  Noodles \t ")
    f.write(CoNoodles_1)
    f.write("\t 120\t ")
    f.write(CostofNoodles_1)
    f.write("\n3.\t  Soup     \t ")
    f.write(CoSoup_1)
    f.write("\t 140\t ") 
    f.write(CostofSoup_1)
    f.write("\n4.\t  Burger   \t ")
    f.write(CoBurger_1)
    f.write("\t 260\t ") 
    f.write(CostofBurger_1)
    f.write("\n5.\t  Sandwich\t ")
    f.write(CoSandwich_1)
    f.write("\t 300\t ")
    f.write(CostofSandwich_1)
    f.write("\n6.\t  Drinks  \t ")
    f.write(CoD_1)
    f.write("\t 65\t ")
    f.write(CostofDrinks_1)
    f.write("\n\n")
    f.write("\nCost of Meal-------: ")
    f.write(CostofMealAmount)
    f.write("\nPaid Tax 20%-------: ")
    f.write(PaidTaxAmount)
    f.write("\nService Charge 1%--: ")
    f.write(Service_ChargeAmount)
    f.write("\nTotal--------------: ")
    f.write(TotalAmout)
    f.write("\n\n\nPROJECT SUBMITTED BY - ROHIT_KANSARA\n        SUBBMITTED TO - MR. BHARAT_SINGH\n CASE LAB_IV SEM_II YEAR_2017-18.")
    f.close()    
#====================================Account File===============================
    f=open("AccountFile.txt","a")
 #   f.write("LACKYARD RESTURANT\nJODHPUR.\nCONTACT : 0291-123456\n")
    f.write("\n\nBilling Time-----:")
    f.write(localtime)
    f.write("\nBill No.")
    f.write(randomRef)
    f.write("\nCustomer Name---: ")
    f.write(Name_1)
    f.write("\nContact Number--: ")
    f.write(Contact_1)
    f.write("\nBill Amount-----: ")
    f.write(TotalAmout)
    f.close()
#===============================================================================    
def qExit():
    root.destroy()

def Print():
    os.startfile("C:/Users/ROHIT KANSARA/Documents/LiClipse Workspace/rk.py/rk.py/invoice.txt","print")

def AccountFile():
    os.system("AccountFile.txt")

def Reset():
    rand.set("") 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")
    Name.set("")
    Contact.set("")


#====================================Restaraunt Info============================
rand = StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
Name=StringVar()
Contact=StringVar()


lblReference= Label(f1, font=('arial', 16, 'bold'),text="Bill No.",bd=16,anchor="w")
lblReference.grid(row=1, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=1,column=1)

lblName= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
lblName.grid(row=2, column=0)
txtName=Entry(f1, font=('arial',16,'bold'),textvariable=Name,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtName.grid(row=2,column=1)

lblContact= Label(f1, font=('arial', 16, 'bold'),text="Contact",bd=16,anchor="w")
lblContact.grid(row=3, column=0)
txtContact=Entry(f1, font=('arial',16,'bold'),textvariable=Contact,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtContact.grid(row=3,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=16,anchor="w")
lblFries.grid(row=1, column=2)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=3)

lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
lblNoodles.grid(row=2, column=2)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=3)

lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Soup",bd=16,anchor="w")
lblSoup.grid(row=3, column=2)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=3)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Burger",bd=16,anchor="w")
lblBurger.grid(row=4, column=2)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=3)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="Sandwich",bd=16,anchor="w")
lblSandwich.grid(row=5, column=2)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=3)

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=6, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=6,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=4)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=5)

lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge 1%",bd=16,anchor="w")
lblService.grid(row=2, column=4)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=5)

lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="Tax 20%",bd=16,anchor="w")
lblStateTax.grid(row=3, column=4)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=5)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=4, column=4)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=4,column=5)

#==========================================Buttons==============================

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=3)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=1)

btnPrint=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Print",bg="powder blue",command=Print).grid(row=5,column=5)

btnAccount=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Account File",bg="powder blue",command=AccountFile).grid(row=5,column=1)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=5)

root.mainloop()