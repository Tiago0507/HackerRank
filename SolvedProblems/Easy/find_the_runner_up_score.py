if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    runner_up = 0
    max_score = arr[0]
    for integer in arr[1:]:
        if integer > max_score:
            runner_up = max_score
            max_score = integer
        # elif max_score > integer > runner_up:
        #     runner_up = integer
    print(runner_up)
        