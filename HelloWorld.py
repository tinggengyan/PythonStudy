import math

# this is a comment
print 'Hello1';
print "Hello2";
print('Hello3');
print("Hello4");

# compute the math
print(4 + 2);
print(4.0 + 2);

# get the type
a = 9;
print(type(a))
print(type(4.0))

# absoulute value
print(abs(-9))

# round
print(round(1.2345))
print(round(1.2345, 2))

# floor
print(math.floor(32.999))

# pow
print(pow(2, 3))

# sqrt
print(math.sqrt(4))

print(2 / 5)
print(2.0 / 5)
print(2 / 5.0)
print(2.0 / 5.0)

# mode
print(5 % 2)
print(5.0 % 2)
print(divmod(5, 2))

# string
print('hello "world!"')
print("hello,'world'")
print('what\'s your name?')
a = 'steve'
b = 'yan'
print(a + b)
c = 900;
# link the string and number
print(a + `c`)
print(b + str(c))
print(a + repr(c))
