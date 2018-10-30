# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 08:46:12 2018

@author: Chris
"""
import xml.etree.ElementTree as ETree
import uuid as UUID

class InventoryItem:
    def __init__(self,name,uuid = None):
        self.name = name
        if uuid is None:
            self.uuid = UUID.uuid4()
        else:
            self.uuid = UUID.UUID(uuid)
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "InventoryItem({},{})".format(self.uuid,self.name)
    
class Book(InventoryItem):
    def __init__(self,title,author = '',uuid = None):
        if uuid is None:
            super().__init__(title)
        else:
            super().__init__(title)
        self.title = title
        self.author = author
        
    def __str__(self):
        if self.author == '':
            return self.title
        else:
            return'{} by {}'.format(self.title,self.author)
class Inventory:
    def __init__(self):
        self.inventory_items = []
    def add_item(self,item):
        self.inventory_items.append(item)

    def remove_item(self,item_uuid):
        for item in self.inventory_items:
            if item.uuid == item_uuid:
                self.inventory_items.remove(item)
                
    def load_item(self):
        with open('BookList.txt','rb+') as filehandler:
            inventory_items = pickle.load(filehandler)
                     
                
    def save_item(self,inventory_items):
        with open('BookList.txt','wb+' ) as filehandler:#new code(save method)
            pickle.dump(inventory_items,filehandler)

    
      
#couldnt get either to work, it throws an TypeError: a bytes-like object is required, not 'str'

    def __str__(self):
        return '\n'.join(str(item)for item in self.inventory_items)

def main():
    library = Inventory()
    print("""
                 -------Main Menu-------
                 1. Load Book List
                 2. Add Book
                 3. Delete Book
                 4. Save Book
                 5. Quit  """)
    new_book = input('Please enter choice [1-5]: ')
    answer = int(new_book)
    if answer == 1:
       LibraryList = library.load_item()
       print(LibraryList)
       main()
  
    elif answer == 2:
      new_book = input('Please enter new book or type [done] to quit: ')
      while new_book != 'done':
        add_book = Book(new_book)
        library.add_item(add_book)
        new_book = input('Please enter new book or type [done] to quit: ')
      print (library)
      main()

    elif answer == 3:
      del_book = input('Please enter book to remove or type [done] to quit: ')
      while del_book != 'done':
        library.remove_item(del_book)
        del_book = input('Please enter book to remove or type [done] to quit: ')
      print(library)
      main()
    elif answer == 4:
      NewLibrary = library.save_item(Inventory)
      print(NewLibrary)
    else:
      main()
main()
    
