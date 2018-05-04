# Python Interview Questions

## Snippets

```python

# For alphabet
>>> 'A'.isdigit()
False
>>> 'A'.isalpha()
True

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict):
    print "%s: %s" % (key, mydict[key])

# CONVERT int to string

    s.append(chr(ord(‘0’) + x % 10) 			where x is int

#CONVERT STRING TO INT

elif ord(i) >= 48 and ord(i) <= 57 :
            number_started = True
            ans = (ans * 10) +  (ord(i) - ord('0'))


def letterCasePermutation(self, S):
  res = ['']
  for ch in S:
      if ch.isalpha():
          res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
      else:
          res = [i+ch for i in res]
  return res

```

## List Comprehension
```python

return [key for key, value in sequences.iteritems() if value > 1] #extract the relevant keys



```

## Interpreted language


Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.

## Dynamically Typed

Python is dynamically typed, this means that you don't need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error

## Shallow copy vs deep copying

-   Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Whereas, deep copy is used to store the values that are already copied.   

-   Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it.
- Deep copy doesn’t copy the reference pointers to the objects. Deep copy makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object.   

## Decorators
What are Python decorators and how would you use them?  

They extend past python, and are functions that take a function as an argument and return functions (e.g.  nodes). A simple example might be a decorator that takes a function, prints its args to stdout, prints the return value to stdout, then returns that return value. The syntax in Python is usually done with the @decorator_name above a function definition.  


## Lists vs Tuples
Tuples are immutable. A tuple might be a good type for a coordinate inst var in some class. Lists are ordered collections, but with a tuple, each index generally has a certain meaning, so coord[0] is the x coordinate and coord[1] is y.


## Range vs Xrange
Range returns a list of the full sequence while xrange generates each element iteratively like you would with the "yield" keyword. This changes in python3, and the default behavior is to yield like xrange. I think xrange is out.


## Special methods (str, gt, hash)

These are methods like str and gt, which override behavior of other global functions like str() and operators like >. enter and exit will be used with the with keyword, and there are many more like getattr. Overriding getattr can result in some very unpredictable behavior with a dynamic language like Python, and you should be very careful when you use magic like that.


## Python and multithreading

Python doesn't allow multi-threading in the truest sense of the word. It has a multi-threading package but if you want to multi-thread to speed your code up, then it's usually not a good idea to use it. Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your 'threads' can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core. All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package often isn't a good idea.  

There are reasons to use Python's threading package. If you want to run some things simultaneously, and efficiency is not a concern, then it's totally fine and convenient.
