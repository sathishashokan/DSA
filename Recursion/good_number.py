from math import ceil

MOD = 10**9 + 7
def good_number(n):
    even = (n+1)//2
    odd = n//2
    def pow(x, n):
        x %= MOD
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==1:
            return x * pow(x, n-1) % MOD
        return pow((x * x)%MOD, n//2)
    return pow(5, even) * pow(4, odd) % MOD

print(good_number(4))
