def main():
    n = int(input ())
    print(get_combs(n))
    

def get_combs(n):
    combs = []
    get_combs_i(n,[], combs)
    return combs

def get_combs_i(n, st, combs):
    if len(st) == n:
        combs.append("".join(st))
        return
    
    st.append('0')
    get_combs_i(n, st, combs)
    del st[-1]
    
    st.append('1')
    get_combs_i(n, st, combs)
    del st[-1]
    
    st.append('2')
    get_combs_i(n, st, combs)
    del st[-1]
main()

"""
si cumple condicion (termino de construir camino)
    agreagr camino a resultado 
    return 
    
decision 1
seguir camino
devolver decision 1

decision 2
seguir camino
devolver decision 2
"""
