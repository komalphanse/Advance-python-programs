def scope_func():
    print("inside scope function")
    def scope_inner_func():
        var=20
        print("inside inner function value of var:",var)
    scope_inner_func()
    print("try printing var from outer function:",var)#var can not access outside the function 
scope_func()        
