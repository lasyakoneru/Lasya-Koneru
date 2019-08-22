#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:33:33 2019

@author: lasyakoneru
"""


phone_number = int(input('Enter a ten digit phone number that you would like to be seperated by hyphens: '))
print()

last_set = phone_number % 10000
remainder = phone_number//10000
middle_set = remainder % 1000
first_set = remainder// 1000

print(str(first_set) + '-' + str(middle_set) + '-' + str(last_set))