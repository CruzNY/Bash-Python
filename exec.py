#!/usr/bin/python3

import os
import time
start_time = time.time()
fileName = input('Enter java filename  ')
print()
print('----------------------------------------------------------------------------')
print()
os.system('javac '+fileName+'.java')
os.system('java '+fileName)
print('complete')
print()
print('Program Build Time: ', time.time() - start_time)
print()
print('----------------------------------------------------------------------------')
print()
