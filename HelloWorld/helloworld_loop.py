#   define func
def hello(n, output = True):
    """Prints hello world n-times"""

    #   if output is true
    if output is True:
        #   Loop
        for i in range(n):
            #   print string
            print("Hello World Loop style", i+1 )
    else:
        print("Output = False")

#   Call hello
hello(4, output = True)