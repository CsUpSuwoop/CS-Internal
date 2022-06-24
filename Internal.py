

from tkinter import *
from tkinter import ttk

root=Tk()
#def callback():
  #  val1=entry.get()
  #  val2=entryIH.get()
  #  val3=entry_row.get()
   # print("Customer's full name :" +val1)
   # print("Customer's recipet number:" +val2)
   # print("row numbers#:" +val3)
   # if chvar.get()==1:
    #print("balloons")

customer_details = []



def quit():
    root.destroy()

    

def append_details():
    global total_entries, entry, entry1, entryIH, entry_quantity
    # append each item to its own area of the list
    customer_details.append([entry.get(), entry1.get(), entryIH.get(), entry_quantity.get()])
    #clear the boxes
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entryIH.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    total_entries += 1



    
def print_details():
    name_count = 0
    # Create the column headings
    Label(root, font=("Helvetica 10 bold"),text="Row").grid(column=0, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Customer Name").grid(column=1, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Item hired").grid(column=2, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Item Quantity").grid(column=3, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Reciept number").grid(column=4, row=9)
# add each item in the list into its own row
    while name_count < total_entries:
        Label(root, text=name_count).grid(column=0, row=name_count+10)
        Label(root, text=(customer_details[name_count][0])).grid(column=1, row=name_count+10)
        Label(root, text=(customer_details[name_count][1])).grid(column=4, row=name_count+10)
        Label(root, text=(customer_details[name_count][2])).grid(column=2, row=name_count+10)
        Label(root, text=(customer_details[name_count][3])).grid(column=3, row=name_count+10)
        name_count += 1
        print(name_count)


def delete_row ():
    #these are the global variable(s)
    global total_entries, delete_item, customer_details
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())] 
    total_entries -= 1
    name_count = 0
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(root, text="                    ").grid(column=0, row=name_count+10) 
    Label(root, text="                    ").grid(column=1, row=name_count+10)
    Label(root, text="                    ").grid(column=2, row=name_count+10)
    Label(root, text="                    ").grid(column=3, row=name_count+10)
    Label(root, text="                    ").grid(column=4, row=name_count+10)

    Label(root, text="                    ").grid(column=0, row=name_count+11) 
    Label(root, text="                    ").grid(column=1, row=name_count+11)
    Label(root, text="                    ").grid(column=2, row=name_count+11)
    Label(root, text="                    ").grid(column=3, row=name_count+11)
    Label(root, text="                    ").grid(column=4, row=name_count+11)

    Label(root, text="                    ").grid(column=0, row=name_count+12) 
    Label(root, text="                    ").grid(column=1, row=name_count+12)
    Label(root, text="                    ").grid(column=2, row=name_count+12)
    Label(root, text="                    ").grid(column=3, row=name_count+12)
    Label(root, text="                    ").grid(column=4, row=name_count+12)

    Label(root, text="                    ").grid(column=0, row=name_count+13) 
    Label(root, text="                    ").grid(column=1, row=name_count+13)
    Label(root, text="                    ").grid(column=2, row=name_count+13)
    Label(root, text="                    ").grid(column=3, row=name_count+13)
    Label(root, text="                    ").grid(column=4, row=name_count+13)

    Label(root, text="                    ").grid(column=0, row=name_count+14) 
    Label(root, text="                    ").grid(column=1, row=name_count+14)
    Label(root, text="                    ").grid(column=2, row=name_count+14)
    Label(root, text="                    ").grid(column=3, row=name_count+14)
    Label(root, text="                    ").grid(column=4, row=name_count+14)
    #print all the items in the list
    print_details()
 


