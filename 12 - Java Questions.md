# Java Questions

## Abstract vs Interface

An interface is entirely virtual, where as an abstract method can have some shared code. Example: In you don’t have any common code between rectangle and circle then go with interface.


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
