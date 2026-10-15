# PURWADHIKA JC OL DATA SCIENCE
# CAPSTONE PROJECT  : PYTHON FUNDAMENTAL (CREATE, READ, UPDATE, DELETE)
# STUDY CASE        : FREE PUBLIC LIBRARY

############################################# DEFINE TABLE STRUCTURES & DATASET #############################################

# Table Books: Master Data, to save books that are available in the library 

Books = {
    'ISBN'          : ['978-0375704024','978-1529926941','978-1911215370','978-0451087546','978-0385182447',
                      '978-0439023528','978-0439023498','978-0439023511','978-1338635171','978-1546171461',
                      '978-1594746031','978-1594746123','978-1594747588','978-0735232143','978-0735231504','978-0241320952'],
    'BookName'      : ['Norwegian Wood','The City and Its Uncertain Walls','Men Without Women','The Long Walk','Pet Sematary',
                      'The Hunger Games','Catching Fire','Mockingjay','The Ballad of Songbirds and Snakes','Sunrise on the Reaping',
                      'Miss Peregrine Home For Peculiar Children','Hollow City','Library of Souls','A Map of Days','The Conference of The Birds','The Desolations of Devil Acre'],
    'AuthorFirst'   : ['Haruki','Haruki','Haruki','Stephen','Stephen','Suzanne',
                        'Suzanne','Suzanne','Suzanne','Suzanne','Ransom',
                        'Ransom','Ransom','Ransom','Ransom','Ransom'],
    'AuthorLast'    : ['Murakami','Murakami','Murakami','King','King',
                        'Collins','Collins','Collins','Collins','Collins',
                        'Riggs','Riggs','Riggs','Riggs','Riggs','Riggs'],
    'PublishedYear' : [2000,2024,2018,1979,1983,
                       2008,2009,2010,2020,2025,
                       2011,2014,2015,2018,2020,2021],
    'StockQty'      : [9,10,6,10,7,
                       10,10,9,10,9,
                       10,7,10,8,8,1]
}

# ISBN              PRIMARY KEY: International Standard Book Numbers (14 char length)
# BookName          Book Title
# AuthorFirst       Author's First Name
# AuthorLast        Author's Last Name
# PublishedYear     Published Year
# StockQty          Book stocks left to rent

# Table Member: Master Data, to save member of the library; 
# Premium Member Feature (max. 5 books can be rented), Non Premium (max. 3 books)
Members = {
    'MemberID'      : ['MMB-P001','MMB-R002','MMB-R003','MMB-P004','MMB-R005',
                        'MMB-P006','MMB-P007','MMB-R008'],
    'Phone'         : ['6281892374012','6281892354012','62818943474012','628182374012','628189434237401',
                       '628189234274012','62818934237401','628189234012'],
    'MemberFirst'   : ['Mariah','John','Charlie','Brandon','Alicia',
                       'Thomas','Salmah','Little'],
    'MemberLast'    : ['Streep','Mellon','Clarkson','Pitt','Gaga',
                       'Cruise','Burdock','Jackboy'],
    'MemberSince'   : ['2023-12-03','2022-02-01','2023-09-09','2023-12-22','2020-11-30',
                       '2026-02-14','2022-01-13','2022-04-10'],
    'RentedBooks'   : [0,0,0,0,2,
                       4,2,3]
}

# MemberID          PRIMARY KEY: Member ID (Number Auto Generated)
#                   R >> Regular Member (max. 3 books)  |   P >> Premium Member (max. 5 books)
# Phone             PRIMARY KEY: Member's Phone Number (Unique)
# MemberFirst       Member's First Name
# MemberLast        Member's Last Name
# MemberSince       Member's first registration date
# RentedBooks       Books that is being rented by the member

# Table Transaction Rental: Transaction data, to save rental transaction of the members
TrxRental = {
    'TrxID'         : ['RENT-001','RENT-002','RENT-003','RENT-004','RENT-006',
                       'RENT-007','RENT-009','RENT-010','RENT-011','RENT-012',
                       'RENT-013','RENT-014','RENT-015','RENT-016','RENT-017','RENT-018'],
    'MemberID'      : ['MMB-R008','MMB-R003','MMB-R008','MMB-P007','MMB-P007',
                       'MMB-R003','MMB-R008','MMB-R005','MMB-R005','MMB-R008',
                       'MMB-P007','MMB-P006','MMB-R008','MMB-P006','MMB-P006','MMB-P006'],
    'ISBN'          : ['978-0385182447','978-0385182447','978-1911215370','978-1911215370','978-0375704024',
                       '978-1911215370','978-0735231504','978-1911215370','978-0735231504','978-0735232143',
                       '978-1594746123','978-0385182447','978-0735232143','978-1594746123','978-0439023511','978-1546171461'],
    'RentalStart'   : ['2023-04-10','2023-10-11','2024-07-10','2024-09-13','2025-01-13',
                       '2025-10-11','2026-02-12','2026-02-15','2026-03-12','2026-03-12',
                       '2026-03-12','2026-04-11','2026-04-12','2026-04-18','2026-05-10','2026-06-01'],
    'RentalEnd'     : ['2023-06-06','2024-01-10','2024-08-10','2024-11-30','2025-06-08',
                       '2025-12-11','2026-04-12',"","","",
                       "","","","","","","",""]           
}

# TrxID             PRIMARY KEY: Rental Transaction ID (Number Auto Generated)
# MemberID          Member ID
# ISBN              International Standard Book Numbers (14 char length)
# RentalStart       Rent Starting Date
# RentalEnd         Rent Ending Date

# Table Canceled Transaction ID
CanceledTrx = {
    'TrxID' : ['RENT-005','RENT-008','RENT-019'],
    'CancelDate' : ['2024-12-11','2025-10-11','2026-06-01'],
    'Reason' : ['Staff input member incorrectly','Staff double input','Staff double input']
}

# Save User's input choice for Yes/No Question
setYes = {True, "1", "Yes", "yes", "Ya", "ya", ""} #To save user's input possibilities
setNo = {False, "0", "No", "no", "Tidak", "tidak"} #To save user's input possibilities

# To Save Today's date
TodayDate = "2026-08-20"

# To Save Head Librarian Account and Password
AdminUser = { 'Head' : '123' }

