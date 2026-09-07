"""
You are fighting a boss with an unknown amount of health. You have a sequence of n
 spell cards, where the i
-th card deals ai
 damage. You can rearrange your hand and play the cards in any order you choose.

The boss has an adaptive shield. If you ever play two cards in a row that deal the exact same amount of damage, the shield permanently activates. The card that triggers the shield still deals its normal damage, but all subsequent cards you play will deal 0
 damage.
 

Find the maximum total health the boss can have such that you will defeat him if you arrange and play your cards optimally.
"""
def main():
    cases = int(input())
    for i in range(cases):
        _ = input()
        cards = list(map(int, input().split()))
        maxi = get_max(cards)
        print(maxi)
        
def get_max(cards):
    dicti={}
    for i in cards:
        if i not in dicti:
            dicti[i] = 0
        dicti[i]+=1
    loc_max = max(dicti.values())
    m = len(cards) - loc_max
    
    maxi = 0
    if loc_max <= m + 2:
        maxi = sum(cards)
    else:
        maxi = sum(cards) - (loc_max - (m + 2)) * max(dicti, key = dicti.get)
    return maxi
        
            
main()