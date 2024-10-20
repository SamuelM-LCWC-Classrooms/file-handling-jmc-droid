def task_1():
    total = 0
   
    with open('task_1.txt', 'r') as file:
        
        for line in file:
            
            total += int(line.strip())

    return total


import csv

def task_2():
    
    menu = {}
    with open('menu.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu[row['Code']] = float(row['Price'])
    
    total_cost = 0
    print("Welcome to the Italian Takeaway Ordering System!")
    
    while True:
        
        order = input("Enter food codes separated by commas (or type 'done' to finish): ").strip()
        
        if order.lower() == 'done':
            break
        
        items = order.split(',')
        
        for item in items:
            item = item.strip()
            if item in menu:
                total_cost += menu[item]
                print(f"Added {item}, Price: £{menu[item]:.2f}")
            else:
                print(f"Sorry, {item} is not on the menu.")
    
    print(f"Your total cost is: £{total_cost:.2f}")
    return total_cost


    
import json

def task_3():
    
    with open('contact.json', 'r') as file:
        contacts = json.load(file)
    
    
    name = input("Enter the name to search: ").strip()
    
    if name in contacts:
        contact_info = contacts[name]
        number = contact_info.get('number', 'No number available')
        email = contact_info.get('email', 'No email available')
        return f"Number: {number}, Email: {email}"
    else:
        return "User not found."