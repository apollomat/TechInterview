# Python Interview Questions

## Shallow copy vs deep copying

-   Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Whereas, deep copy is used to store the values that are already copied.   

-   Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it.
- Deep copy doesn’t copy the reference pointers to the objects. Deep copy makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object.   

## Decorators
What are Python decorators and how would you use them?  

They extend past python, and are functions that take a function as an argument and return functions (e.g.  nodes). A simple example might be a decorator that takes a function, prints its args to stdout, prints the return value to stdout, then returns that return value. The syntax in Python is usually done with the @decorator_name above a function definition.  


## Lists vs Tuples
Do you know what is the difference between lists and tuples? Can you give me an example for their usage?
Tuples are immutable. A tuple might be a good type for a coordinate inst var in some class. Lists are ordered collections, but with a tuple, each index generally has a certain meaning, so coord[0] is the x coordinate and coord[1] is y.


## Range vs Xrange
Do you know the difference between range and xrange?
Range returns a list of the full sequence while xrange generates each element iteratively like you would with the "yield" keyword. This changes in python3, and the default behavior is to yield like xrange. I think xrange is out.


## Special methods

What are "special" methods (<foo>), how they work, etc
These are methods like str and gt, which override behavior of other global functions like str() and operators like >. enter and exit will be used with the with keyword, and there are many more like getattr. Overriding getattr can result in some very unpredictable behavior with a dynamic language like Python, and you should be very careful when you use magic like that.
