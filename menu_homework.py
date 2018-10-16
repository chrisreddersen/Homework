#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:18:25 2018

@author: chris
"""
from menu_list import menu
def main():
    print (" LIST MANIPULATION MENU")
    choose = input('Would you like to play?[y or n]: ')
    if choose == 'y':
        menu()

    else:
        pass
    

main()
    