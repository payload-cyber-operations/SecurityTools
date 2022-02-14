import getopt
import sys



def global_variables():
    global number1
    global number2


global_variables()

try:
    opt, args = getopt.getopt(sys.argv[1:], "a:b:c:",["arturo=","bacilio=","carlos="])
    #print(opt)
    for o, a in opt:

        if o in ("-a","--arturo"):
            number1 = int(a)
        elif o in ("-b","--bacilio"):
            number2 = int(a)



    print(number1 + number2)

except Exception as e:
    print(str(e))
