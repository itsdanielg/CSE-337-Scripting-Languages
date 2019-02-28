import shelve
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Phonebook")
data = shelve.open("database")

def mainScreen():
    mainFrame.grid(row=0, column=0)
    mainFrame.tkraise()
    mainCreateButton.grid(row=0, column=0, padx=5, pady=5)
    mainSearchButton.grid(row=1, column=0, padx=5, pady=5)
    mainDeleteButton.grid(row=2, column=0, padx=5, pady=5)
    mainListButton.grid(row=3, column=0, padx=5, pady=5)

def mainForget():
    mainFrame.grid_forget()
    mainCreateButton.grid_forget()
    mainSearchButton.grid_forget()
    mainDeleteButton.grid_forget()
    mainListButton.grid_forget()

def insertScreen():
    mainForget()
    insertFrame.grid(row=0, column=0)
    insertFrame.tkraise()
    insertNameLabel.grid(row=0, sticky=E, padx=5, pady=5)
    insertPhoneLabel.grid(row=1, sticky=E, padx=5, pady=5)
    insertAddressLabel.grid(row=2, sticky=E, padx=5, pady=5)
    insertNameEntry.grid(row=0, column=1, padx=5, pady=5)
    insertPhoneEntry.grid(row=1, column=1, padx=5, pady=5)
    insertAddressEntry.grid(row=2, column=1, padx=5, pady=5)
    insertRadioButtonFrame.grid(row=3, columnspan=2, padx=5, pady=5)
    insertPersonalRB.grid(row=0, column=0, padx=5, pady=5)
    insertBusinessRB.grid(row=0, column=1, padx=5, pady=5)
    insertButtonFrame.grid(row=4, columnspan=2, padx=15, pady=15)
    insertSaveButton.grid(row=0, column=0, padx=5, pady=5)
    insertCancelButton.grid(row=0, column=1, padx=5, pady=5)

def insertRecord():
    name = insertNameEntry.get()
    phone = insertPhoneEntry.get()
    address = insertAddressEntry.get()
    pType = use.get()
    if not name:
        messagebox.showerror("Record Failed", "Name is empty!")
    elif not phone:
        messagebox.showerror("Record Failed", "Phone number is empty")
    elif not address:
        messagebox.showerror("Record Failed", "Address is empty!")
    elif not phone.isdigit():
        messagebox.showerror("Record Failed", "Phone number is invalid")
    else:
        values = [int(phone), address, pType]
        if name in data:
            data[name] = values
            messagebox.showinfo("Record Edit", "Record has been edited!")
        else:
            data[name] = values
            messagebox.showinfo("Record Created", "Record has been created!")
    
def insertForget():
    insertFrame.grid_forget()
    insertNameLabel.grid_forget()
    insertPhoneLabel.grid_forget()
    insertAddressLabel.grid_forget()
    insertNameEntry.grid_forget()
    insertPhoneEntry.grid_forget()
    insertAddressEntry.grid_forget()
    insertRadioButtonFrame.grid_forget()
    insertPersonalRB.grid_forget()
    insertBusinessRB.grid_forget()
    insertButtonFrame.grid_forget()
    insertSaveButton.grid_forget()
    insertCancelButton.grid_forget()
    mainScreen()

def searchScreen():
    mainForget()
    searchFrame.grid(row=0, column=0)
    searchFrame.tkraise()
    searchNameLabel.grid(row=0, sticky=E, padx=5, pady=5)
    searchNameEntry.grid(row=0, column=1, padx=5, pady=5)
    searchNameButton.grid(row=1, columnspan=2, padx=5, pady=5)
    searchNameFoundLabel.grid(row=2, columnspan=2, padx=5, pady=5)
    searchPhoneLabel.grid(row=3, columnspan=2, padx=5, pady=5)
    searchAddressLabel.grid(row=4, columnspan=2, padx=5, pady=5)
    searchTypeLabel.grid(row=5, columnspan=2, padx=5, pady=5)
    searchReturnButton.grid(row=6, columnspan=2, padx=25, pady=25)

