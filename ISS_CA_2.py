def find_cube_pairs(targ): # added colon and changed target to targ
    sol = [] # rmeoved semicolon
    max_num = round(targ ** (1/3))  # removed *** to **

    for a in range(1, max_num + 1): # changed ranges-> range
        for b in range(a, max_num + 1): # added colon && changed ranges-> range
            if a**3 + b**3 == targ: #removed *** , added colon 
                sol.append((a, b))#removed semicolon
    return sol
#semi colons have been removed, even if they remained they wouldn't have caused any problem
pairs = find_cube_pairs(1729) # comma removed
print("Valid cube pairs for 1729:") #comma removed
for a, b in pairs:   # no colon and the identifier was wrong
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") #changed b**2 to b**3 and a**2 to a**3
