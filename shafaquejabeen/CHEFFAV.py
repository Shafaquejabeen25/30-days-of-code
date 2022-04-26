T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    V=S.find("chef")
    B=S.find("code")
    if (B>V):
        print("WA")
    else:
        print("AC")