############################################# DEFINE RECURRING FUNCTIONS #############################################

def CheckISBNFormat (ISBN):     # Function to pre-check format of 14-digit ISBN; Use when add new books and inside CallBooks Function
    """ Function to pre-check standard format of 14-digit ISBN; Use when add new books and inside CallBooks Function """
    result = False

    #Check ISBN length is 14 character (separated by dash at 4th character)
    if len(ISBN) == 14 and ISBN[3] == "-":

        #Check ISBN all characters (except 4th) is numeric
        if ISBN[0:3].isnumeric() == False or ISBN[4:14].isnumeric() == False:
            print ("Incorrect format of ISBN.")
            result = False
        else:
            result = True       #Return True; to continue the next process

    else:           #One or both condition aren't fulfilled 
        print ("Incorrect format of ISBN. ISBN should be in 14-digit format.")
        result = False

    return result

def CallBooks (ISBN,Operator):  # Function to call Book Titles; If ISBN is not in corrected format, this function won't run
    """ Function to call Book Titles from "Corrected-Format" ISBN; 
        If ISBN is not in corrected format, this function won't run  
        Operator: 1 for Add new books, 0 for check existence"""
    IdxBooks = None

    if CheckISBNFormat (ISBN) == True:
        #After check the format of ISBN, find index of the ISBN    
        if (ISBN not in Books['ISBN']) and (int(Operator) != 1) :
            print (f"The book you are searching for doesn't exist")
            IdxBooks = None

        elif ISBN in Books['ISBN'] or (int(Operator) != 1):
            #If ISBN exist, call the index location in Books Dictionary
            IdxBooks = Books['ISBN'].index(ISBN)
            if int(Operator) == 1:          #For (1) Add new book (with ISBN existed)
                print("Book already exist.")

            #Book Title
            print (f"\nBook Title: {Books['BookName'][IdxBooks]}")   

    return IdxBooks

def CheckMember(MemberID):      # Check existing member with pre-checked member format
    """ Function to check existing member, 
        with pre-checked format (only begin with specific character and the length); 
        Member status won't be checked from the input, as it may be changed """

    #Check inputed format
    if len(MemberID) != 8 or MemberID[0:4] != 'MMB-':
        print ("Wrong Member ID format.")
    else:
        #Format is correct, search existing member 
        if "MMB-R" + MemberID[-3:] in Members['MemberID']: 
            MemberID = "MMB-R" + MemberID[-3:]
            IdxMember = Members['MemberID'].index(MemberID)
            print (f"\nMember's Name: {Members['MemberFirst'][IdxMember]}  {Members['MemberLast'][IdxMember]}")

        elif "MMB-P" + MemberID[-3:] in Members['MemberID']:
            MemberID = "MMB-P" + MemberID[-3:]
            IdxMember = Members['MemberID'].index(MemberID)
            print (f"\nMember's Name: {Members['MemberFirst'][IdxMember]}  {Members['MemberLast'][IdxMember]}")     
        
        else:
            MemberID = None
            IdxMember = None
            print ("Member is not found")

        return MemberID, IdxMember   

def GenerateNum (CurrentNum):   # Function to generate Member & Transaction running numbers
    """ Function to generate Member & Transaction running numbers """
    Num = int(CurrentNum)
    Num +=1

    if Num < 10:
        RunNum = "00" + str(Num)
    elif Num < 100:
        RunNum = "0" + str(Num)
    elif Num >= 100:
        RunNum = str(Num)

    return RunNum

def CheckDate (InputDate):      # Function to check inputted Date Format (Member & Transaction); Will return as "YYYY-MM-DD"
    """ Function to check Date Format (Member & Transaction), Year limited to 2026 only;
        InputDate: YYYYMMDD
        Wrong input format will return as None. Corrected format will return as "YYYY-MM-DD" """
    DictDay = {
                'Month' :   ["01","02","03","04","05","06","07","08","09","10","11","12"],
                'Day'   :   ["31","28","31","30","31","30","31","31","30","31","30","31"]
              }
    ReturnedDate = None

    #Check Date format in 8 digits
    if len(InputDate) != 8:
        print ("Date should be input in 6 digit with the format YYYYMMDD.")
    else:

        #Check Year
        if int(InputDate[0:4]) != int(TodayDate[0:4]):              
            print ("Wrong year. This year is 2026.")

        #Check Non Leaped Year; Month and Date    
        elif int(InputDate[0:4]) % 4 != 0:
            if InputDate[4:6] not in DictDay['Month']:
                print ("Wrong month format.")
            else:
                #Call index location of the month
                Idx = DictDay['Month'].index(InputDate[4:6])

                if int(InputDate[-2:]) !=0 and int(InputDate[-2:]) <= int(DictDay['Day'][Idx]):
                    ReturnedDate = InputDate[0:4] + "-" + InputDate[4:6] + "-" + InputDate[-2:]
                else:
                    print ("Wrong inputted date.")   

        #Check Leaped Year
        elif int(InputDate[0:4]) % 4 == 0 :
            if int(InputDate[4:6]) == 2 and int(InputDate[-2:]) > 29:
                print ("Wrong inputted date.")
            else:
                ReturnedDate = InputDate[0:4] + "-" + InputDate[4:6] + "-" + InputDate[-2:]

    return ReturnedDate
  
def HeadTransaction (method):   # Function to display header of Transaction Dictionary
    """ Function to display header of Transaction Dictionary;
        method: "Normal" for Rental & Return Transactions; "Administrator" for Joined Rental, Return, and Canceled Transactions """
    if method == "Normal":
        print (f"\n{"Transc ID" :<11} | {"Member ID":<10} | {"ISBN":<15} | {"Rental Start":<8}  | {"Rental End":<13} \n{"="*75} ")
    elif method == "Administrator":
        print (f"\n{"Transc ID" :<11} | {"Member ID":<10} | {"ISBN":<15} | {"Rental Start":<8}  | {"Rental End":<13} | {"Remarks":<30} \n{"="*110} ")

