import sys

if len(sys.argv) != 1:
    print("none")
else:
    table = 0
    while table <= 10:
        num = 0
        print(f"Table de {table}:", end="")
        while num <= 10:
            print(f" {table * num}", end="")
            num += 1
        print()
        table += 1
        
