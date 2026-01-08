try: 
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    if x1 not in [0, 1] or x2 not in [0, 1]:
        raise ValueError
    
    gx = x1 + x2
    threshold = 1

    if gx >= threshold:
        y = 1
    else:
        y = 0

    print("y =", y)
    

except ValueError:
    print("Please enter binary inputs.")
