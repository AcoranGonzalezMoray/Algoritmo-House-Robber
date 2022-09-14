# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}
    def t(n):
        if n<0:
            return 0;
        if n==0:
            return items[0]
        if n==1:
            return max(items[0], items[1])

        mem[n] = max(t(n-2)+items[n], t(n-1))
        return mem[n]

    return t(len(items)-1)
