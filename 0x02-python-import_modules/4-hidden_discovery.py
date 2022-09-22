#!/usr/bin/python3.8
if __name__ == "__main__":
    import hidden_4
    files = dir(hidden_4)
    for i in range(len(files)):
        if (files[i][0:2] == "__"):
            continue
        print(files[i])