def OutstandingTransaction (MemberId, method):      # Display Outstanding Transaction Dictionary, with or without Filter: MemberID
    """ Function to display Outstanding Transaction Dictionary;
        by Default: return all outstanding, With parameter: filtered by Member;
        Member ID + "Print" >> Return Transaction ID;
        Member ID + "List" >> Return ISBN from the books that haven't returned 
        method: "Print" for display records; "List" for filtered ISBN list without showing; Both methods only with specific MemberID """

    Outstanding = []        # Return book purpose

    #Use parameter, whether display all transactions, or filtered by member
    for idx in range ( len( TrxRental['TrxID'] ) ):
        if TrxRental['RentalEnd'][idx] != "":
            #Skip rental transactions that has been completed (books returned)
            pass
        else:
            #None parameter, print all outstanding transactions
            if method == "Print" and MemberId == None :
                print (f" { TrxRental['TrxID'][idx]:<10} | { TrxRental['MemberID'][idx]:<10} | { TrxRental['ISBN'][idx]:<15} | { TrxRental['RentalStart'][idx]:<13} | {"  -----  "} ")
                idx+=1

            #Index parameter exist, print all outstanding transactions from related Index
            elif method == "Print" and MemberId is not None:
                if TrxRental['MemberID'][idx] == MemberId:    #Looping index equal to Member ID in Dict (From input/other Function)
                    print (f" { TrxRental['TrxID'][idx]:<10} | { TrxRental['MemberID'][idx]:<10} | { TrxRental['ISBN'][idx]:<15} | { TrxRental['RentalStart'][idx]:<13} | {"  -----  "} ")
                    Outstanding.append( TrxRental['TrxID'][idx] )
                    idx+=1

            #Return list of books that haven't returned by Customer; use when Customer want to rent a book (One Customer = One Book per title)
            elif method == "List":
                if TrxRental['MemberID'][idx] == MemberId:    #Looping index equal to Member ID in Dict (From input/other Function)                          
                    Outstanding.append( TrxRental['ISBN'][idx] )
                    idx+=1

    if MemberId is not None:
        return Outstanding

def CreateNewRecords (DictName, field1="", field2="", field3="", field4="", field5="", field6="" ):     # Create new records for all Dict
    """ Save data into Dictionary/table """

    # ISBN | BookName | AuthorFirst | AuthorLast | PublishedYear | StockQty
    if DictName == "Books":
        Books['ISBN'].append(field1)              
        Books['BookName'].append(field2)          
        Books['AuthorFirst'].append(field3)       
        Books['AuthorLast'].append(field4)        
        Books['PublishedYear'].append(field5)     
        Books['StockQty'].append(field6)
        print ("\nBook has been recorded successfully.")
    
    # MemberID | Phone | MemberFirst | MemberLast | MemberSince | RentedBooks    
    elif DictName == "Members":
        Members['MemberID'].append(field1)       
        Members['Phone'].append(field2)                  
        Members['MemberFirst'].append(field3)          
        Members['MemberLast'].append(field4)    
        Members['MemberSince'].append(field5)        
        Members['RentedBooks'].append(0)
        print ("\nNew member has been recorded successfully.")

    # TrxID | MemberID | ISBN | RentalStart | RentalEnd
    elif DictName == "TrxRental":
        TrxRental['TrxID'].append(field1)
        TrxRental['MemberID'].append(field2)
        TrxRental['ISBN'].append(field3)
        TrxRental['RentalStart'].append(field4)
        TrxRental['RentalEnd'].append("")

    # TrxID | CanceledDate | Reason
    elif DictName == "Canceled":
        CanceledTrx['TrxID'].append(field1)
        CanceledTrx['CancelDate'].append(field2)
        CanceledTrx['Reason'].append(field3)

def ReadRecords (DictName):     # Function to display all Books Collection & all Members
    """ Function to display all records from Books or Members Dict  """ 

    if DictName == "Books":
        # Print header of the table
        print (f"\n{"ISBN" :<15} | {"Book Name":<50} | {"Author":<20} | {"Year":<7}  | {"Stock":<8} \n{"="*115} ")

        # Print the data of the table (from Books Dictionary, call with the key and index of the value) 
        for idx in range ( len( Books['ISBN'] ) ):
            AuthorName = Books['AuthorFirst'][idx] + " " + Books['AuthorLast'][idx]
            print (f" { Books['ISBN'][idx]:<15} | { Books['BookName'][idx]:<50} | { AuthorName:<20} | { Books['PublishedYear'][idx]:<8} | { Books['StockQty'][idx]:<8} ")
            idx+=1

    elif DictName == "Members":
        # Print header of the table
        print (f"\n{"Member ID" :<11} | {"Member Name":<20} | {"Phone Number":<17} | {"Member Since":<8}  | {"Rented Books":<8}  | {"Premium Member":<5} \n{"="*110} ")
    
        # Print the data of the table (from Members Dictionary, call with the key and index of the value) 
        for idx in range ( len( Members['MemberID'] ) ):
            MemberName = Members['MemberFirst'][idx] + " " + Members['MemberLast'][idx]
    
            MemberSince = Members['MemberSince'][idx][:7]   #Only Display Year and Month
    
            #Change into string, member category is Premium / Not
            if Members['MemberID'][idx][4:5] == "P":
                    MemberPremium = "Yes"
            else:
                    MemberPremium = "No"
    
            print (f" { Members['MemberID'][idx]:<10} | { MemberName:<20} | { Members['Phone'][idx]:<17} | { MemberSince:<13} | { Members['RentedBooks'][idx]:<13} | {MemberPremium} ")
            idx+=1

def UpdateRecords (DictName, Fieldname, Index, Value):  #Function to update records, with assign DictName, Field, Index Loc, and Value
    """ Function to update records, with assign DictName, Field, Index Loc, and Value """
    DictName[Fieldname][Index] = Value

def UpdateBookStocks (ISBN, MemberId, Operator):    # Update book stocks (Rent or Return (incl. Cancel) ), based from ISBN
    """ Update book stocks, based from ISBN;
        Operator: Borrow, Return """

    #Call Index Books by ISBN, update Book Stock
    IdxBooks = Books['ISBN'].index(ISBN)

    #Call Index Member by Member ID, update rented books
    IdxMember = Members['MemberID'].index(MemberId)

    if Operator == "Borrow":
        Books['StockQty'][IdxBooks] = Books['StockQty'][IdxBooks] - 1                   #Minus books
        Members['RentedBooks'][IdxMember] = Members['RentedBooks'][IdxMember] + 1       #Add Rented books

    elif Operator == "Return":
        Books['StockQty'][IdxBooks] = Books['StockQty'][IdxBooks] + 1                   #Add books 
        Members['RentedBooks'][IdxMember] = Members['RentedBooks'][IdxMember] - 1       #Minus Rented books

