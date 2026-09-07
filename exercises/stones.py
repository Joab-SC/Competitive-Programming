def main():
   stones = input()
   colors = list(input())
   print(removeStones(colors))
   
def removeStones(list):
    counter = 0
    for i in range(len(list) -1):
        if list[i] == list[i+1]:
            counter +=1 
    return counter

   

    
main()