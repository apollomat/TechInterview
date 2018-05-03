# Databases

## Different Types of SQL JOINs  

Here are the different types of the JOINs in SQL:  

(INNER) JOIN: Returns records that have matching values in both tables  

LEFT (OUTER) JOIN: Return all records from the left table, and the matched records from the right table  

RIGHT (OUTER) JOIN: Return all records from the right table, and the matched records from the left table  

FULL (OUTER) JOIN: Return all records when there is a match in either left or right table  


## Simple query:

Write an SQL query to find names of employee start with 'A'?  
 1
SELECT * FROM Employees WHERE EmpName like 'A%'


## ACID

ACID property is used to ensure that the data transactions are processed reliably in a database system.

A single logical operation of a data is called transaction.

ACID is an acronym for Atomicity, Consistency, Isolation, Durability.

Atomicity: it requires that each transaction is all or nothing. It means if one part of the transaction fails, the entire transaction fails and the database state is left unchanged.

Consistency: the consistency property ensure that the data must meet all validation rules. In simple words you can say that your transaction never leaves your database without completing its state.

Isolation: this property ensure that the concurrent property of execution should not be met. The main goal of providing isolation is concurrency control.

Durability: durability simply means that once a transaction has been committed, it will remain so, come what may even power loss, crashes or errors.



## NOSQL vs SQL

Reasons for SQL:
* Structured data
* Strict schema
* Relational data
* Need for complex joins
* Transactions
* Clear patterns for scaling
* More established: developers, community, code, tools, etc
* Lookups by index are very fast
Reasons for NoSQL:
* Semi-structured data
* Dynamic or flexible schema
* Non-relational data
* No need for complex joins
* Store many TB (or PB) of data
* Very data intensive workload
* Very high throughput for IOPS
Sample data well-suited for NoSQL:
* Rapid ingest of clickstream and log data
* Leaderboard or scoring data
* Temporary data, such as a shopping cart
* Frequently accessed ('hot') tables
* Metadata/lookup tables
