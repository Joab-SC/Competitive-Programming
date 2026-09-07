"""
A Ministry for Defense sent a general to inspect the Super Secret Military Squad under the command of the Colonel SuperDuper. Having learned the news, the colonel ordered to all n squad soldiers to line up on the parade ground.

By the military charter the soldiers should stand in the order of non-increasing of their height. But as there's virtually no time to do that, the soldiers lined up in the arbitrary order. However, the general is rather short-sighted and he thinks that the soldiers lined up correctly if the first soldier in the line has the maximum height and the last soldier has the minimum height. Please note that the way other solders are positioned does not matter, including the case when there are several soldiers whose height is maximum or minimum. Only the heights of the first and the last soldier are important.
"""
def get_swapps(arreglo):
    maximum = max(arreglo)
    index_max = min([i for i, x in enumerate(arreglo) if x == maximum])
    minimum = min(arreglo)
    index_min = max(i for i, x in enumerate(arreglo) if x == minimum)

    
    
    counter = 0
    
    minimum_interchanges = len(arreglo) - index_min - 1
    maximum_interchanges = index_max
    counter = maximum_interchanges + minimum_interchanges
    if index_max > index_min:
        counter -= 1
    
    return counter
    

def main():
    columnas = input()
    bloques_columna = list ( map( int, input().split()))
    print(get_swapps(bloques_columna))
    

            

main()