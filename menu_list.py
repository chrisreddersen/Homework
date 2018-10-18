# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:21:12 2018

@author: CHRIS
"""
def menu():
    menu_list = ['item1','item2','item3','item4','item5']#created a list to play with
    print("********MAIN MENU*********") #Designed a menu that will manipulate items in this list
    print("""
    1: Print List
    2: Delete Item from list
    3: Add Item to list
    4: Rename Item in list
    5: Exit """)
    menu_loop = True      #designed a loop
  
    while menu_loop != False:
        choice = input("Enter your choice [1-5]: ")
        answer = int(choice)    
        if answer == 1:
            for index,value in enumerate(menu_list,1):
                    numbered_list = ('{}.{}'.format(index,value))
                    print(numbered_list)
        elif answer == 2:
                delete_choice = input('which item would you like to delete?: ')
                menu_list.remove(delete_choice)
        elif answer == 3:
                add_item = input("Please enter item to be added: ")
                menu_list.append(add_item)
        elif answer == 4:
            rename_item = input('Please enter item to be renamed: ')
            if rename_item in menu_list:
                menu_list.remove(rename_item)
                new_name = input('What would you like to rename it?: ')
                menu_list.append(new_name)

            else: 
                print('This item is not in the list')
        elif answer == 5:
                print ("Good Bye")
                menu_loop = False #loop exit
        




 
    
