





######### THINGS NEEDED TO DO ##########
#change the code so that all the inputs print even after they dissapear (when the append button has been clicked)

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
     #   print("balloons")

customer_details = []



def quit():
    root.destroy()

    

def append_details():
    # append each item to its own area of the list
    customer_details.append([entry.get(), entry1.get(), entryIH.get(), entry_quantity.get()])
    #clear the boxes
    entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entryIH.delete(0, 'end')
    entry_quantity.delete(0, 'end')



    
def print_details():
    name_count = 0
    # Create the column headings
    Label(root, font=("Helvetica 10 bold"),text="Row").grid(column=0, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Customer Name").grid(column=1, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Item hired").grid(column=2, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Item Quantity").grid(column=3, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Reciept number").grid(column=4, row=9)
    #make it so that the function prints the details entered in the entry box
    Label(root, font=("Helvetica 10"),text = entry.get()).grid(column=1, row=10)
    Label(root, font=("Helvetica 10"),text = entry1.get()).grid(column=4, row=10)
    Label(root, font=("Helvetica 10"),text = entryIH.get()).grid(column=2, row=10)
    Label(root, font=("Helvetica 10"),text = entry_quantity.get()).grid(column=3, row=10)
    Label(root, font=("Helvetica 10"),text = entry_row.get()).grid(column=0, row=10)

def delete_row ():
    #these are the global variables that are used
    global customer_details, delete_item, total_entries, name_count
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())]
    total_entries -= 1
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="                    ").grid(column=0,row=name_count+10) 
    Label(main_window, text="                    ").grid(column=1,row=name_count+10)
    Label(main_window, text="                    ").grid(column=2,row=name_count+10)
    Label(main_window, text="                    ").grid(column=3,row=name_count+10)
    Label(main_window, text="                    ").grid(column=4,row=name_count+10)
    #print all the items in the list
    print_customer_details()
 


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
    # Check that reciept number is not blank, set error text if blank
    if len(entry1.get()) == 0:
        Label(root, fg="red", text="Required").grid(column=2, row=2)
        input_check = 1
    
    # Check the item quantity is not blank and between 5 and 10, set error text if blank
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) < 1 or int(entry_quantity.get()) > 500:
            Label(root, fg="red", text="1-500 only").grid(column=2, row=4)
            input_check = 1
    else:
        Label(root, fg="red", text="1-500 only") .grid(column=2, row=4)
        input_check = 1

    # Check that item hired is not blank, set error text if blank
    if len(entryIH.get()) == 0:
        Label(root, fg="red", text="Required") .grid(column=2, row=3)
        input_check = 1
    if input_check == 0:
        append_details()


#create entry box for customer name, receipt number
entry = ttk.Entry(root, width=23)
entry1 = ttk.Entry(root, width=23)
entryIH = ttk.Entry(root, width=23)
entry_quantity = ttk.Entry(root, width=23)
entry_row = ttk.Entry(root, width=23)


entry.grid(row=1, column=1)
entry1.grid(row=2, column=1)
entryIH.grid(row=3, column=1)
entry_quantity.grid(row=4, column=1)
entry_row.grid(row=5, column=1)



#Create/add buttons 
buttonROW = ttk.Button(root, text="Delete row")
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
lblrow.grid(row=5
            , column=0)


total_entries = 0
#combo box
#items = StringVar()
#item_hired = ttk.Combobox(root, state="readonly", textvariable=items, values=("balloon", "tables", "streamers", "balloon pump", "party poppers", "party hat", "gift wrapping paper", "birthday cards" )) .grid(row=3, column=1)


root.geometry("500x450")
root.mainloop()
