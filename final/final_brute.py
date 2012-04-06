
cells = 4
particles = 6

count = 0
valid = 0

for a in range(cells):
    for b in range(cells):
        for c in range(cells):
            for d in range(cells):
                for e in range(cells):
                    for f in range(cells):
                        count += 1
        
                        for x in range(cells):
                            if x not in [a,b,c,d,e,f]:
                                valid += 1
                                break

print valid
print count
