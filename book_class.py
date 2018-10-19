# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:05:30 2018

@author: Chris
"""

#import xml.etree.ElementTree as ETree

import uuid
class InventoryItem:
    def __init__(self,name):
        self.name = name
        self.uuid = uuid.uuid4()
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "InventoryItem({},{})".format(self.uuid,self.name)
    
class Book(InventoryItem):
    def __init__(self,title,author = ''):
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
    def __str__(self):
        return '\n'.join(str(item)for item in self.inventory_items)




    


    
                
        
    
        
