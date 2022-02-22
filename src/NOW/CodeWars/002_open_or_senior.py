def open_or_senior(data):
    # HSTH 1st solution
    out = []
    # print(data)
    for pair in data:
        if pair[0] > 54 and pair[1] > 7:
            out.append('Senior')
        else:
            out.append('Open')

    return out

def open_or_senior_sharp(data):
    # codewars sharp solution: straight to list comprehension output
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

def open_or_senior_lambda(data):
    # codewars sharp solution: return list via lambda
    return map(lambda d: 'Senior' if d[0] >= 55 and d[1] > 7 else 'Open', data)

def main():
    input = [(45, 12),(55,21),(19, -2),(104, 20)]
    print(open_or_senior(input))

if __name__ == '__main__': main()