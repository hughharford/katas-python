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
# from mcpi import minecraft


class writeinthesky:


    x_direction = None  # 1 = +ve movement in the x-axis (north)
    y_direction = 1  # 1 = +ve movement in the y-axis (west)
    z_direction = 1  # 1 = +ve movement in the z-axis (up)
    mc_x_position = 0  # start x-coordinate in minecraft
    mc_y_position = 0  # start y-coordinate in minecraft
    mc_z_position = 0  # start z-coordinate in minecraft
    direction_show = 1

    writtensize = 1

    def set_mc(self, in_mc):
        self.mc = in_mc

    def set_mc_start_pos(self):
            # on top of the high up world 'joiner spot' is:
        x1 = 67.5
        y1 = 35.5
        z1 = -16

        # # # # # # # # # # # # # 
        # TELEPORT LINE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
        # # # # # # # # # # # # # 
        self.mc.player.setPos(x1, y1, z1)


    def set_mc_xyz(self, xyzinput):
        self.mc_x_position = xyzinput[0]  # set start x-coordinate in minecraft
        self.mc_y_position = xyzinput[1]  # set start y-coordinate in minecraft
        self.mc_z_position = xyzinput[2]  # set start z-coordinate in minecraft
    
    def set_write_direction(self, x_dir, y_dir, z_dir):
        # print(f'set_write_direction: {x_dir + y_dir + z_dir}')
        if (abs(x_dir) + abs(y_dir) + abs(z_dir)) == 1:
            self.x_direction = x_dir
            self.y_direction = y_dir
            self.z_direction = z_dir
            print('Writing direction set ok:')
            if x_dir > 0: print('+ve x direction - north')
            elif x_dir < 0: print('-ve x direction - south')
            elif y_dir > 0: print('+ve y direction - west')
            elif y_dir < 0: print('-ve y direction - east')
            else: 
                print('z direction! CAREFUL!! not implemented yet')
        else:
            raise ValueError('set only one of x, y, z as the write direction!')
        
        # we write form top of the letters down, so:
        self.z_direction = -1 
        
        # how to enable the use of the direction easily?
        # row * direction => would give change (+ve or -ve) to only the relevant direction
    
    def run_basics(self, inputarray=''):
        '''
        NOTE: starts from established x, y, z in MC
        '''
        if inputarray == '':        # if not provided, supply an array to work with
            s = np.array([[1,0,0,1, 0, 1,0,0,1, 0, 0,1,1,0, 0, 1,0,0,1],  # letters H U G  H, 7 rows, 4 columns
                          [1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1],
                          [1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,0, 0, 1,0,0,1],
                          [1,1,1,1, 0, 1,0,0,1, 0, 1,0,1,1, 0, 1,1,1,1],
                          [1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1],
                          [1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1, 0, 1,0,0,1],
                          [1,0,0,1, 0, 0,1,1,0, 0, 0,1,1,0, 0, 1,0,0,1]])
        # print('input:')
        # self.check_via_readout(s)
        # print("shape: {}".format(s.shape))
        written = self.write_array(s)
        # print('written:')
        # self.check_via_readout(written)

    def write_array(self, to_write):
        col, row = 0, 0 # row and column counts for actual output
        no_cols = to_write.shape[1]
        no_rows = to_write.shape[0]
        
        starter = np.zeros((no_rows, no_cols), dtype = np.int64)  # numpy: row first!
        # print(f'starter: \n{starter}') # just to show an empty starter, if we need to
        print("no rows {}, and no columns = {}".format(no_rows,no_cols))

        # going by rows
        for r in to_write:
            row += 1
            for c in r: # by cols
                col += 1
                rout = row-1
                cout = col-1
                if to_write[rout, cout] == 1:
                    # this is where we "write in the sky"
                    # print(to_write[rout,cout])
                    self.write_skyward(rout, cout)
                    starter[rout, cout] = 8
            col = 0 # resetting
        return starter

    def write_skyward(self, row_write, column_write):
        # call make block with block value
        # x is north-south, y is east-west, z is vertical 
        # column_write is columns in the letter array (can be directed either N/S or E/W)
        # z_pos is rows in the letter array
        
        # BELOW, TOOK OUT 2 x " * __direction", 1 for each x writing or y writing
        
        z = self.mc_z_position + (column_write * self.z_direction)
        if abs(self.x_direction):  # writing north-south orientation (+ve or -ve)
            if self.direction_show:
                print('writing north-south orientation (+ve or -ve)')
                self.direction_show = 0
            x = self.mc_x_position + (row_write * self.x_direction)
            y = self.mc_y_position # * self.y_direction
            self.mc_make_block(x, y, z)
            # i.e. y (east-west) is constant, x is our array columns, z is our array rows
        elif abs(self.y_direction):  # writing east-west orientation (+ve or -ve)
            if self.direction_show:
                print('writing east-west orientation (+ve or -ve)')
                self.direction_show = 0
            x = self.mc_x_position # * self.x_direction
            y = self.mc_y_position + (row_write * self.y_direction)
            self.mc_make_block(x, y, z)
            # i.e. y (east-west) is constant, x is our array columns, z is our array rows
        else:  
            raise ValueError('WRITING ERROR: that did"t work, can"t write as you intended')
    
    def mc_make_block(self, x, y, z):
        print(f'made block at x(n-s): {x}, y(e-w): {y}, z(up-down): {z}')
        s = self.writtensize
        # self.mc.setBlocks(x, y, z, s, s, s, 1) 


    def print_a_dot(self, r, c):
        print("r: {}, c: {}".format(r, c))
    
    def check_via_readout(self, to_write):
        print(to_write)
        

def main():
    # starting position
    startxyz = [68,35,16] # x,y,z
    # mc = minecraft.Minecraft.create()

    wits = writeinthesky()
    # wits.set_mc(mc)
    wits.set_mc_xyz(startxyz)
    wits.set_write_direction(0, 1, 0) # set (only 1 to = 1) direction here:
                    # x(n-s), y(e-w), z(up-down)
    wits.run_basics('') # supply input array here to print it

if __name__ == '__main__': main()