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

## VPTR and Vtable

Tl;DR:
vtable: A table of function pointers. It is maintained per class.
vptr: A pointer to vtable. It is maintained per object (See this for an example).

To implement virtual functions, C++ uses a special form of late binding known as the virtual table or vTable. The virtual table is a lookup table of functions used to resolve function calls in a dynamic/late binding manner.

Every class that uses virtual functions (or is derived from a class that uses virtual functions) is given its own virtual table.

This table is simply a static array that the compiler creates at compile time. A virtual table contains one entry for each virtual function that can be called by objects of the class.

Each entry in this vTable is simply a Function Pointer that points to the most-derived function accessible by that class ie the most Base Class.

The compiler also adds a hidden pointer to the base class, which we will call vptr.

vPtr is set (automatically) when a class instance is created so that it points to the virtual table for that class. vptr is inherited by derived classes


## Pointers vs references
Pointers: A pointer is a variable that holds memory address of another variable. A pointer needs to be dereferenced with * operator to access the memory location it points to.  

References : A reference variable is an alias, that is, another name for an already existing variable. A reference, like a pointer is also implemented by storing the address of an object.  

A reference can be thought of as a constant pointer (not to be confused with a pointer to a constant value!) with automatic indirection, i.e the compiler will apply the * operator for you.  


Pointers can be reassigned, references cannot. Pointer arithmetic, pointer == null, etc.
