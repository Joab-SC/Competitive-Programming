"""
You are given a string s
 consisting of digits from 1
 to 4
.

Let's say that the string is beautiful if it is impossible to select some of its elements and write them out (in the same order as they appear in the string) to form a number that is a multiple of 4
. For example, the strings 31, 222, 213 are beautiful, while the strings 143, 3123, 1322 are not. The empty string is considered beautiful.

Your task is to calculate the minimum possible number of elements in the string s
 that need to be removed in order to make it beautiful.
"""
        
def main():
    n = int(input())
    for _ in range(n):
        counter = 0
        st = input()
        counter += st.count("4")
        st = st.replace("4", "")
        
        
        pairs = []
        id_count = 0
        for i in range(len(st)):
            item = (id_count, st[i])
            if st[i] != "2":
                for _ in range(i, len(st)-1):
                    pairs.append([item, None])
            for pair in filter_pairs(pairs):
                pair[1] = item 
            id_count +=1
            
        multiple_pairs = filter_multiple_pairs(pairs)
        while(multiple_pairs):
            highest = get_highest(multiple_pairs)
            for i in range(len(multiple_pairs) -1, -1, -1):
                pair = multiple_pairs[i]
                if pair[0] == highest or pair[1] == highest:
                    multiple_pairs.remove(pair)
            counter += 1
        print(counter)
        
def get_highest(pairs):
    total = [x for sublista in pairs for x in sublista]
    frecuencias = {}
    for el in total:
        frecuencias[el] = frecuencias.get(el, 0 ) + 1
    return max(frecuencias, key=frecuencias.get)
    
       
def filter_multiple_pairs(pairs):
    filtered = []
    for pair in pairs:
        number = int(pair[0][1] + pair[1][1])
        if number%4 == 0:
            filtered.append(pair)
    return filtered


def filter_pairs(pairs):
    filtered = []
    for pair in pairs:
        if pair[1] == None and pair not in filtered:
            filtered.append(pair)
    return filtered 
    
                    
                    
                    
                
                

        
        
        
main()
