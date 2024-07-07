if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    permutations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    clean_permutations = [row for row in permutations if sum(row) != n]
    print(clean_permutations)