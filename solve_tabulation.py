# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        # Primera fase: Rellenamos la tabla 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        if len(items)==0:
            return 0

        if len(items)==1:
            table.append(items[0])

        if len(items)>1:
            table.append(items[0])
            table.append(max(items[0], items[1]))

            for i in range(2, len(items)):
                table.append(max(table[i - 2] + items[i], table[i - 1]))
        return
        
    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. 
        if len(items)==1:
            taken.append(len(items))
            return
        if len(items)==2:
            taken.append(items.index(max(items[0], items[1]))+1)
            return
        i = len(table) - 1 #longitud
        b = table[-1] #ultimo valor de la tabla
        while i > 1 and b > 0:
            if table[i] <= b and table[i] != table[i - 1]:
                taken.insert(0, i + 1) #el ladrón robó en la casa
                b = b - items[i]
                i -= 2
            else:
                i -= 1
        taken.insert(0, i + 1)

        return
        
    fill_table()
    fill_taken()
    return table[-1], taken
