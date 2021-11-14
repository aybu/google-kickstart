
def silly_sub(p, n):
    """
        Brute-Force, to be improved ...
    """

    while True:
	    prev = p
        p = ( 
            p.replace('01', '2')
             .replace('12', '3')
             .replace('12', '3')
             .replace('23', '4')
             .replace('34', '5')
             .replace('45', '6')
             .replace('56', '7')
             .replace('67', '8')
             .replace('78', '9')
             .replace('89', '0')
             .replace('90', '1')
        )
        if prev == p:
            return p

T = int(input())
for i in range(T):
    N = int(input())
    P = input()
    result = silly_sub(P, N)
    print(f'Case #{i+1}: {result}')
    
