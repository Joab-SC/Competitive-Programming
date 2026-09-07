def main():
    n = int(input())
    for _ in range(n):
        l,r,c = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(sum_pairs(r,c,arr))
    
def sum_pairs(rows,columns, arr):
    possible_numbers = [x for x in arr  if x <= rows or x <= columns]
    if rows == columns:
        return len(possible_numbers)//2
    
    minimum_line = min(rows, columns)
    only_max_numbers = [x for x in possible_numbers if x > minimum_line] 
    both_numbers = [x for x in possible_numbers if x not in only_max_numbers]
    
    if len(both_numbers) <= len(only_max_numbers):
        return len(both_numbers)
    else:
        return len(only_max_numbers) + (len(both_numbers) - len(only_max_numbers))//2 
    
main()