def DeleteRecords (DictName, delISBN="", delMemberID="", delIdx=""):     #Function to delete books, member (no transaction) & records from Transaction table (canceled)
    if DictName == "Books":
        #Check ISBN Format, Call Book's Name & Index based on ISBN
        IdxBooks = CallBooks (delISBN, 0)
        
        if IdxBooks is not None:
            if ISBN in TrxRental['ISBN']:
                print ("This book can't be removed")
            else:
                confirm = str( input("Are you sure want to remove this book? (1) Yes | (0) No \t") )
                if confirm in setYes:
                    del Books['ISBN'][IdxBooks]              
                    del Books['BookName'][IdxBooks]          
                    del Books['AuthorFirst'][IdxBooks]       
                    del Books['AuthorLast'][IdxBooks]        
                    del Books['PublishedYear'][IdxBooks]     
                    del Books['StockQty'][IdxBooks]
                    print ("\nBook has been removed successfully.")

    elif DictName == "Members":
        #Check inputed format, and member's existence
        MemberID, IdxMember = CheckMember(delMemberID)

        if MemberID is not None and IdxMember is not None:
            if MemberID in TrxRental['MemberID']:
                print ("This member can't be removed")
            else:
                confirm = str( input("Are you sure want to remove this member? (1) Yes | (0) No \t") )
                if confirm in setYes:
                    del Members['MemberID'][IdxMember]       
                    del Members['Phone'][IdxMember]                  
                    del Members['MemberFirst'][IdxMember]         
                    del Members['MemberLast'][IdxMember]    
                    del Members['MemberSince'][IdxMember]       
                    del Members['RentedBooks'][IdxMember]
                    print ("\nMember has been removed successfully.")

    elif DictName == "TrxRental":
        del TrxRental['TrxID'][delIdx]
        del TrxRental['MemberID'][delIdx]
        del TrxRental['ISBN'][delIdx]
        del TrxRental['RentalStart'][delIdx]
        del TrxRental['RentalEnd'][delIdx]

def Authorization():            #Check Head Librarian Authorization
    """ Check Head Librarian Authorization """

    #Confirm authorization by request username and password
    username = input ("\nPlease input your username: \t")
    password = input ("Please input your password: \t")
    Authorized = False

    if username not in AdminUser.keys() :         #Reject process from unauthorized user
        print ("\nSorry. You have no authorization.")        
    elif AdminUser[username] == password: 
        print ("\n***** Welcome Head Librarian *****")
        Authorized = True
    else:                                         #Correct username; Wrong password
        print ("\nPlease check again.")

    return Authorized

#################################################### PROGRAM MENU #################################################### 