#set up error messages if entry boxes are left empty    
def check_inputs():
    input_check = 0
    Label(root, text="      ") .grid(column=3, row=1)
    Label(root, text="      ") .grid(column=3, row=2)
    Label(root, text="      ") .grid(column=5, row=6)
    Label(root, text="      ") .grid(column=3, row=4)
    # Check that Full name is not blank, set error text if blank
    if len(entry.get()) == 0:
        Label(root, fg="red", text="Required").grid(column=2, row=1)
        input_check = 1
    if len(entry.get()) > 0:
        Label(root, text = "                  ").grid(column=2, row=1)
        input_check = 1
    # Check that reciept number is not blank, set error text if blank
    if len(entry1.get()) == 0:
        Label(root, fg="red", text="Required").grid(column=2, row=2)
        input_check = 1
    if len(entry1.get()) > 0:
        Label(root, text = "                  ").grid(column=2, row=2)
        input_check = 1
    #check that reciept number does not have a letter in it, set error message if it does
    if len(entry1.get()) != 0:
        if entry1.get().strip().isdecimal() == False:
            input_check = 1
            Label(root, text="No letters, only numbers", fg="red") .grid(row=2, column=2)
        if entry1.get().strip().isdecimal() == True:
            Label(root, text = "                  ").grid(column=2, row=2)
            input_check = 1
            
    
    # Check the item quantity is not blank and between 1 and 500, set error text if blank
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) < 1: 
            Label(root, fg="red", text="1-500 only").grid(column=2, row=4)
        if int(entry_quantity.get()) > 500:
            Label(root, fg="red", text="1-500 only").grid(column=2, row=4)
            input_check = 1
            
    else:
        Label(root, fg="red", text="1-500 only") .grid(column=2, row=4)
        input_check = 1
    if len(entry_quantity.get()) > 1:
        Label(root, text = "                  ").grid(column=2, row=4)
        input_check = 1

    # Check that item hired is not blank, set error text if blank
    if len(entryIH.get()) == 0:
        Label(root, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if len(entryIH.get()) > 0:
        Label(root, text = "                  ").grid(column=2, row=3)
        input_check = 1
    #append details if all requirements are met
    if len(entry.get()) > 0:
        if input_check == 1:
            if len(entry1.get()) > 0:
                if entry1.get().strip().isdecimal() == True:
                    if int(entry_quantity.get()) > 1:
                        if int(entry_quantity.get()) < 501:
                            if len(entryIH.get()) > 0:
                                append_details()


#create entry box for customer name, receipt number
entry = ttk.Entry(root, width=23)
entry1 = ttk.Entry(root, width=23)
entryIH = ttk.Entry(root, width=23)
entry_quantity = ttk.Entry(root, width=23)
delete_item = ttk.Entry(root, width=23)






entry.grid(row=1, column=1)
entry1.grid(row=2, column=1)
entryIH.grid(row=3, column=1)
entry_quantity.grid(row=4, column=1)
delete_item.grid(row=5, column=1)



#Create/add buttons 
buttonROW = ttk.Button(root, text="Delete row", command=delete_row)
buttonAP = ttk.Button(root, text="Append details", command=check_inputs)
buttonPRNT = ttk.Button(root, text="Print details", command=print_details)
buttonQUIT = ttk.Button(root, text="Quit", command=quit)


buttonROW.grid(row=7, column=3, sticky=W+E, pady=5)
buttonAP.grid(row=7, column=0, sticky=W+E, pady=5)
buttonPRNT.grid(row=7, column=1, sticky=W+E, pady=5)
buttonQUIT.grid(row=7, column=2, sticky=W+E, pady=5)


#create labels 
lbltitle = ttk.Label(root, text="Julies Party Hire", font=(("Arial"), 22))
lblname= ttk.Label(text="Enter Your Name:")
lblreciept = ttk.Label(text="Reciept Number:")
lblitemH = ttk.Label(text="Item Hired: ")
lblquantity = ttk.Label(text="Item # quantity: ")
lblrow = ttk.Label(text="Row number: ")

lbltitle.grid(row=0, column= 0, columnspan=2)
lblname.grid(row=1, column=0, sticky=E)
lblreciept.grid(row=2, column=0)
lblitemH.grid(row=3, column=0)
lblquantity.grid(row=4, column=0)
lblrow.grid(row=5, column=0)


total_entries = 0


#combo box
#items = StringVar()
#item_hired = ttk.Combobox(root, state="readonly", textvariable=items, values=("balloon", "tables", "streamers", "balloon pump", "party poppers", "party hat", "gift wrapping paper", "birthday cards" )) .grid(row=3, column=1)


root.geometry("500x450")
root.mainloop()
