# Java Questions

## Abstract vs Interface

An interface is entirely virtual, where as an abstract method can have some shared code. Example: In you don’t have any common code between rectangle and circle then go with interface.

interface: To implement a contract by multiple unrelated objects (car can be sold, so can a pencil)

abstract class: To implement the same or different behaviour among multiple related objects
(customer type -- gold, silver, platinum, make getName an abstract method)

## Final keyword

Variable: Value of Final variable is constant, you can not change it.  

Method: you can’t override a Final method.  

Class: you can’t inherit from Final class.  

## Super keyword

Used to refer to the parent class method or values

## StringBuffer vs String

String is an immutable class.   

Reassigning a string to another value will create a whole new copy of the string. This can be poor for larger strings. StringBuffer has better performance.  

## Throw vs Throws

Throws declares that a method might throw those types of exceptions. Throw is used to actually throw the exception

```java
public void someMethod(List<Foo> someList) throws SomeException {
    if (someList.isEmpty()) throw new SomeException();
}
```

## Finalize method

This method is thrown right before an object is freed. If you want to close a DB connection, use finalize.

## Static method

Variable is used for all of the classes and is class specific, not object specific.

## Volatile

Guarantees that all reads/writes of the variable will be read from main memory (and not a cache).


## Array vs ArrayList
 What is difference between Array and ArrayList ? When will you use Array over ArrayList ? The Array and ArrayList classes differ on the following features:

Arrays can contain primitive or objects, while an ArrayList can contain only objects.
Arrays have fixed size, while an ArrayList is dynamic.
An ArrayListprovides more methods and features, such as addAll, removeAll, iterator, etc.
For a list of primitive data types, the collections use autoboxing to reduce the coding effort. However, this approach makes them slower when working on fixed size primitive data types.
