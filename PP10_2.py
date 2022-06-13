def cheers(n):
    if n == 0:
        print("Hooray!", sep=" ")
    else:
        print("Hip!", end=" ")
        cheers(n-1)

cheers(5)