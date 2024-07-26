if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        operation = command[0]
        
        if operation == 'insert':
            index = int(command[1])
            value = int(command[2])
            my_list.insert(index, value)
        elif operation == 'remove':
            value = int(command[1])
            my_list.remove(value)
        elif operation == 'append':
            value = int(command[1])
            my_list.append(value)
        elif operation == 'sort':
            my_list.sort()
        elif operation == 'pop':
            my_list.pop()
        elif operation == 'reverse':
            my_list.reverse()
        elif operation == 'print':
            print(my_list)
    