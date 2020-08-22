#while(true):

try:
    def add():
        n1=int(input('enter a number\n'))
        n2=int(input('enter a number\n'))
        sum=n1+n2
        print('n1 and n2 equal=',sum)
    add()
except ValueError:
        print('plz enter a integer type value')



