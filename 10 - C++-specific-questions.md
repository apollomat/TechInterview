# Python Interview Questions

## Copy Constructor
```java
class SampleClass{
  public:
  int* ptr;
  SampleClass();
  // Copy constructor declaration
  SampleClass(SampleClass &obj);
  };

  SampleClass::SampleClass(){
  ptr = new int();
  *ptr = 5;
  }

  // Copy constructor definition
  SampleClass::SampleClass(SampleClass &obj){
  //create a new object for the pointer
  ptr = new int();
  // Now manually assign the value
  *ptr = *(obj.ptr);
  cout<<"Copy constructor...\n";
  }
```

## What are virtual functions?
A virtual function a member function which is declared within base class and is re-defined (Overriden) by derived class.


Virtual functions are member functions of class which is declared using keyword 'virtual'.

When a base class type reference is initialized using object of sub class type and an overridden method which is declared as virtual is invoked using the base reference,
the method in child class object will get invoked.

## Pure virtual functions
A function is made as pure virtual function by the using a specific signature, " = 0"
appended to the function declaration as given below.

Purpose: It's to make the class abstract, so that it can't be instantiated, but a child class can override the pure virtual methods to form a concrete class. This is a good way to define an interface in C++.


## Public vs Private

Three access specifiers: private, protected or public (by default access to members of a class is private)


## Static

We can define class members static using static keyword. When we declare a member of a class as static it means no matter how many objects of the class are created, there is only one copy of the static member. A static member is shared by all objects of the class.

When you a declare a static variable at file scope, then that variable is only available in that particular file.

## Data type ranges
https://msdn.microsoft.com/en-us/library/s3f49ktz.aspx
Int: 4 bytes
Char: 1 byte
Double: 8 bytes