def searchRecord():
    name = searchNameEntry.get()
    if not name:
        messagebox.showerror("Search Failed", "Name is empty!")
    else:
        if name in data:
            values = data[name]
            name = "Name: " + name
            phone = "Phone: " + str(values[0])
            address = "Address: " + values[1]
            pType = values[2]
            if pType == 1:
                pType = "Type: Personal"
            else:
                pType = "Type: Business"
            searchNameFoundLabel.config(text=name)
            searchPhoneLabel.config(text=phone)
            searchAddressLabel.config(text=address)
            searchTypeLabel.config(text=pType)
            messagebox.showinfo("Record Found", "Record has been found!")
        else:
            messagebox.showerror("Record Not Found", "Record does not exist!")

def searchForget():
    searchFrame.grid_forget()
    searchNameLabel.grid_forget()
    searchNameEntry.grid_forget()
    searchNameButton.grid_forget()
    searchNameFoundLabel.grid_forget()
    searchPhoneLabel.grid_forget()
    searchAddressLabel.grid_forget()
    searchTypeLabel.grid_forget()
    searchReturnButton.grid_forget()
    mainScreen()

def deleteScreen():
    mainForget()
    deleteFrame.grid(row=0, column=0)
    deleteFrame.tkraise()
    deleteNameLabel.grid(row=0, sticky=E, padx=5, pady=5)
    deleteNameEntry.grid(row=0, column=1, padx=5, pady=5)
    deleteNameButton.grid(row=1, columnspan=2, padx=5, pady=5)
    deleteReturnButton.grid(row=2, columnspan=2, padx=25, pady=25)

def deleteRecord():
    name = deleteNameEntry.get()
    if not name:
        messagebox.showerror("Search Failed", "Name is empty!")
    else:
        if name in data:
            del data[name]
            messagebox.showinfo("Record Deleted", "Record has been deleted!")
        else:
            messagebox.showerror("Record Not Found", "Record does not exist!")

def deleteForget():
    deleteFrame.grid_forget()
    deleteNameLabel.grid_forget()
    deleteNameEntry.grid_forget()
    deleteNameButton.grid_forget()
    deleteReturnButton.grid_forget()
    mainScreen()

def listScreen():
    mainForget()
    listFrame.grid(row=0, column=0)
    listFrame.tkraise()
    listRecords()

def listRecords():
    keyList = list(data.keys())
    frameRow = 0
    frameColumn = 0
    for key in keyList:
        values = data[key]
        name = "Name: " + key
        phone = "Phone: " + str(values[0])
        address = "Address: " + values[1]
        pType = values[2]
        if pType == 1:
            pType = "Type: Personal"
        else:
            pType = "Type: Business"
        labelRow = 0;
        recordFrame = Frame(listFrame, bg="gray")
        recordFrame.grid(row=frameRow, column=frameColumn, padx=5, pady=5)
        Label(recordFrame, text=name, font=('Helvetica', 12), bg="gray").grid(row=labelRow, columnspan=2, padx=5, pady=5)
        Label(recordFrame, text=phone, font=('Helvetica', 12), bg="gray").grid(row=labelRow+1, columnspan=2, padx=5, pady=5)
        Label(recordFrame, text=address, font=('Helvetica', 12), bg="gray").grid(row=labelRow+2, columnspan=2, padx=5, pady=5)
        Label(recordFrame, text=pType, font=('Helvetica', 12), bg="gray").grid(row=labelRow+3, columnspan=2, padx=5, pady=5)
        Label(recordFrame, text="------------------------------", font=('Helvetica', 12), bg="gray").grid(row=labelRow+4, columnspan=2, padx=5, pady=5)
        frameColumn += 1
        if frameColumn > 7:
            frameColumn = 0
            frameRow += 1
    listButton.grid(row=frameRow + 1, columnspan=8, padx=25, pady=25)


def listForget():
    children = listFrame.winfo_children()
    for widget in children:
        labels = widget.winfo_children()
        for label in labels:
            label.grid_forget()
        widget.grid_forget()
    listFrame.grid_forget()
    listButton.grid_forget()
    mainScreen()

