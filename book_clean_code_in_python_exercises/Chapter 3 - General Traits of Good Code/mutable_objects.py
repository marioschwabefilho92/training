def function(arg):
    arg += " in function "
    print(arg)

immutable = "hello"
function(immutable)

mutable = list("hello")
function(mutable)