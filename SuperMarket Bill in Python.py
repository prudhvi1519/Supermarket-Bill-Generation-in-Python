#Supermaket Bill Generation using Python
from datetime import datetime
import time
import os

# Function to display a moving "Thank You" message
def marquee_thnq(text="Thank Uhhh!\tVisit Again...", width=76, delay=0.1):
    text = " "*width + text + " "*width  # Padding the text with spaces
    while True:
        print(text[:width], end="\r")  # Display the message with carriage return to simulate scrolling
        time.sleep(delay)  # Delay to control the speed of the message
        text = text[1:] + text[0]  # Shift the text for the scrolling effect

# Collecting the customer's name, ensuring it's valid (only alphabet characters)
while True:
    name=input("\nEnter your name: ").title()  #Customer name for billing
    if name.isalpha():
        break
    else:
        print("Please enter a VALID Name!")  # Error message for invalid name

#List of Items available
items_available='''
Rice       Rs 65/kg
Sugar      Rs 50/kg
Oil        Rs 120/lit
Salt       Rs 40/kg
Pepper     Rs 60/kg
Tumeric    Rs 65/kg
Paste      Rs 20/each
'''

#Definations
price=0
price_list=[]
total_price=0
ilist=[]
qlist=[]
plist=[]
final_amount=0

#Dictionary storing the price for each available item
items_prices={'Rice':65, 'Sugar':50, 'Oil':120, 'Salt':40, 'Pepper':60, 'Tumeric':65, 'Paste':20}

# Ask the user to press '1' to view the list of available items
option=int(input("For list of Items, Press 1: "))
if option==1:
    print(items_available)  # Display the list of available items
else:
    int(input("Wrong!\nFor list of Items, Press 1: "))  # If wrong input, ask again
    print(items_available)

# Loop to allow the customer to buy items until they decide to exit
for i in range(len(items_prices)):
    ipt1=input("\nPress 1 for BUY,  2 for EXIT: ")  # Ask if the user wants to buy or exit
    if ipt1=='2':  # Exit if the user presses '2'
        break
    elif ipt1=='1':  # If the user presses '1' to buy an item
        item=input("Enter your Item: ").title()  # Ask for the item name
        if item in items_prices.keys():  # Check if the item exists in the dictionary
            try:
                quantity=int(input("Enter quantity: "))  # Ask for the quantity
                if quantity<=0:
                    print("Quantity must be greater than 0.")
                    continue
                price=(items_prices[item])*quantity  # Calculate the price for the item
                price_list.append((item, quantity, price))  # Add the item details to the price list
                total_price+=price  # Add the item price to the total price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst=(total_price/100)*13  # Calculate GST (13% of total price)
                final_amount=total_price+gst  # Calculate the final amount after GST
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
        else:
            print("Sorry! You entered Item not available..")  # Error message if the item is not available
    else:
        print("Oops! Wrong Input")  # Error message for wrong input

# Ask if the user is ready for the bill generation
inp2=input("Can I Bill the Items YES or NO: ").lower()

#Bill Generation if the user confirms
if inp2==('yes') and final_amount!=0:  # Executes If there is at least one item purchased
    print("\n")
    print("="*31, "Smart Bazaar", "="*32)  # Display the store name with decorations
    print(" "*32,"chodavaram")  # Store location (you can change this)
    try:
        print("Customer Name: ",name," "*20,"Date:",datetime.now())  # Print customer name and date
    except Exception as e:
        print("\nError: Could not retrieve the current date and time.")
        print("Possible Solution: Please ensure you have imported the 'datetime' module correctly.")
        print("If the error persists, check your Python environment and try importing 'from datetime import datetime'.")
        print("Error Details:", e)
        input("Press Enter to exit.")
        exit()  # Exit the program if there's an error
    print("-"*77)  # Separator for the bill
    print("S.No"," "*8,"ITEM"," "*8,"Quantity"," "*4,"Price")  # Header for the bill
    for i in range(len(price_list)):  # Loop through all the items purchased
        print(" ",i+1, " "*10, ilist[i]," "*12,qlist[i]," "*8,plist[i])  # Print each item's details
    print("-"*77)
    print(" "*38,"Total Amount:"," "*10,total_price)  # Total price
    print(" "*38,"GST Amount (13%):"," "*6,f"{gst:.4f}")  # GST amount
    print("-"*77)
    print(" "*38,"Final Amount:"," "*10,f"{final_amount:.4f}")  # Final amount after GST
    print("-"*77)
else:
    print("\nNo Items selected for Billing.") # Prints If No Items were selected

# Call the marquee function to display the "Thank You" message
marquee_thnq()  # The message will move across the screen
