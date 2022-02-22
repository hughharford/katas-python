def digital_root(n):
    # ...
    # print(f'{digits_n} and sum of: {sum(digits_n)}')
    
    # HSTH 1st SOLUTION:
    o = sum([int(x) for x in str(n)])
    if len([int(x) for x in str(o)]) > 1:
        return digital_root(o)
    else: 
        return o
    
    
def digital_root_hsth(n):
    # ...
    # print(f'{digits_n} and sum of: {sum(digits_n)}')

    # HSTH ORIGINAL SOLUTION:
    '''  '''
    o = sum([int(x) for x in str(n)])
    if len([int(x) for x in str(o)]) > 1:
        return digital_root_hsth(o)
    else: 
        return o
    

def digital_root_sharpest(n):
    # SHARPEST SOLUTION ON CODEWARS:
    ''' '''
    return n % 9 or n and 9
    
    
def digital_root_experimental(n):    
    return n % 9 or 9
    # n and 9 

def main():
    f = 10899
    print(f'n % 9: {f % 9}')
    print(f'n and 9: {f and 9}')
    print(f'f is: {f}')
    print(f'hsth: {digital_root_hsth(f)}')
    print(f'sharpest: {digital_root_sharpest(f)}')
    print(f'experimental: {digital_root_experimental(f)}')


if __name__ == '__main__': main()
