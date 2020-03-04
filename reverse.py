n=int(input())
a=list(map(int,input().split()))
r=a[::-1]
x=map(str,r)
print("->".join(x))