while True:
    #Keep showing menu program, as long User do not choose Exit
    print ( "\n\t\t*******WELCOME TO FREE PUBLIC LIBRARY*******"
            "\n\t1. Display, Add and Edit Books Collection"
            "\n\t2. Display, Add and Edit Members"
            "\n\t3. Display All Rental Transactions"
            "\n\t4. Rent and Return a Book"
            "\n\t8. Display all Historical Transaction" #(Only reserved for head librarian)
            "\n\t9. Remove Rental Transaction" #(Only reserved for head librarian)
            "\n\t0. Exit Program"
    )

    try:
        choice = int ( input ("\nHow can I help you today?\t") )

        # ***** 1. Display, Add and Edit Books Collection *****
        if choice == 1:
            try:
                ReadRecords ("Books")

                #Show menu option, to add new member, edit existing member, or back to main menu
                while True :                
                    AddEdit = int ( input ("\nPlease choose your option: (1) Add new books | (2) Edit existing books | (3) Display books | (9) Delete books collection | (0) Back to main menu \t") )

                    if AddEdit == 1:        #Add Books Process
                             
                        ISBN = str ( input ("\nPlease input ISBN number: \t") ).strip()
                        #Check ISBN Format, and Books should not existed
                        if (CheckISBNFormat (ISBN) == True) and (CallBooks (ISBN, 1) == None):

                            #After check the format of ISBN, continue with add process
                            BookTitle = str( input ("\nPlease input the book's title: \t") ).strip().title()
                            AuthorFirst = str( input ("Please input the author's first name: \t") ).strip().title()
                            AuthorLast = str( input ("Please input the author's last name: \t") ).strip().title()     
                            
                            while True:
                                try:
                                    #Pre confirm each input: Published year do not exceed today (2026)
                                    PblshYear = int( input ("Please input the published year: \t") )

                                    if PblshYear > int(TodayDate[0:4]) :
                                        print ("Published year can't exceed today's date.")
                                    elif PblshYear <= 1950 :     # Reconfirm again
                                        confirm = str( input("Are you sure the published year is {PblshYear}? (1) Yes | (0) No \t") )
                                        if confirm in setYes:
                                            break
                                    else:
                                        break

                                except ValueError:
                                    #Error Input type
                                    print ("\nInvalid input.")
                                
                            while True:
                                try:
                                    #Pre confirm each input: Stock Qty exceed 15
                                    #Usually, a library won't have a large amount of qty for each book's title
                                    Stock = int( input ("Please input the stock: \t") )

                                    if Stock <= 0 :
                                        print ("Book stock can't be zero or below.")
                                    elif Stock >15 :     # Reconfirm again
                                        confirm = str( input("Are you sure the book stock is {Stock}? (1) Yes | (0) No \t") )
                                        if confirm in setYes:
                                            break
                                    else:
                                        break        
                                                                    
                                except ValueError:
                                    #Error Input type
                                    print ("\nInvalid input.")

                            #Add the new book process
                            CreateNewRecords ("Books", ISBN, BookTitle, AuthorFirst, AuthorLast, PblshYear, Stock)

                    elif AddEdit == 2:      #Edit existing books, call based on ISBN 

                        ISBN = str ( input ("\nPlease input ISBN number: \t") ).strip()                        
                        #Check ISBN Format, Call Book's Name & Index based on ISBN
                        IdxBooks = CallBooks (ISBN, 0)
                        
                        if IdxBooks is not None:    #Books is found
                            #Call every details in order, confirm with user if there's need editing
                            
                            #Book's Title has been called in the function
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                BookTitle = str( input ("\nPlease input the correct book's title: \t") ).strip().title()
                                UpdateRecords (Books, 'BookName', IdxBooks, BookTitle)

                            #Author Full Name
                            print (f"\nAuthor's Name: {Books['AuthorFirst'][IdxBooks]}  {Books['AuthorLast'][IdxBooks]}")
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                AuthorFirst = str( input ("\nPlease input the author's first name: \t") ).strip().title()
                                AuthorLast = str( input ("\nPlease input the author's last name: \t") ).strip().title()   
                                UpdateRecords (Books, 'AuthorFirst', IdxBooks, AuthorFirst)
                                UpdateRecords (Books, 'AuthorLast', IdxBooks, AuthorLast)

                            #Published Year
                            print (f"\nPublished Year: {Books['PublishedYear'][IdxBooks]}")
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                while True:                                    
                                    try:
                                        #Pre confirm each input: Published year do not exceed today (2026)
                                        PblshYear = int( input ("\nPlease input the published year: \t") )

                                        if PblshYear > int(TodayDate[0:4]) :
                                            print ("\nPublished year can't exceed today's date.")
                                        elif PblshYear <= 1950 :     # Reconfirm again
                                            confirm = str( input("\nAre you sure the published year is {PblshYear}? (1) Yes | (0) No \t") )
                                            if confirm in setYes:
                                                UpdateRecords (Books, 'PublishedYear', IdxBooks, PblshYear)
                                                break
                                        else:
                                            UpdateRecords (Books, 'PublishedYear', IdxBooks, PblshYear)
                                            break

                                    except ValueError:
                                        #Error Input type
                                        print ("\nInvalid input.")
                                
                            #Stock Qty
                            print (f"\nStocks: {Books['StockQty'][IdxBooks]}")
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                while True:
                                    try:
                                        #Pre confirm each input: Stock Qty exceed 15
                                        Stock = int( input ("\nPlease input the stock: \t") )

                                        if Stock <= 0 :
                                            print ("\nBook stock can't be zero or below.")
                                        elif Stock >15 :     # Reconfirm again
                                            confirm = str( input(f"\nAre you sure the book stock is {Stock}? (1) Yes | (0) No \t") )
                                            if confirm in setYes:
                                                UpdateRecords (Books, 'StockQty', IdxBooks, Stock)                                                                                        
                                                break
                                        else:
                                            UpdateRecords (Books, 'StockQty', IdxBooks, Stock)
                                            break     
                                        
                                    except ValueError:
                                        #Error Input type
                                        print ("\nInvalid input.")                        

                            print ("\nBook has been edited successfully.")

                            #Finish editing, back to main menu                            
                            break

                    elif AddEdit == 3:      #Display books collection again
                        ReadRecords ("Books")

                    elif AddEdit == 9:      #Delete books collection; limited to haven't been rented
                        ISBN = str ( input ("\nPlease input ISBN number: \t") ).strip()                                                
                        DeleteRecords("Books", delISBN=ISBN)

                    elif AddEdit == 0:      #Back to main menu, break from loop
                        break
                    else:                   #Not valid option
                        print ("\nThe option you entered is not valid.")                        
            except:                         # Mitigate error input
                    print ("\nThe input you entered is not valid.")
                
        # ***** 2. Display, Add and Edit Members *****
        elif choice == 2:          
            try:
                ReadRecords ("Members")            
                #Show menu option, to add new member, edit existing member, or back to main menu
                while True :
                
                    AddEdit = int ( input ("\nPlease choose your option: (1) Add new member | (2) Edit existing member | (3) Display members list | (9) Delete member | (0) Back to main menu \t") )

                    if AddEdit == 1:        #Add new member process
                        #Member ID Auto Generated from the last record
                        
                        #Call last item of the Dictionary; call Function to Extract 3 last digit and add +1
                        MemberID = "MMB-R" + GenerateNum (Members['MemberID'][-1][-3:])                        

                        while True:
                            #Pre confirm each input: Member Phone (11-16 digits, do not start with 0)
                            MemberPhone = str( input ("\nPlease input member's phone number: \t") ).strip()

                            if MemberPhone.isnumeric()==False:
                                print ("Please input number only.")

                            else:
                                if MemberPhone[0] != "0":
                                    if len(MemberPhone) not in range (11, 17):
                                        print ("Phone number should be in 11 - 16 digits.")
                                    else:
                                        #Check duplicate member: from Member Phone
                                        if MemberPhone not in Members['Phone']:
                                            break
                                        else:
                                            print ("Member has already existed.")
                                else:
                                    print ("Phone number can't be started with (0) zero.")

                        while True:
                            MemberFirst = str( input ("\nPlease input member's first name: \t") ).strip().title()
                            MemberLast = str( input ("Please input member's last name: \t") ).strip().title()

                            #If Member's First Name is not empty
                            if len(MemberFirst)>3:
                                break
                        
                        while True:
                            RawDate = str( input ("\nPlease input member's joining date (YYYYMMDD): \t") ).strip()
                            MemberDate = CheckDate (RawDate)

                            #If Member Date is already in correct format, break
                            if MemberDate is not None:
                                break
                            
                        confirm = str( input("\nIs the new member is a premium member? (1) Yes, Premium Member | (0) No, Regular Member \t") )
                        if confirm in setYes:
                            #If Premium Member, change the member ID structure & reassign back
                            ChgdMemberId = MemberID[:4] + "P" + MemberID[5:]        # Change member ID Structure by Slicing and Joining characters
                            MemberId = ChgdMemberId                            
                        
                        #Add the new member process
                        CreateNewRecords ("Members", MemberId, MemberPhone, MemberFirst, MemberLast, MemberDate, 0)
                                               
                    elif AddEdit == 2:      #Edit existing member process
                        
                        #Call based on member ID
                        MemberID = str( input ("\nPlease input member's ID: \t") ).strip().upper()

                        #Check inputed format, and member's existence
                        MemberID, IdxMember = CheckMember(MemberID)

                        if MemberID is not None and IdxMember is not None:                                
                            #Member's full name has been called in the function
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            
                            #Call every details in order, confirm with user if there's need editing                            
                            if confirm in setNo:
                                MemberFirst = str( input ("\nPlease input the member's first name: \t") ).strip().title()
                                MemberLast = str( input ("Please input the member's last name: \t") ).strip().title()   
                            else:
                                #No editing, assign variable as Old values
                                MemberFirst = Members['MemberFirst'][IdxMember]
                                MemberLast = Members['MemberLast'][IdxMember]
                            
                            #Member's Phone Number
                            #Scenario: One might try to registered as different name to get new member ID, but edit later with the same data               
                            print (f"\nMember's Phone: {Members['Phone'][IdxMember]} ")
                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                #Member's Phone
                                while True:
                                    #Pre confirm each input: Member Phone (11-16 digits, do not start with 0)
                                    MemberPhone = str( input ("Please input member's phone number: \t") ).strip()

                                    if MemberPhone.isnumeric()==False:
                                        print ("Please input number only.")
        
                                    else:                                    
                                        if MemberPhone[0] != "0":
                                            if len(MemberPhone) not in range (11, 17):
                                                print ("Phone number should be in 11 - 16 digits.")
                                            else:
                                                #Check duplicate member: from Member Phone
                                                if MemberPhone not in Members['Phone']:
                                                    break
                                                else:
                                                    print ("Member has already existed.")
                                        else:
                                            print ("Phone number can't be started with (0) zero.")
                                            
                            else:
                                #No editing, assign variable as Old values
                                MemberPhone = Members['Phone'][IdxMember]

                            UpdateRecords (Members, 'MemberFirst', IdxMember, MemberFirst)
                            UpdateRecords (Members, 'MemberLast', IdxMember, MemberLast)
                            UpdateRecords (Members, 'Phone', IdxMember, MemberPhone)
                                
                            #Member Premium Status
                            if MemberID[4] == "P":
                                print ("\nCurrent Member Status: Premium") 
                            elif MemberID[4] == "R":
                                print ("\nCurrent Member Status: Regular")

                            confirm = str( input("Looks good? (1) Yes | (0) No, need to edit \t") )
                            if confirm in setNo:
                                #If there's change FROM premium TO regular, check total rented books
                                if MemberID[4] == "P":  
                                    if int(Members['RentedBooks'][IdxMember]) >3 :
                                        print ("Current Member Status can't be changed. Please return books first.")
                                    else:
                                        ChgdMemberId = MemberID[:4] + "R" + MemberID[5:]        
                                        UpdateRecords (Members, 'MemberID', IdxMember, ChgdMemberId)

                                        #Table Transaction; UPDATE Outstanding Rental only
                                        for idx in range ( len( TrxRental['TrxID'] ) ):
                                            if TrxRental['MemberID'][idx] == MemberID:
                                                UpdateRecords (TrxRental, 'MemberID', idx, ChgdMemberId)

                                #From Regular to Premium
                                else:        
                                    ChgdMemberId = MemberID[:4] + "P" + MemberID[5:]                     
                                    UpdateRecords (Members, 'MemberID', IdxMember, ChgdMemberId)

                                    #Table Transaction; UPDATE Outstanding Rental only
                                    for idx in range ( len( TrxRental['TrxID'] ) ):
                                        if TrxRental['MemberID'][idx] == MemberID:
                                            UpdateRecords (TrxRental, 'MemberID', idx, ChgdMemberId)

                            #Rented Books can't be edited
                            print ("\nMember's data has been edited successfully.")
                        
                        #Finish editing, back to main menu                            
                        break
                    
                    elif AddEdit == 3:      #Display members again
                        ReadRecords ("Members")

                    elif AddEdit == 9:      #Delete member; limited to no-transaction member
                        MemberID = str( input ("\nPlease input member's ID: \t") ).strip().upper()
                        DeleteRecords("Members", delMemberID=MemberID)

                    elif AddEdit == 0:      #Back to main menu, break from loop
                        break
                    else:                   #Not valid option
                        print ("\nThe option you entered is not valid.")
            except:                         # Mitigate error input
                pass        

        # ***** 3. Display All Rental Transactions *****
        elif choice == 3:           
            #BY DEFAULT: Display  OUTSTANDING  rental books
            print ("\n Here's our outstanding rental books that haven't returned by members. ")
            HeadTransaction ("Normal")          # Print header of the table
            OutstandingTransaction (None, "Print")   # Print outstanding rental records
        
            try:
                ShowAll = str (input ("\nDo you need to show all rental transactions? (1) Yes | (0) No \t") )

                if ShowAll in setYes:
                    print ("\n Here's all rental books history transactions. ")                
                    HeadTransaction ("Normal")          # Print header of the table

                    #Display all records
                    for idx in range ( len( TrxRental['TrxID'] ) ):
                        
                        if TrxRental['RentalEnd'][idx] != "":
                            RentalEnd = TrxRental['RentalEnd'][idx]
                        else:
                            RentalEnd = "  -----  "         #Books that haven't returned, will shown as -----

                        print (f" { TrxRental['TrxID'][idx]:<10} | { TrxRental['MemberID'][idx]:<10} | { TrxRental['ISBN'][idx]:<15} | { TrxRental['RentalStart'][idx]:<13} | { RentalEnd } ")
                        idx+=1
            except:                         # Mitigate error input
                pass
                           
        # ***** 4. Rent and Return a Book *****
        elif choice == 4:       
            try:
                #Show menu option, to rent a book, return a book, or back to main menu
                while True :                
                    
                    #Call based on member ID
                    MemberID = str( input ("\nPlease input member's ID: \t") ).strip().upper()
                    if MemberID == "0" or MemberID == "":           #Escape to main menu
                        break
                    else:
                        #Check member's existence, and call Member's name if exist
                        MemberID, IdxMember = CheckMember(MemberID)
                              
                    if MemberID is not None and IdxMember is not None:
                        RentReturn = str (input ("\n(1) Rent a Book | (2) Return a book | (0) Back to main menu \t") ).strip()                        
                        if RentReturn == "0":           #Back to main menu, break from loop
                            break

                        elif RentReturn == "1":         #Rent a Book Process

                            #Checking step process: Check member status AND rented books; whether eligible to rent another book or not                            
                            if (MemberID[4] == "R" and Members['RentedBooks'][IdxMember] == 3) or (MemberID[4] == "P" and Members['RentedBooks'][IdxMember] == 5):
                                print ("\nMaximum books has been reached. Please return books first.")
                            else:
                                Cart = []
                                RentedQty = 0

                                #To Check previous rental transaction (ISBN), whether user will rent the same book or not
                                ListTrx = OutstandingTransaction (MemberID, "List")

                                while True:                                    
                                    #Check ISBN format, call the book name for easily reading
                                    ISBN = str ( input ("\nPlease input ISBN number: \t") ).strip()
                                    if ISBN == "0" or ISBN == "":
                                        break           #Escape and go to final cart

                                    else:
                                        if CheckISBNFormat(ISBN) == False:
                                            IdxBooks = None
                                        else:
                                            IdxBooks = CallBooks (ISBN, 0)
                                            
                                            #If Books found in collection, Check duplicate in Previous Transaction, check Stock and Cart
                                            if ISBN in ListTrx:
                                                print ("You already have rented this book before.")
                                                IdxBooks = None
                                    
                                    if IdxBooks is not None :           
                                        #Check stock availability from collection
                                        StockStatus = Books['StockQty'][IdxBooks]
                                        if StockStatus == 0:
                                            print ("Sorry. Out of stock. You can't borrow this book.")

                                        if len(Cart) != 0:
                                            #Check items in the cart. One Checkout One ISBN; Stock in Cart not needed to be checked
                                            for idx in range ( len(Cart) ):
                                                if Cart[idx][1] == ISBN:
                                                    print ("You already have this book on your cart.")
                                                    IdxBooks = None
                                           
                                    #Stock available, books aren't duplicated in cart and previous rental transaction
                                    if IdxBooks is not None and StockStatus > 0:                                            

                                        confirm = str( input("Do you want to borrow this book?  (1) Yes | (0) No \t") )
                                        if confirm in setYes:                                    
                                            #Check again member status AND rented books (include carts); whether eligible to rent another book or not 
                                            if (MemberID[4] == "R" and ( Members['RentedBooks'][IdxMember] +RentedQty) == 3) or (MemberID[4] == "P" and ( Members['RentedBooks'][IdxMember] +RentedQty) == 5):
                                                print ("\nMaximum books has been reached. Please return books first.")
                                                break

                                            else:
                                                if len(Cart) != 0:
                                                    # Cart already exist, generate number based from Cart; 
                                                    CurrentNum = Cart[-1][0]                                                
                                                    TrxID = 'RENT-' + GenerateNum (CurrentNum[-3:])
                                                else:
                                                    #Cart is empty, generate number from Last Transaction

                                                    # Member eligible; Auto generate Transaction ID; 
                                                    CurrentNum = TrxRental['TrxID'][-1]                                                
                                                    TrxID = 'RENT-' + GenerateNum (CurrentNum[-3:])

                                                    # Compensate with canceled transaction ID
                                                    if TrxID == CanceledTrx['TrxID'][-1]:
                                                        TrxID = 'RENT-' + GenerateNum(TrxID[-3:]) 
                                                    
                                                Cart.append([TrxID,ISBN])
                                                RentedQty += 1
                                                    
                                    confirm = str( input("\nDo you want to borrow another book?  (1) Yes | (0) No \t") ).strip()
                                    if confirm in setNo:
                                        break

                                #Out of While Loop Cart
                                #Display cart information, and final confirmation                                
                                if len(Cart) == 0:              #Cart is empty
                                    print("\nHave a nice day.")     

                                elif len(Cart) != 0:
                                    print("\nHere's the books you will rent.")
                                    print (f"\n{"ISBN" :<15} | {"Book Name":<50} \n{"="*60} ")

                                    for idx in range( len(Cart) ):
                                        #Call Index Books by ISBN
                                        IdxBooks = Books['ISBN'].index(Cart[idx][1])
                                        print(f"{Cart[idx][1] :<15} | {Books['BookName'][IdxBooks] :<50} ")

                                    confirm = str( input("\nConfirm to borrow these books?  (1) Yes | (0) No \t") )
                                    if confirm in setYes:                                        
                                        # Update: Transaction, Members, Books Table
                                                                    
                                        #Cart Structure  [TrxRental ID, ISBN]
                                        for idx in range( len(Cart) ):

                                            #Call Index Books by ISBN, update Stocks in Books Dict and Member
                                            UpdateBookStocks (Cart[idx][1], MemberID, "Borrow")

                                            #Update Transaction Rental
                                            CreateNewRecords ("TrxRental", Cart[idx][0], MemberID, Cart[idx][1], TodayDate)
                                        
                                        print("\nThank you. Please come again.")
                                    else:
                                        print("\nHave a nice day.")  

                                #Clearing cart items
                                Cart.clear()    
                                RentedQty = 0
                                break               #Back to Main Menu
                        
                        elif RentReturn == "2":         #Return a Book Process
                            
                            #Display  OUTSTANDING  rental books
                            print ("\n Here's outstanding rental books that you haven't returned. ")                
                            HeadTransaction ("Normal")          # Print header of the table

                            # Print outstanding rental records, return transaction ID into the list
                            ListTrx = OutstandingTransaction (MemberID, "Print")

                            while True:                                
                                if len(ListTrx) == 0:
                                    print (f"\n {"-"*73} ")     #No Outstanding transaction, just print a line
                                    break

                                #If ListTrx is not empty, give option to input Transaction ID
                                elif len(ListTrx) > 0:
                                    ReturnTrx = str (input ("\nPlease input Transaction ID: | (0) Back to main menu \t") ).strip()
                                    if ReturnTrx == "0" :   #Escape and back to main
                                        break
                                    elif ReturnTrx not in ListTrx:
                                        print ("\nTransaction ID is not found.")

                                    elif ReturnTrx in ListTrx:
                                        ReturnIdx = TrxRental['TrxID'].index(ReturnTrx)     #Get index loc inside TrxRental Dict
                                        ReturnISBN = TrxRental['ISBN'][ReturnIdx]           #Get value of ISBN from Trx ID

                                        CallBooks (ReturnISBN,0)    #Call book title
                                        confirm = str( input("You will return this book?  (1) Yes | (0) No \t") )
                                        if confirm in setYes:

                                            # Return book process
                                            while True:
                                                #Check returned date                                            
                                                RawDate = str( input ("\nPlease input returned date (YYYYMMDD): \t") ).strip()
                                                ReturnDate = CheckDate (RawDate)

                                                RentDate = TrxRental['RentalStart'][ReturnIdx]
                                                # RentDate structure  YYYY-MM-DD

                                                # If Return Date is already in correct format, 
                                                # Check return date, must be the same or after rent date
                                                if ReturnDate is not None:
                                                    
                                                    if int(ReturnDate[0:4]) <= int(RentDate[0:4]):     #Check if less or same year
                                                        if int(ReturnDate[5:7]) == int(RentDate[5:7]):     #Check if same month, continue check date
                                                            if int(ReturnDate[-2:]) < int(RentDate[-2:]):     #Check Date
                                                                print("Return date can't be earlier than Rental date")
                                                            else:    
                                                                break
                                                        elif int(ReturnDate[5:7]) < int(RentDate[5:7]):    #If return month is earlier
                                                            print("Return date can't be earlier than Rental date")
                                                        else:
                                                            break
                                                    else:    
                                                        break

                                            #Update Book Stock from Books Dict and Member    
                                            UpdateBookStocks (ReturnISBN, MemberID, "Return")                                                                           
                                            
                                            # Transaction table updated;
                                            UpdateRecords (TrxRental, 'RentalEnd', ReturnIdx, ReturnDate) 

                                            print ("\nBook has been returned. Thank you")
                                            break

                                        else:       #Not return book
                                            break

                                    else:
                                        print ("\nThe option you entered is not valid.") 

                            # End of Book Return Process 
                            break

                        else:                       #Not valid option
                            print ("\nThe option you entered is not valid.")
            except:         # Mitigate error input
                pass      

        # ***** 8. History All Transactions included Canceled Transactions *****
        elif choice == 8:
        #Hidden menu, to display all canceled transactions (dedicated to head librarian)           
            if Authorization() == True:         #Check from Admin User Dict
                
                #Gather all transactions ID into one list(use duplicate), and sort 
                AllTrx = TrxRental['TrxID'].copy()
                AllTrx.extend(CanceledTrx['TrxID'].copy())
                AllTrx.sort()
                
                HeadTransaction ("Administrator")
                #Loop by the length of the AllTrx List, call correspond index
                for idxList in range ( len(AllTrx) ):
                    
                    if AllTrx[idxList] in TrxRental['TrxID']:           #If Trx ID is part of Transaction Dict
                        idx = TrxRental['TrxID'].index(AllTrx[idxList])

                        if TrxRental['RentalEnd'][idx] != "":
                            RentalEnd = TrxRental['RentalEnd'][idx]
                        else:
                            RentalEnd = "  -----  "         #Books that haven't returned, will shown as -----

                        print (f" { TrxRental['TrxID'][idx]:<10} | { TrxRental['MemberID'][idx]:<10} | { TrxRental['ISBN'][idx]:<15} | { TrxRental['RentalStart'][idx]:<13} | { RentalEnd :<13} | ")

                    elif AllTrx[idxList] in CanceledTrx['TrxID']:       #If Trx ID is part of Canceled Dict
                        idx = CanceledTrx['TrxID'].index(AllTrx[idxList])

                        print (f" { CanceledTrx['TrxID'][idx]:<10} | { "  -----":<10} | { "     -----":<15} | { " CANCELED ":<13} | { CanceledTrx['CancelDate'][idx]:<13} | { CanceledTrx['Reason'][idx]:<20} ")
        
        # ***** 9. Correction / Cancel Transaction *****
        elif choice == 9:
        #Hidden menu, to correct rental transaction (dedicated to head librarian)           
            if Authorization() == True:         #Check from Admin User Dict
                #ONLY to CORRECTING staff error while input
                #LIMITED to REVERSE books that haven't been returned
                HeadTransaction ("Normal")          # Print header of the table
                OutstandingTransaction (None, "Print")   # Print outstanding records (that can be edited/reversed)

                while True:
                    CancelTrx = str (input ("\nPlease input transaction ID that you want to cancel: \t") )
                    DelTrxId = 0       #Used for index of the Transaction ID that need to delete/cancel
                    
                    if CancelTrx == "0":           #Escape to main menu
                        break

                    #Check Trx Rental ID exist or not
                    elif CancelTrx not in TrxRental['TrxID']:
                        print ("\tTransaction Not Found")

                    else:                        
                        #Call index location, search by value
                        DelTrxId = TrxRental['TrxID'].index(CancelTrx)

                        #Pre check again correspond Trx ID; book hasn't been returned 
                        if TrxRental['RentalEnd'][DelTrxId] != "":
                            print (f"\tTransaction ID: {CancelTrx} can't be canceled.")

                        else:
                            ReconfirmDelete = input (f"Are you sure want to cancel Transaction ID: {CancelTrx}? (1) Yes | (0) No  \t")

                            if ReconfirmDelete in setYes:
                                ReasonDelete = str ( input ("Plase input the reason: \t") ).strip().capitalize()

                                # ADD the deleted transaction ID to CancelTrx
                                CreateNewRecords("Canceled", CancelTrx, TodayDate, ReasonDelete)

                                # UPDATE Book Stock from Books Dict and Member                                                                
                                MemberId = TrxRental['MemberID'][DelTrxId]
                                ISBN = TrxRental['ISBN'][DelTrxId]
                                UpdateBookStocks (ISBN, MemberId, "Return")
                                
                                # DELETE from Transaction Rental table
                                DeleteRecords ("TrxRental", delIdx=DelTrxId)
                                print (f"\nTransaction ID: {CancelTrx} has been canceled. Have a nice day.")
                            
                            else:
                                print ("\nProcess has been canceled.")

                            break       #Out of Cancel transaction loop            
                                                                            
        # ***** 0. Exit Program *****
        elif choice == 0:           
            print ("\nThank you. Have a nice day.\n")
            break

        # *****Choice is not found *****
        else:                       
            print ("\nThe option you entered is not valid.")    

    except:         # Mitigate error input
        pass
#------------------------------------------------------------ END ------------------------------------------------------------#