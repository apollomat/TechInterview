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
Virtual functions are member functions of class which is declared using keyword 'virtual'.

When a base class type reference is initialized using object of sub class type and an overridden method which is declared as virtual is invoked using the base reference,
the method in child class object will get invoked.

## Pure virtual functions
A function is made as pure virtual function by the using a specific signature, " = 0"
appended to the function declaration as given below.
