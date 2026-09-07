"""
The layout of Farmer John's farm is quite peculiar, with a large circular road running around the perimeter of the main field on which his cows graze during the day. Every morning, the cows cross this road on their way towards the field, and every evening they all cross again as they leave the field and return to the barn.
As we know, cows are creatures of habit, and they each cross the road the same way every day. Each cow crosses into the field at a different point from where she crosses out of the field, and all of these crossing points are distinct from each-other. Farmer John owns exactly 26 cows, which he has lazily named A through Z (he is not sure what he will do if he ever acquires a 27th cow...), so there are precisely 52 crossing points around the road. Farmer John records these crossing points concisely by scanning around the circle clockwise, writing down the name of the cow for each crossing point, ultimately forming a string with 52 characters in which each letter of the alphabet appears exactly twice. He does not record which crossing points are entry points and which are exit points.

Looking at his map of crossing points, Farmer John is curious how many times various pairs of cows might cross paths during the day. He calls a pair of cows (a,b)
 a "crossing" pair if cow a
's path from entry to exit must cross cow b
's path from entry to exit. Please help Farmer John count the total number of crossing pairs.
"""


def main():
    s =input()
    print(get_crosses(s))
    
def get_crosses(s):
    crosses = 0
    reviewed = set([])
    for i in range(len(s)-1):
        l = s[i]
        
        j = i +1
        
        found =  set([])
        while j !=len(s) and s[j] != l:
            if s[j] in found:
                found.remove(s[j])
            elif s[j] not in reviewed:
                found.add(s[j])
            j+=1
        crosses += len(found)
        reviewed.add(l)
    return crosses
            
main()