def changeStyles():
    mainFrame.config(padx=10, pady=10, bg="gray")
    insertFrame.config(padx=10, pady=10, bg="gray")
    searchFrame.config(padx=10, pady=10, bg="gray")
    deleteFrame.config(padx=10, pady=10, bg="gray")
    listFrame.config(padx=10, pady=10, bg="gray")
    mainCreateButton.config(font=('Helvetica', 20), width=40)
    mainSearchButton.config(font=('Helvetica', 20), width=40)
    mainDeleteButton.config(font=('Helvetica', 20), width=40)
    mainListButton.config(font=('Helvetica', 20), width=40)
    insertNameLabel.config(font=('Helvetica', 20), bg="gray")
    insertPhoneLabel.config(font=('Helvetica', 20), bg="gray")
    insertAddressLabel.config(font=('Helvetica', 20), bg="gray")
    insertNameEntry.config(font=('Helvetica', 20), width=35)
    insertPhoneEntry.config(font=('Helvetica', 20), width=35)
    insertAddressEntry.config(font=('Helvetica', 20), width=35)
    insertRadioButtonFrame.config(bg="gray")
    insertPersonalRB.config(font=('Helvetica', 20), bg="gray")
    insertBusinessRB.config(font=('Helvetica', 20), bg="gray")
    insertButtonFrame.config(bg="gray")
    insertSaveButton.config(font=('Helvetica', 20))
    insertCancelButton.config(font=('Helvetica', 20))
    searchNameLabel.config(font=('Helvetica', 20), bg="gray")
    searchNameEntry.config(font=('Helvetica', 20), width=35)
    searchNameButton.config(font=('Helvetica', 20))
    searchNameFoundLabel.config(font=('Helvetica', 16), bg="gray")
    searchPhoneLabel.config(font=('Helvetica', 16), bg="gray")
    searchAddressLabel.config(font=('Helvetica', 16), bg="gray")
    searchTypeLabel.config(font=('Helvetica', 16), bg="gray")
    searchReturnButton.config(font=('Helvetica', 20))
    deleteNameLabel.config(font=('Helvetica', 20), bg="gray")
    deleteNameEntry.config(font=('Helvetica', 20), width=35)
    deleteNameButton.config(font=('Helvetica', 20))
    deleteReturnButton.config(font=('Helvetica', 20))
    listButton.config(font=('Helvetica', 20))

mainFrame = Frame(root)
insertFrame = Frame(root)
searchFrame = Frame(root)
deleteFrame = Frame(root)
listFrame = Frame(root)

mainCreateButton = Button(mainFrame, text="Create/Edit Record", command=insertScreen)
mainSearchButton = Button(mainFrame, text="Search Record", command=searchScreen)
mainDeleteButton = Button(mainFrame, text="Delete Record", command=deleteScreen)
mainListButton = Button(mainFrame, text="List Records", command=listScreen)

use = IntVar(None, 1)

insertNameLabel = Label(insertFrame, text="Name")
insertPhoneLabel = Label(insertFrame, text="Phone")
insertAddressLabel = Label(insertFrame, text="Address")
insertNameEntry = Entry(insertFrame)
insertPhoneEntry = Entry(insertFrame)
insertAddressEntry = Entry(insertFrame)
insertRadioButtonFrame = Frame(insertFrame)
insertPersonalRB = Radiobutton(insertRadioButtonFrame, text="Personal", variable=use, value=1)
insertBusinessRB = Radiobutton(insertRadioButtonFrame, text="Business", variable=use, value=2)
insertButtonFrame = Frame(insertFrame)
insertSaveButton = Button(insertButtonFrame, text="Save Record", command=insertRecord)
insertCancelButton = Button(insertButtonFrame, text="Home", command=insertForget)

searchNameLabel = Label(searchFrame, text="Name")
searchNameEntry = Entry(searchFrame)
searchNameButton = Button(searchFrame, text="Search Record", command=searchRecord)
searchNameFoundLabel = Label(searchFrame, text="Name: ")
searchPhoneLabel = Label(searchFrame, text="Phone: ")
searchAddressLabel = Label(searchFrame, text="Address: ")
searchTypeLabel = Label(searchFrame, text="Type: ")
searchReturnButton = Button(searchFrame, text="Home", command=searchForget)

deleteNameLabel = Label(deleteFrame, text="Name")
deleteNameEntry = Entry(deleteFrame)
deleteNameButton = Button(deleteFrame, text="Delete Record", command=deleteRecord)
deleteReturnButton = Button(deleteFrame, text="Home", command=deleteForget)

listButton = Button(listFrame, text="Home", command=listForget)

changeStyles()
mainScreen()
root.mainloop()
data.close()