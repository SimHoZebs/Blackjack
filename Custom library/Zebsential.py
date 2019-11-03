def Debug(text, *do):
    #If DO_DEBUG == 1, text will print.
    #If Do_DEBUG == 0, text will not print.
    #Buf if do == 1, it will overwrite DO_DEBUG and print anyway.
    #And if do == 0, it will overwrite DO_DEBUG and not print anyway.
    #if do is left empty it will just follow DO_DEBUG.

    if not bool(do):
        if something == 1:
            print(text)

    elif do[0] == 1:
        print(text)

def DoDebug(value):
    global something
    something = value
