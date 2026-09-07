import math

def main():
    c = int(input())
    left_overs = {}
    left_overs["S"] = 0
    left_overs["M"] = 0
    left_overs["L"] = 0
    for _ in range(c):
        size, slices = input().split()
        slices = int(slices)
        left_overs[size] += slices
            
    boxes = calc_boxes(left_overs)
    print(boxes)
    
def calc_boxes(left_overs):
    boxes = 0
    boxes += math.ceil(left_overs["S"]/6)
    boxes += math.ceil(left_overs["M"]/8)
    boxes += math.ceil(left_overs["L"]/12)
    return (boxes)
main()