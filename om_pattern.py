def create_om(k=10):
    kk = k+1
    for i in range(1, kk):
        print()
        for j in range(1, kk):
            if j == kk//2 and i != j or (j == k and i > kk//2):
                print("+", end='')
            elif i == kk//2 or (i == 1 and j < kk//2) or (i == k and j < kk//2):
                print("+", end=' ')
            else:
                print(" ", end=' ')


create_om()
