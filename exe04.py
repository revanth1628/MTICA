def printsun():
    print("sunday ")
def printmon():
    print(" monday")
def printtue():
    print("tuesday ")
def printwed():
    print("wednesday ")
def printthu():
    print("thursday ")
def printfri():
    print(" friday")
def printsat():
    print(" sarurday")
def choice():
    print("enter the day number between 1-7:")
DaySelect={1:printsun,2:printmon,3:printtue,4:printwed,5:printthu,6:printfri,7:printsat}
selection=0
while(True):
    if selection>7:print("INVALID")
    choice()
    selection=int(input('select the option:'))
    if(selection>=1) and (selection<8):
        DaySelect[selection]()
        
        
