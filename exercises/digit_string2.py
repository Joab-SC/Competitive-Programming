def main():
    n = int(input())
    for _ in range(n):
        st = input()
    
        necessary_twos = 0
        necessary_others= 0 
        fours = 0
        fours += st.count("4")
        st = st.replace("4", "")
        i = 0
        while(i < len(st) and st[i] == "2" ):
            i+= 1
        
        st = st[i:len(st)]
        
        necessary_twos = st.count("2")
        
        for i in range(0, len(st)):
            if (st[i]  == "1" or st[i] == "3") and "2" in st[i+1:len(st)]:
                necessary_others += 1
        print(min(necessary_twos + fours, necessary_others + fours))
main()