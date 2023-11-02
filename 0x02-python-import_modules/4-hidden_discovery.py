#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    array = dir(hidden_4)
    for j in range(len(array)):
        if (array[j][:2] != "__"):
            print(array[j])
