n = int(input())
answer = []
for i in range(n):
    num = int(input())
    Q=num//25
    num = num - 25*Q
    print(Q, end=" ")
    D=num//10
    num = num - 10*D
    print(D, end=" ")
    N=num //5
    num = num - 5*N
    print(N, end=" ")
    P=num//1
    print(P)
    