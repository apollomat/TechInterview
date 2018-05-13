# Javascript

## Closures

Closures: http://javascriptissexy.com/understand-javascript-closures-with-ease/  


Inner function has access to everything in the outer function and any global variables

```JavaScript
function showName (firstName, lastName) { 
		var nameIntro = "Your name is ";
	 	// this inner function has access to the outer function's variables, including the parameter​
		function makeFullName () { 
			return nameIntro + firstName + " " + lastName;
		 }

		return makeFullName (); 
	}


  // This example is explained in detail below (just after this code box).​
	​function celebrityIDCreator (theCelebrities) {
	    var i;
	    var uniqueID = 100;
	    for (i = 0; i < theCelebrities.length; i++) {
	      theCelebrities[i]["id"] = function ()  {
	        return uniqueID + i;
	      }
	    }

	    return theCelebrities;
	}

	var actionCelebs = [{name:"Stallone", id:0}, {name:"Cruise", id:0}, {name:"Willis", id:0}];

	var createIdForActionCelebs = celebrityIDCreator (actionCelebs);
  var stalloneID = createIdForActionCelebs [0]; console.log(stalloneID.id()); // 103

```


In the preceding example, by the time the anonymous functions are called, the value of i is 3 (the length of the array and then it increments). The number 3 was added to the uniqueID to create 103 for ALL the celebritiesID. So every position in the returned array get id = 103, instead of the intended 100, 101, 102.  



When a function accesses a variable outside its scope, it accesses that variable, not a frozen copy. So when the value held by the variable changes, the function gets that new value. By the time the user starts pressing buttons, our loop will have already completed and btnNum will be 3, so this is what each of our anonymous functions will get for num!  


The reason this happened was because, as we have discussed in the previous example, the closure (the anonymous function in this example) has access to the outer function’s variables by reference, not by value. So just as the previous example showed that we can access the updated variable with the closure, this example similarly accessed the i variable when it was changed, since the outer function runs the entire for loop and returns the last value of i, which is 103.  

To fix:

To fix this side effect (bug) in closures, you can use an Immediately Invoked Function Expression (IIFE), such as the following:

```JavaScript
function celebrityIDCreator (theCelebrities) {
    var i;
    var uniqueID = 100;
    for (i = 0; i < theCelebrities.length; i++) {
        theCelebrities[i]["id"] = function (j)  { // the j parametric variable is the i passed in on invocation of this IIFE​
            return function () {
                return uniqueID + j; // each iteration of the for loop passes the current value of i into this IIFE and it saves the correct value to the array​
            } () // BY adding () at the end of this function, we are executing it immediately and returning just the value of uniqueID + j, instead of returning a function.​
        } (i); // immediately invoke the function passing the i variable as a parameter​
    }
​
    return theCelebrities;
}
​
​var actionCelebs = [{name:"Stallone", id:0}, {name:"Cruise", id:0}, {name:"Willis", id:0}];
​
​var createIdForActionCelebs = celebrityIDCreator (actionCelebs);
​
​var stalloneID = createIdForActionCelebs [0];
 console.log(stalloneID.id); // 100​
​
​var cruiseID = createIdForActionCelebs [1]; console.log(cruiseID.id); // 101
```
