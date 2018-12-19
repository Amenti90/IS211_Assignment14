# the fibonacci function

def fibonacci(n):
    if n < 2:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


# the greatest common denominator function
def gcd(a,b):
    if a %b == 0:
        return b
    while a:
        return (b(a%b))

# the string comparison function compareTo
def compareTo(s1,s2):
    if s1==s2:
        return 0
    if s1< s2:
        return s1-s2
    if s1>s2:
        return s1-s2




# def compareTo(s1,s2):
print "A Comparison of s1: 12876 and s2: 19839187"
print compareTo(12876, 19839187)






