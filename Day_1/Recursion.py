# Function thats callzz its self is know as Recursion Function
#printing 1 to 4 by using the Recursion function

def inc( number ) :
    if number == 5 :
        return 5
    else :
        print(number)
        return inc( number + 1 )

print(inc(1))