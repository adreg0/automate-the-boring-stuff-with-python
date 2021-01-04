import pyinputplus as pyip

print("Bread:")
bread= pyip.inputMenu(["wheat","white","sourdough"])
if bread=="wheat":
    bread=10 
elif bread=="white":
    bread=15 
elif bread=="sourdough":
    bread=10 

print("Protein:")
protein=pyip.inputMenu(["chicken","turkey","ham","tofu"])
if protein=="chicken":
    protein=12
elif protein=="turkey":
    protein=14
elif protein=="ham":
    protein=16
elif protein=="tofu":
    protein=18

cheesereq= "Cheese needed ?"
response = pyip.inputYesNo(cheesereq)
if response == "yes":
    cheese=pyip.inputMenu(["cheddar","Swiss","mozzarella"])
    if cheese=="cheddar":
        cheese=5 
    elif cheese=="Swiss":
        cheese=7 
    elif cheese=="mozzarella":
        cheese=9 
else:
    cheese=0

addreq="mayo,mustard,letuce,tomato needed ?"
response1=pyip.inputYesNo(addreq)
if response1=="yes":
    addons=10
else:
    addons=0
    
units="No. of sandwiches needed= ?"
units=pyip.inputInt(units,min=1)
sandwich = bread+protein+cheese+addons
gross=units*sandwich
print("Total mount to be paid : ",gross)

