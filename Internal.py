
##### JULIES PARTY HIRE TRACKER INTERNAL ##########
# Author - Guransh Singh
# Created - 7/05/22


from tkinter import *
from tkinter import ttk


root=Tk()




customer_details= []

def quit():
    root.destroy()

    
#my append function
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



#my print details function    
def print_details():
    name_count = 0
    # Create the column headings
    Label(root, font=("Helvetica 10 bold"),text="Row").grid(column=0, row=9)
    Label(root, font=("Helvetica 10 bold"),text="Customer's Full Name").grid(column=1, row=9)
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

#my delete row function
def delete_row ():
    #these are the global variable(s)
    global total_entries, delete_item, customer_details
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())] 
    total_entries -= 1
    name_count = 0
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(root, text="                                 ").grid(column=0, row=name_count+10) 
    Label(root, text="                                 ").grid(column=1, row=name_count+10)
    Label(root, text="                                 ").grid(column=2, row=name_count+10)
    Label(root, text="                                 ").grid(column=3, row=name_count+10)
    Label(root, text="                                 ").grid(column=4, row=name_count+10)
    

    Label(root, text="                                 ").grid(column=0, row=name_count+11) 
    Label(root, text="                                 ").grid(column=1, row=name_count+11)
    Label(root, text="                                 ").grid(column=2, row=name_count+11)
    Label(root, text="                                 ").grid(column=3, row=name_count+11)
    Label(root, text="                                 ").grid(column=4, row=name_count+11)
    

    Label(root, text="                                 ").grid(column=0, row=name_count+12) 
    Label(root, text="                                 ").grid(column=1, row=name_count+12)
    Label(root, text="                                 ").grid(column=2, row=name_count+12)
    Label(root, text="                                 ").grid(column=3, row=name_count+12)
    Label(root, text="                                 ").grid(column=4, row=name_count+12)
    

    Label(root, text="                                 ").grid(column=0, row=name_count+13) 
    Label(root, text="                                 ").grid(column=1, row=name_count+13)
    Label(root, text="                                 ").grid(column=2, row=name_count+13)
    Label(root, text="                                 ").grid(column=3, row=name_count+13)
    Label(root, text="                                 ").grid(column=4, row=name_count+13)
    

    Label(root, text="                                 ").grid(column=0, row=name_count+14) 
    Label(root, text="                                 ").grid(column=1, row=name_count+14)
    Label(root, text="                                 ").grid(column=2, row=name_count+14)
    Label(root, text="                                 ").grid(column=3, row=name_count+14)
    Label(root, text="                                 ").grid(column=4, row=name_count+14)
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
        Label(root, fg="red", text="Required, do not leave this blank").grid(column=2, row=1)
        input_check += 1
    if len(entry.get()) > 0:
        Label(root, text = "                                                                  ").grid(column=2, row=1)
#check that first and last name has been entered, if only first, set up an error message
        try:
            entry.get().split(" ")[1]
            Label(root, text= "                            ").grid(column=2, row=1)
        except:
            Label(root, fg="red", text="Enter FULL name").grid(column=2, row=1)
            input_check += 1
 



# Check that reciept number is not blank, set error text if blank
    if len(entry1.get()) == 0:
        Label(root, fg="red", text="Required, do not leave this blank").grid(column=2, row=2)
        input_check += 1
    if len(entry1.get()) > 0:
        Label(root, text = "                                                    ").grid(column=2, row=2)
#check that reciept number does not have a letter in it, set error message if it does
    if len(entry1.get()) != 0:
        if entry1.get().strip().isdecimal() == False:
            input_check += 1
            Label(root, text="Do not enter letter(s), only numbers", fg="red") .grid(row=2, column=2)
        if entry1.get().strip().isdecimal() == True:
            Label(root, text = "                                                              ").grid(column=2, row=2)
            
    
# Check the item quantity is not blank and between 1 and 500, set error text if blank
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) < 1:
            Label(root, fg="red", text="Required, 1-500 only").grid(column=2, row=4)
            input_check += 1
    else:
        Label(root, fg="red", text="Required, 1-500 only") .grid(column=2, row=4)
        input_check = 1
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) > 1:
            Label(root, text="                                         ").grid(column=2, row=4)
        if int(entry_quantity.get()) < 500:
            Label(root, text="                                         ").grid(column=2, row=4)
        if int(entry_quantity.get()) > 500:
            Label(root, fg="red", text="Required, 1-500 only").grid(column=2, row=4)
            input_check += 1
        
# Check that item hired is not blank, set error text if blank
    if len(entryIH.get()) == 0:
        Label(root, fg="red", text="Required, do not leave this blank") .grid(column=2, row=3)
        input_check += 1
    if len(entryIH.get()) > 0:
        Label(root, text = "                                                              ").grid(column=2, row=3)
# make sure no integers have been entered, set error message if an integer has been entered
        if entryIH.get().isalpha() == False:
            Label(root, fg='red', text="No number(s), only letters").grid(column=2,row=3)
            input_check += 1
        if entryIH.get().isalpha() == True:
            Label(root, text="                                                                                          ").grid(column=2,row=3)
            Label(root, text="                                                                                          ").grid(column=2,row=3)


#append details if all requirements are met
        if input_check == 0:
            append_details()




#create entry box for customer name, receipt number, what item(s) they will be purchasing, quantity of item(s) 
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
lblname= ttk.Label(text="Enter Your Full Name:")
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


root.geometry("500x450+650+350")
root.mainloop()
