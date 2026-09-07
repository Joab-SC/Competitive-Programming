""""
After a glorious night of stand-up comedy, a comedian wants to measure their success. Not with surveys, not with likes, but with real crowd noises! Luckily, the mic captured all the reactions during the routine. The audio has been converted into a single string S
full of mashed-up sounds, such as applause, laughs, boos, etc.
"""

def main():
    points = 0
    i = input()
    temp = ""
    for char in i:
        temp += char
        if "bravo" in temp:
            points += 3
            temp = ""
        elif "ha" in temp:
            points += 1
            temp = ""
        elif "booo" in temp:
            points += -1
            temp = ""
            
    print(points)
        
main()