def f():
    print('Initiate f()')
    def g():
        print('initiate g()')
        print('End g()')
        return
    g()
    print('End f()')
    return
f()    