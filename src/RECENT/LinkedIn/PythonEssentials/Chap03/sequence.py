#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = ( 1, 2, 3, 4, 5 )
# error, as tuple: x[3] = 42
for i in x:
    print('i is {}'.format(i))
