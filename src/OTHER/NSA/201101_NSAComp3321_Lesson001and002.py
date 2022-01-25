'''
Created on 1 Nov 2020

@author: hsth
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        #NSA COMP3321 - first lesson exercises

        p1 = "fermented lemons"
        p2 = "a peaceful sleeping Bernie"
        p3 = "a money tree"
        p4 = "homemade bagels"
        p5 = "Shortcake's chilli con carne"
        
        c1 = 9.42
        c2 = 5.67
        c3 = 3.25
        c4 = 13.40
        c5 = 7.50
        
        print(c1+c2+c3+c4+10*c5)
        print("\n", p1, "\n", p2, "\n", p3, "\n", p4, "\n", p5)
        
        x = len("blood-oxygenation level dependent function magnetic resonance imaging")
        print(x)
        
        print((p4 + ", ") * 100 + "\n \n")
        
        
        print("\n \n")
#        print(dir(p1).x)
#        print(_)
        print(dir(p1))
        print("\n \n")
        
        print("is p1 a string? " + str(isinstance(p1, str)))
        
        p1 = 75
        print("is p1 now an integer? " + str(isinstance(p1, int)))
        
        a = b = c = 77
        
        print(a)        
        
        x, y = 1, 2
        z = 1, 2
        x, y = 1, 2
        print(x, " ... ", y)

        x, y = y, x
        
        print(x, " ... ", y)
        print(z)
        print(x, "   ", y, "   ", z)
        
        print(dir())
        
        a = [1,2,3,4]
        
        print("Printing 1 in a, and 5 in a:")
        print(1 in a)
        print(5 in a)
        
        # NOT DOING AS EXPECTED...!
        self.assertTrue(4 in a, "asserting 5 in a, failing if not the case") 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()