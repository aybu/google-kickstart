
def transform(s, f):
    time = 0
    num_letters = 26

    for char1 in s:
        min_dist = num_letters
        for char2 in f:
            diff = ord(char1) - ord(char2)
            min_dist = min(min_dist, min(-diff % num_letters, diff % num_letters))
        time += min_dist

    return time

T = int(input())
for i in range(T):
    S = input()
    F = input()
    result = transform(S, F)
    print(f'Case #{i+1}: {result}')
    
