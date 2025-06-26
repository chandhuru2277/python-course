with open("File-and-Error-handling/data.txt", "r") as f:
    data= f.read()
    print(data)

    # tell position
    print(f.tell())
    
    # seek
    f.seek(0,2) # move to end
    print(f.tell())

    f.seek(0) # move to start
    print(f.tell())

    