a = '12.09'
b = "hello"

a = """123sajhdjksfnmdsnfmsdnfm,nfm,sdnfmsdm,nm,sdfn,m
sdmndsam,nsadmansdsadmasmdnas,
dsa,ndmnsm,dnasdmna,dsm,StopAsyncIteration
jahjdhasdjkhadjkhasdjhjkhaskjhdkjas"""
print(a)


b = "Hello, World!"
print(b[2:5])
print(b[:2])
print(b[2:])

print(b[-5:-2])


a = "Hello"
print(a.upper())
print(a.lower())


b = " hello@gmail.com "
print(b)
print(b.strip())

c = "Hello"
print(c.replace("o","m"))

d = "1,2,3,4,5,6"
print(d.split(","))


a = "john"
b = "hello"
c = a+" "+b
print(c)

age = 27
result = "My Age is {2} my friend is {1} my boss is {0}"
print(result.format(27,28,30))


a = "hello \"how\" are you"
print(a)


a = "123 string"
print(a.isdigit())

b = "hello@"
print(b.capitalize())

print(b.count('l'))

print(b.isalnum())

print(b.islower())