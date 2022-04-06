# PRACTICE GENERAL ALGORITHMS

## CONTENTS

1. HackerRank
2. CodeWars


## HackerRank



## CodeWars

1. [DNA to RNA Conversion](https://www.codewars.com/kata/dna-to-rna-conversion/train/python)
    ### Comprehensions:
    ```Python
    def DNAtoRNA(dna):
        return "".join(["U" if c=="T" else c for c in dna])
    ``` 
    ### Simple Replace:
    ```Python
    def DNAtoRNA(dna):
        return dna.replace('T', 'U')
    ```
    ### My solution (comprehension and lambda!)
    Complex, but first ever lambda usage. Just need to get better at comprehensions, see above
    ```Python
    def dna_to_rna(dna):
    convert = lambda char : "U" if char == "T" else char
    return "".join([convert(char) for char in dna])
    ```
2. [Playing Banjo](https://www.codewars.com/kata/are-you-playing-banjo/train/python)
Simple enough:
    ```Python
    def are_you_playing_banjo(name):
        return name + (' plays banjo' if name[0].lower() == 'r' else ' does not play banjo')
    ```
3. [Opposites Attract](https://www.codewars.com/kata/555086d53eac039a2a000083/train/python)
    ### My solution
    ```Python
    def lovefunc( flower1, flower2 ):
        f1 = flower1 % 2
        f2 = flower2 % 2
        return (f1 == 0 and f2 == 1) or (f2 == 0 and f1 == 1)  
    ```
    ### Other neat
    ```Python
    def lovefunc( flower1, flower2 ):
        return (flower1+flower2)%2
    ```
    ### Other neat with lambda
    ```Python
    lovefunc=lambda a,b:(a+b)%2
    ```
4. more
```Python
```
   