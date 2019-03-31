def cuenta_progresiva (i, x):
    print(i, end=', ')
    if (i >= x):
        return
    else: cuenta_progresiva (i+1, x)
