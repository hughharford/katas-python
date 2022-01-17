'''
Created on 25 Dec 2021

@author: hsth

Christmas day coding for G & I Short

Plan:
     >> Make writing in the sky (wits) in Minecraft
     >> 
     >> 
     >>  
'''
import numpy as np

class writeinthesky:
    
    def run_basics(self):
        
        s = np.array( [[1,0,0,1],
                       [1,0,0,1],
                       [1,0,0,1],
                       [1,1,1,1],
                       [1,0,0,1],
                       [1,0,0,1],
                       [1,0,0,1]])
        
        print(s)
        print("size: {}".format(s.shape))
        
        returned_pos = self.write_array(s)
        print("returned_pos = ", format(returned_pos))

        self.check_via_readout(s)


        return returned_pos

    def write_array(self, to_write):
        pos = [0,0]
        no_cols = to_write.shape[1]
        no_rows = to_write.shape[0]
        print("no columns = {}, and no rows {}".format(no_cols, no_rows))

        col, row = 0, 0 # row and column counts for position
        # going by rows (x = rows)
        for x in to_write:
            row += 1
            pos[0] += 1 # counting rows tracked through 

            for y in x:
                col += 1
                pos[1] += 1 # counting items tracked through 
                # print("x: {} y: {} col: {} row: {}".format(x,y,col,row))
                self.print_a_dot(col, row)
            col = 0 # resetting

        return pos

    def print_a_dot(self, pos_x, pos_y):
        print("LOOKING TO PRINT @ x: {}, y: {}".format(pos_x,pos_y))

    def print_a_dot(self, pos_x, pos_y):
        print("x: {}, y: {}".format(pos_x,pos_y))
    
    def check_via_readout(self, to_write):
        no_cols = to_write.shape[1]
        no_rows = to_write.shape[0]
        readout = np.zeros((no_rows, no_cols))
        print(readout) 


def main():
    writeinthesky.run_basics()

if __name__ == '__main__': main()
