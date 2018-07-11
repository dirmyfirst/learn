import time
start = time.clock()
fib =lambda n,x=0,y=1:x if not n else fib(n-1,y,x+y)
print (fib(20))
end = time.clock()
print ("read: %f s" % (end - start))
