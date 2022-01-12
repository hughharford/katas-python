'''
Created on 2 Nov 2020

@author: hsth
'''
import unittest

class Test(unittest.TestCase):

    def testName(self):
        
        import os
        import random
        
        print(dir(os))
        print("\n")
        print(os.name)
        print("\n")
        print(os.O_PATH)


        mySnack1 = "crumpets"
        annaSnack1 = "fruit and nuts / fruit 'n nut"
        
        snacksX2 = mySnack1 + " ___with___" + annaSnack1
        
        snacksX5 = [mySnack1, 
                    "fruit with nuts", 
                    "fruit 'n nut chocolate", 
                    "toast", 
                    annaSnack1]
        
        for i in range (0,100):
            print(snacksX2 + "\n")

        print(snacksX5)
        print(mySnack1 in snacksX5)
        
        mySnack1, annaSnack1 = annaSnack1, mySnack1
        print("mySnack1 now = " + mySnack1)
        print("\n")
        print("annaSnack1 now = " + annaSnack1)
        print("\n")
        
        print(7 % 2)
        print("\n")
        
        prices = [9.42, 5.67, 3.25, 13.40, 7.5]
        print("lowest price is: " + str(min(prices)))
        # print("\n")

        print("highest price is: " + str(max(prices)))

        limit = random.randint(11,200)
        for j in range(1,limit):
            print(mySnack1)
        
        print(limit)
        randIndex = random.randrange(0,len(snacksX5))
        print("selected snack: " + str(snacksX5[randIndex]))
        print("price of selected snack: " + str(prices[randIndex]))

        def first_func(x):
            return x*2
        
        print(str(first_func(10)))
        
        print(str(first_func('hello ')))
        
        def add(a, b):
            return a+b
        
        def add2(a, b):
            print(a+b)
        
        print(str(add(10, 5)))
        print(str(add("a","b")))
        
        print("\n add and add2 functions \n")
        x = add(7,3)
        print(x)
        
        x = add2(2,3)
        print(x)
        
        print("\n ")
        x = add
        
        
        def f(a, b, c = 1):
            return (a + b) * c
        
        print("\n f: ")
        print(f(1,2))
        print(f(1,2,7))
        
        print(f(a=3, b=2, c = 9))
        
        def g(a, b, c=1):
            return (a + b) * c

        # EXERCISES top of page 25
        
        def all_the_snacks(snack, num, spacer = ", "):
            print((snack+spacer)*num)
        
        all_the_snacks(snacksX5[randIndex], 5, " :: ")
        
        def in_snack_list(snacklist, snackToCheck):
            print(snackToCheck in snacklist)
        
        in_snack_list(snacksX5, "toast")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()