target = 12321
if target>0:
    s = str(target)[::-1]
    if int(s) == target:
        print("true")
    else:print("bad")