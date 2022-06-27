# Python 101 notes

## CONTENTS
- Mostly CodeWars and Learn examples with my comments
### Day 2 - Lists


### Day 2 - Lists
- For loop versus comprehension example 1
- Code Kata name:
  - `MEXICAN WAVE`
- Good example (with comprehension):
  ```Python
  def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
  ```
- My submission (for loop):
  ```Python
  def wave(people):
    out = []
    print(people)
    if len(people):
        for i in range(len(people)):
            temp = people
            if temp[i] != ' ':
                out.append(temp[0:i]+temp[i].upper()+temp[i+1:])
    print('out = ' + str(out))
    return out
  ``` 

- For loop versus comprehension example 2
- Code Kata name: 
  - `MULTIPLICATION TABLE`
- Good example (with comprehension):
  ```Python
    def multiplicationTable(size):
        return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
  ```
- My solution (complex!):
  ```Python
    def multiplication_table(size):
    # get lead sides
    lead_side = [x+1 for x in range(size)]
    
    # set lead sides
    output = []
    newout = []
    add = 2
    for row in range(size):
        if row == 0:
            output.append(lead_side)
        else:
            temp1 = [None]*size
            temp1[0] = row+1
            output.append(temp1)

    # calculate the rest
    for row in range(size):
        mult = output[0][row]
        for col in range(1,size):
            if row > 0 and col != 0:
                output[row][col] = (col+1)*mult 
    
    return output
  ```
  - Another For loop solution, without all the complexity!
  ```Python
  def multiplication_table(size):
    columns = []
    for i in range(1,size+1):
        rows = []
        for j in range(1,size+1):
            rows.append(i*j)
        columns.append(rows)
        
    return columns
  ```

  ### Python101 day 3 - Dicts
  - For loop versus comprehension example 
  - Code Kata name:
    - `COUNTING DUPLICATES`
    - n.b. must use DICTS
  - Good example (with comprehension):

  - Better solution from CodeWars: (but this doesn't use a dict!)
    ```Python
        def duplicate_count(s):
          return len([c for c in set(s.lower()) if s.lower().count(c)>1])
    ```

  - My solution
    ```Python
      def duplicate_count(text):
        # print(text)
        dups = {}
        for char in text:
            if dups.get(char.lower(), 0) == 0:
                dups[char.lower()] = 1
            else:
                dups[char.lower()] = dups[char.lower()] + 1
            
        return len([value for value in dups.values() if value > 1])

    ## ATTEMPTS at comprehensions:
    # new_dict_comp = {key:dups.value[key] for key,value in dups if dups.value[key] > 0}
    # sum({(True if value > 1) for value in dups})
    ```