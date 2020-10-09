def check_input(ans):
    global mem
    a = "".join(ans.split())
    a = a.split("=")
    if len(a) == 2:
        if a[0].isalpha():
            if a[1].isdigit():
                mem[a[0]] = (a[1])
            elif a[1].isalpha():
                if a[1] in mem.keys():
                    mem[a[0]] = mem[a[1]]
                else:
                    print("Unknown variable")
            elif not a[1].isdigit():
                print("Invalid assignment")

        else:
            print("Invalid identifier")
    else:
        print("Invalid assignment")


def validate(ans):
    z = ans
    x = ""
    for i in z:
        if not i.isalpha():
            x += " " + i + " "
        else:
            x += i
    v = x.split()
    y = None
    if len(v) == 1:
        if v[0] in mem.keys():
            y = mem[v[0]]
        else:
            y = ("Unknown variable")
    else:
        for i in range(len(v)):
            if v[i] in mem.keys():
                v[i] = mem[v[i]]
        y = "".join(v)
    return y


def final_out(ans):
    try:
        if "//" in ans:
            raise ValueError
        print(int(eval(ans)))
    except (ValueError, NameError, SyntaxError):
        print("Invalid expression")


mem = {}
while True:
    answer = input()
    if not answer:
        pass
    elif answer[0] == "/":
        if answer == "/help":
            print("Adding sequence of numbers")
        elif answer == "/exit":
            print("Bye!")
            break
        else:
            print("Unknown command")
    elif len(answer) >= 1:
        if "=" in answer:
            check_input(answer)
        else:
            out = validate(answer)
            if out == ("Unknown variable"):
                print(out)
            else:
                final_out(out)

