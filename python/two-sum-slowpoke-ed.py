# TWO SUM
# SLOWPOKE EDITION

def two_sum(numbers, target):
    nr, nl = 0, 0
    ir, il = 0, 0
    nmax = max(numbers)
  
    while nr != nmax:
        if nr not in numbers or nl > nmax:
            nr += 1
            nl = nr

        else:
            ir = numbers.index(nr)
            
            if nl in numbers or (nl == nr and numbers.count(nl) > 1):
                if numbers.count(nl) > 1:
                  numbers[ir] = "_"
                
                il = numbers.index(nl)
                if not ir == il and nr + nl == target:
                  return (ir, il)

                numbers[ir] = nr

            nl += 1
