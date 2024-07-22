# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
def lexicographic_permutation(S, k):
    S = sorted(S)
    perms = permutations(S, k)
    for perm in perms:
        print(''.join(perm))
            
if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    lexicographic_permutation(S, k)