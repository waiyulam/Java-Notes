
# Database 

- 一、 [基本概念 Basics ](#Basics)

- 二、 [事务 Transaction](#Transaction)
  * [概念 Definitions](#Definitions)
  * [ACID](#ACID)
  * [AUTOCOMMIT](#AUTOCOMMIT)

- 三、 [并发一致问题 Concurrency&Consistency](#Anomalies-with-Interleaved-Execution)
  * [丢失修改](#Overwriting-Uncommited-Data)
  * [读脏数据](#Dirty-Read)
  * [不可重复读](#Unrepeatable-Reads)
  * [幻影读](#幻影读)

- 四、 [封锁 Concurrency Control](#Concurrency-Control)
  * [可串行化调度 Serializability](#Conflict-Serializablity)
  * [封锁粒度 Granularity](#Granularity)
  * [封锁类型 Lock types](#Locks-Types)
  * [封锁协议 Concurrency Control Protocal](#Concurrency-Control-Protocal)
  * [MySQL 隐式与显示锁定](#MySQL-隐式与显示锁定)
  * [死锁 Deadlock](#Deadlock)

- 五、 [隔离级别 Transaction Isolation](#隔离级别)
  * [未提交读（READ UNCOMMITTED](#READ-UNCOMMITTED)
  * [提交读（READ COMMITTED）](#READ-COMMITTED)
  * [可重复读（REPEATABLE READ）](#REPEATABLE-READ)
  * [可串行化（SERIALIZABLE）](#SERIALIZABLE)

- 六、[多版本并发控制 Multi-Version Concurrency Control](#MVCC)
  * [基本思想](#基本思想)
  * [版本号](#版本号)
  * [Undo 日志](#Undo-日志)
  * [ReadView](#ReadView)
  * [快照读与当前读](#快照读与当前读)

- 七、[Next-Key Locks](#Next-Key-Locks)
  * [Record Locks](#Record-Locks)
  * [Gap Locks](#Gap-Locks)
  * [Next-Key Locks](#Next-Key-Locks)

- 八、[关系数据库设计理论 Relational model](#Relational-model)
  * [函数依赖](#函数依赖)
  * [异常](#异常)
  * [范式](#范式)

- 九、ER 图
  * 实体的三种联系
  * 表示出现多次的关系
  * 联系的多向性
  * 表示子类
  * 参考资料

- 十、[分布式数据库](#十分布式数据库)
  * [概念](#分布式概念)
  
# Basics

- 数据（data）：描述事物的符号记录称为数据。 Symbolic records describing things are called data.

- 数据库（DataBase，DB）：是长期存储在计算机内、有组织的、可共享的大量数据的集合，具有永久存储、有组织、可共享三个基本特点。 It is a collection of a large amount of organized, shareable data stored in a computer for a long time, and has three basic characteristics of permanent storage, organization, and shareability.

- 数据库管理系统（DataBase Management System，DBMS）：是位于用户与操作系统之间的一层数据管理软件。 a layer of data management software located between the user and the operating system.

- 数据库系统（DataBase System，DBS）：是有数据库、数据库管理系统（及其应用开发工具）、应用程序和数据库管理员（DataBase Administrator DBA）组成的存储、管理、处理和维护数据的系统。a system consisting of a database, a database management system (and its application development tools), applications, and a database administrator (DBA) to store, manage, process, and maintain data.

- 实体（entity）：客观存在并可相互区别的事物称为实体。Objects that exist objectively and can be distinguished from each other are called entities.

- 属性（attribute）：实体所具有的某一特性称为属性。An attribute of an entity is called an attribute.

- 码（key）：唯一标识实体的属性集称为码。The set of attributes that uniquely identify an entity is called a key.

- 实体型（entity type）：用实体名及其属性名集合来抽象和刻画同类实体，称为实体型。Use entity name and its attribute name set to abstract and characterize similar entities, called entity type.

- 实体集（entity set）：同一实体型的集合称为实体集。A set of the same entity type is called an entity set.

- 联系（relationship）：实体之间的联系通常是指不同实体集之间的联系。The relationship between entities usually refers to the connection between different sets of entities.

- 模式（schema）：模式也称逻辑模式，是数据库全体数据的逻辑结构和特征的描述，是所有用户的公共数据视图。A schema is also called a logical schema. It is a description of the logical structure and characteristics of the entire database data. It is a common data view for all users.

- 外模式（external schema）：外模式也称子模式（subschema）或用户模式，它是数据库用户（包括应用程序员和最终用户）能够看见和使用的局部数据的逻辑结构和特征的描述，是数据库用户的数据视图，是与某一应用有关的数据的逻辑表示。External schema is also called subschema or user schema. It is a description of the logical structure and characteristics of local data that database users (including application programmers and end users) can see and use. A database user's data view is a logical representation of data related to an application.

- 内模式（internal schema）：内模式也称为存储模式（storage schema），一个数据库只有一个内模式。他是数据物理结构和存储方式的描述，是数据库在数据库内部的组织方式。Internal schema is also called storage schema. A database has only one internal schema. It is a description of the physical structure and storage of the data, and the way the database is organized within the database.

# Transaction 

## Definitions
- A transaction is a single logical unit of work which accesses and possibly modifies the contents of a database. Transactions access data using read and write operations.

    Read(A): Read operations Read(A) or R(A) reads the value of A from the database and stores it in a buffer in main memory.

    Write (A): Write operation Write(A) or W(A) writes the value back to the database from buffer.

- 事务指的是满足 ACID 特性的一组操作，可以通过 Commit 提交一个事务，也可以使用 Rollback 进行回滚。

<p align="center">
<img width="500" height="400" src="https://camo.githubusercontent.com/5b729240000ac04e2c3e9d315e9b9716591496fe/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232323233373932352e706e67">
</p>

> Rollback: undo all the actions of an aborted transaction 

## ACID 
In order to maintain consistency in a database, before and after the transaction, certain properties are followed. These are called ACID properties.

### 1. 原子性 Atomicity : All or nothing rule’

- 事务被视为不可分割的最小单元，事务的所有操作**要么全部提交成功，要么全部失败回滚**。

  * Abort: If a transaction aborts, changes made to database are not visible.
  * Commit: If a transaction commits, changes made are visible.

<p align="center">
<img width="400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/11-6.jpg">
</p>

Consider the following transaction T consisting of T1 and T2: Transfer of 100 from account X to account Y.If the transaction fails after completion of T1 but before completion of T2.( say, after write(X) but before write(Y)), then amount has been deducted from X but not added to Y. This results in an inconsistent database state. Therefore, the transaction must be executed in entirety in order to ensure correctness of database state.

- 回滚可以用回滚日志（Undo Log）来实现，回滚日志记录着事务所执行的修改操作，在回滚时反向执行这些修改操作即可。

### 2. 一致性（Consistency）

- 事务必须使数据库从一个一致性状态变换到另外一个一致性状态。以转账为例子，A向B转账，假设转账之前这两个用户的钱加起来总共是2000，那么A向B转账之后，不管这两个账户怎么转，A用户的钱和B用户的钱加起来的总额还是2000，这个就是事务的一致性。

The total amount before and after the transaction must be maintained.

Total before T occurs = 500 + 200 = 700.  
Total after T occurs = 400 + 300 = 700.   

Therefore, database is consistent. **Inconsistency** occurs in case **T1 completes but T2 fails**. As a result T is incomplete.

### 3. 隔离性（Isolation）

- 隔离性是当多个用户并发访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务，不能被其他事务的操作所干扰，多个并发事务之间要相互隔离。

即要达到这么一种效果：对于任意两个并发的事务 T1 和 T2，在事务 T1 看来，T2 要么在 T1 开始之前就已经结束，要么在 T1 结束之后才开始，这样每个事务都感觉不到有其他事务在并发地执行。

- Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed

- This property ensures that multiple transactions can occur concurrently without leading to the inconsistency of database state.  

- This property ensures that **the execution of transactions concurrently will result in a state that is equivalent to a state achieved these were executed serially in some order.**

<p align="center">
<img width="400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/22-1.jpg">
</p>

Let X= 500, Y = 500. Consider two transactions T and T”. Suppose T has been
executed till Read (Y) and then T’’ starts. As a result , interleaving of
operations takes place due to which T’’ reads correct value of X but incorrect
value of Y and sum computed by 
    T’’: (X+Y = 50, 000+500=50, 500) is thus not
consistent with the sum at end of transaction: 
    T: (X+Y = 50, 000 + 450 = 50,450).

This results in database inconsistency, due to a loss of 50 units. Hence, transactions must take place in isolation and changes should be visible only after they have been made to the main memory.



### 4. 持久性（Durability）

- 一旦事务提交，则其所做的修改将会永远保存到数据库中。即使系统发生崩溃，事务执行的结果也不能丢失。

This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs. 

> 系统发生奔溃可以用重做日志（Redo Log）进行恢复，从而实现持久性。与回滚日志记录数据的逻辑修改不同，重做日志记录的是数据页的物理修改。

------------------------------------------

The ACID properties, in totality, provide a mechanism to ensure correctness and consistency of a database in a way such that each transaction is a group of operations that acts a single unit, produces consistent results, acts in isolation from other operations and updates that it makes are durably stored.

事务的 ACID 特性概念简单，但不是很好理解，主要是因为这几个特性不是一种平级关系：

- 只有满足一致性，事务的执行结果才是正确的。
- 在无并发的情况下，事务串行执行，隔离性一定能够满足。此时只要能满足原子性，就一定能满足一致性。
- 在并发的情况下，多个事务并行执行，事务不仅要满足原子性，还需要满足隔离性，才能满足一致性。
- 事务满足持久化是为了能应对系统崩溃的情况。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/05ba47a03214cd6a2d9a4c43989b0893bb99c5e0/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373231303433373032332e706e67">
</p>

## AUTOCOMMIT 

MySQL 默认采用自动提交模式。也就是说，如果不显式使用START TRANSACTION语句来开始一个事务，那么每个查询操作都会被当做一个事务并自动提交。

# Anomalies with Interleaved Execution

在并发环境下，事务的隔离性很难保证，因此会出现很多并发一致性问题。

## Overwriting Uncommited Data 

- 丢失修改指一个事务的更新操作被另外一个事务的更新操作替换。

一般在现实生活中常会遇到，例如：T1 和 T2 两个事务都对一个数据进行修改，T1 先修改并提交生效，T2 随后修改，T2 的修改覆盖了 T1 的修改。


<p align="center">
<img width="400" height="400" src="https://camo.githubusercontent.com/c673f3c3526d0242f50a085bc2b39c1aa80f9161/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232313734343234342e706e67">
</p>

## Dirty Read 

- Read uncommited data (WR conflicts)

读脏数据指在不同的事务下，当前事务可以读到另外事务未提交的数据。例如：T1 修改一个数据但未提交，T2 随后读取这个数据。**如果 T1 撤销了这次修改，那么 T2 读取的数据是脏数据。**

<p align="center">
<img width="400" height="400" src="https://camo.githubusercontent.com/b90038472b7b34cc8d78dc427490071c8dbc2da0/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232313932303336382e706e67">
</p>

- Examples: 

　　Mary 的原工资为 1000, 财务人员将 Mary 的工资改为了 8000 (但未提交事务)

　　Mary 读取自己的工资，发现自己的工资变为了 8000，欢天喜地！

　　而财务发现操作有误，回滚了事务，Mary 的工资又变为了1000

　　像这样，Mary记取的工资数8000是一个脏数据。

- Solution: 
　　把数据库的事务隔离级别调整到 READ_COMMITTED

## Unrepeatable Reads 

- RW Conflicts: the violation is that since every transaction is isolated then for every data such as A in T<sub>i</sub>, we should read same value 

不可重复读指在一个事务内多次读取同一数据集合。在这一事务还未结束前，另一事务也访问了该同一数据集合并做了修改，由于第二个事务的修改，第一次事务的两次读取的数据可能不一致。例如：T2 读取一个数据，T1 对该数据做了修改。如果 T2 再次读取这个数据，此时读取的结果和第一次读取的结果不同。

<p align="center">
<img width="400" height="400" src="https://camo.githubusercontent.com/45f4d155d56ee83b082f52800817497f1ddf4e9d/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232323130323031302e706e67">
</p>

- Examples: 
（1）在事务1中，Mary 读取了自己的工资为1000，操作并没有完成
```sql
con1 = getConnection();  
select salary from employee empId ="Mary"; 
```
（2）在事务2中，这时财务人员修改了 Mary 的工资为 2000，并提交了事务.
```sql
con2 = getConnection();  
update employee set salary = 2000;  
con2.commit();  
```
（3）在事务1中，Mary 再次读取自己的工资时，工资变为了2000
```sql
//con1  
select salary from employee empId ="Mary";  
```

- Solution : 

如果只有在修改事务完全提交之后才可以读取数据，则可以避免该问题。把数据库的事务隔离级别调整到REPEATABLE_READ

## 幻影读 Phantom read

幻读本质上也属于不可重复读的情况，T1 读取某个范围的数据，T2 在这个范围内插入新的数据，T1 再次读取这个范围的数据，此时读取的结果和和第一次读取的结果不同。　　
事务 T1 读取一条指定的 Where 子句所返回的结果集，然后 T2 事务新插入一行记录，这行记录恰好可以满足T1 所使用的查询条件。然后 T1 再次对表进行检索，但又看到了 T2 插入的数据。 （**和可重复读类似，但是事务 T2 的数据操作仅仅是插入和删除，不是修改数据，读取的记录数量前后不一致**）

- 幻读的重点在于新增或者删除 (数据条数变化)

<p align="center">
<img width="400" height="400" src="https://camo.githubusercontent.com/200903f2e9011d9b5d20f515c37ba784a88e843e/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232323133343330362e706e67">
</p>

- Examples:
目前工资为1000的员工有10人。 
(1）事务1，读取所有工资为 1000 的员工（共读取 10 条记录 ）
```sql
con1 = getConnection();  
Select * from employee where salary =1000; 
```
（2）这时另一个事务向 employee 表插入了一条员工记录，工资也为 1000
```sql
con1 = getConnection();  
con2 = getConnection();  
Insert into employee(empId,salary) values("Lili",1000);  
con2.commit(); 
```
(3) 事务1再次读取所有工资为 1000的 员工（共读取到了 11 条记录，这就像产生了幻读）
```sql
//con1  
select * from employee where salary =1000;
```

- Solutions: 
如果在操作事务完成数据处理之前，任何其他事务都不可以添加新数据，则可避免该问题。把数据库的事务隔离级别调整到 SERIALIZABLE_READ

产生并发不一致性问题的主要原因是**破坏了事务的隔离性**，解决方法是**通过并发控制来保证隔离性**。并发控制可以通过**封锁**来实现，但是**封锁操作需要用户自己控制**，相当复杂。数据库管理系统**提供了事务的隔离级别**，让用户以一种更轻松的方式处理并发一致性问题。

# Concurrency Control 

## Conflict Serializablity
可串行化调度是指，通过并发控制，使得并发执行的事务结果与某个串行执行的事务结果相同。串行执行的事务互不干扰，不会出现并发一致性问题。
### Conflict Serializable

A schedule is called conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.

### Examples
S1: R1(A), W1(A), R2(A), W2(A), R1(B), W1(B), R2(B), W2(B)
T1: R1(A), W1(A), R1(B), W1(B)
T2: R2(A), W2(A), R2(B), W2(B)

**Possible Serial Schedules are: T1->T2 or T2->T1**

1. Swapping non-conflicting operations R2(A) and R1(B) in S1, the schedule becomes
S11: R1(A), W1(A), R1(B), W2(A), R2(A), W1(B), R2(B), W2(B)
2. Similarly, swapping non-conflicting operations W2(A) and W1(B) in S11, the schedule becomes,
S12: R1(A), W1(A), R1(B), W1(B), R2(A), W2(A), R2(B), W2(B)

S12 is a serial schedule in which all operations of T1 are performed before starting any operation of T2. Since S has been transformed into a serial schedule S12 by swapping non-conflicting operations of S1, S1 is conflict serializable.

S2: R2(A), W2(A), R1(A), W1(A), R1(B), W1(B), R2(B), W2(B)
T1: R1(A), W1(A), R1(B), W1(B)
T2: R2(A), W2(A), R2(B), W2(B)

Swapping non-conflicting operations
S22: R2(A), W2(A), R2(B), W2(B), R1(B), W1(B), R1(A), W1(A)

In schedule S22, all operations of T2 are performed first, but operations of T1 are not in order (order should be R1(A), W1(A), R1(B), W1(B)). So S2 is not conflict serializable.

### Dependency Graph

- one node per transaction; edge from T<sub>i</sub> to T<sub>j</sub> if T<sub>j</sub> reads/writes an object last written by T<sub>i</sub>

- **Theorem**: Schedule is conflict serializable if and only if its dependency graph is acyclic 

```
Serializable schedule S1: R1(A), W1(A), R2(A), W2(A), R1(B), W1(B), R2(B), W2(B)
        A
T1   ------>  T2
        B
T1   ------>  T2

Not Serializable schedule S2: R2(A), W2(A), R1(A), W1(A), R1(B), W1(B), R2(B), W2(B)

        A
T1   <------  T2
        B
T1   ------>  T2
```

## Granularity

**Granularity**: It is the size of data item allowed to lock.

- MySQL 中提供了两种封锁粒度：行级锁以及表级锁。

- Tradeoffs: 

  * 应该尽量只锁定需要修改的那部分数据，而不是所有的资源。**锁定的数据量越少，发生锁争用的可能就越小，系统的并发程度就越高。**

  * 但是**加锁需要消耗资源**，锁的各种操作（**包括获取锁、释放锁、以及检查锁状态**）都会**增加系统开销**。因此**封锁粒度越小，系统开销就越大。**

在选择封锁粒度时，需要在锁开销和并发程度之间做一个权衡。

## Locks Types

### 读写锁 Read and Write Lock 

- 互斥锁（Exclusive），简写为 X 锁，又称写锁。

一个事务对数据对象 A 加了 X 锁，就可以对 A 进行读取和更新。加锁期间其它事务不能对 A 加任何锁。

- 共享锁（Shared），简写为 S 锁，又称读锁。

一个事务对数据对象 A 加了 S 锁，可以对 A 进行读取操作，但是不能进行更新操作。加锁期间其它事务能对 A 加 S 锁，但是不能加 X 锁。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/6f64048dae719a1f7dfbe6af0424350bdb0323dd/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373231333532333737372e706e67">
</p>


### 意向锁 Intention Lock

- 使用意向锁（Intention Locks）可以更容易地支持多粒度封锁。

在存在行级锁和表级锁的情况下，**事务 T 想要对表 A 加 X 锁，就需要先检测是否有其它事务对表 A 或者表 A 中的任意一行加了锁，那么就需要对表 A 的每一行都检测一次，这是非常耗时的。**

- 意向锁在原来的 X/S 锁之上引入了 IX/IS，IX/IS 都是表锁，用来表示一个事务想要在表中的某个数据行上加 X 锁或 S 锁。有以下两个规定：
  * 一个事务在获得某个数据行对象的 S 锁之前，必须先获得表的 IS 锁或者更强的锁；
  * 一个事务在获得某个数据行对象的 X 锁之前，必须先获得表的 IX 锁。

通过引入意向锁，**事务 T 想要对表 A 加 X 锁**，只需要先检测**是否有其它事务对表 A 加了 X/IX/S/IS 锁**，如果**加了就表示有其它事务正在使用这个表或者表中某一行的锁**，**因此事务 T 加 X 锁失败。**


<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/058a319235c3bc00d36b43741ee69bbd4c55018b/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373231343434323638372e706e67">
</p>

> 任意 IS/IX 锁之间都是兼容的，**因为它们只表示想要对表加锁，而不是真正加锁；**

> 这里兼容关系针对的是表级锁，而表级的 IX 锁和行级的 X 锁兼容，两个事务可以对两个数据行加 X 锁。（事务 T1 想要对数据行 R1 加 X 锁，事务 T2 想要对同一个表的数据行 R2 加 X 锁，两个事务都需要对该表加 IX 锁，但是 IX 锁是兼容的，并且 IX 锁与行级的 X 锁也是兼容的，因此两个事务都能加锁成功，对同一个表中的两个数据行做修改。）

## Concurrency Control Protocal

**Concurrency-control protocols**: allow concurrent schedules, but ensure that the schedules are conflict/view serializable, and are recoverable and maybe even cascadeless.

### 1. 三级封锁协议 Lock based protocol

#### 一级封锁协议

事务 T 要修改数据 A 时必须加 X 锁，直到 T 结束才释放锁。

可以**解决丢失修改问题**，因为不能同时有两个事务对同一个数据进行修改，那么事务的修改就不会被覆盖。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/e21a9a4ae5fe5a0aa402c3783d853f6b0c1c12bb/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232303434303435312e706e67">
</p>

#### 二级封锁协议

在一级的基础上，要求读取数据 A 时必须加 S 锁，**读取完马上释放 S 锁。**

可以**解决读脏数据问题**，因为如果一个事务在对数据 A 进行修改，根据 1 级封锁协议，会加 X 锁，那么就不能再加 S 锁了，也就是不会读入数据。


<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/263a88b7ab77811af98b76bf44eeaf060defd03b/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232303833313834332e706e67">
</p>

#### 三级封锁协议

在二级的基础上，要求读取数据 A 时必须加 S 锁，**直到事务结束了才能释放 S 锁。**

可以**解决不可重复读的问题**，因为读 A 时，其它事务不能对 A 加 X 锁，从而避免了在读的期间数据发生改变。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/958afc08e7f6d1db59ac5d7941dca7bb99e8d6ea/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232313331333831392e706e67">
</p>

#### Problem with Lock based protocal : Deadlock&Starvation 

> Consider the following schedule 

Transaction|S1|S2|S3|S4|S5|S6|S7|S8
----|-----|-----|-----|-----|-----|-----|-----|-----|
T1| lockX(B)| read(B)	| B=B*50 |write(B)| | | |lockX(A)
T2| | | | |lockS(A)|read(A)|lockS(B)| 

**Deadlock** : Consider the above execution phase. Now, T1 holds an Exclusive lock over B, and T2 holds a Shared lock over A. Consider Statement 7, T2 requests for lock on B, while in Statement 8 T1 requests lock on A. This as you may notice imposes a Deadlock as none can proceed with their execution.

**Starvation**: If concurrency control manager is badly designed. For example: A transaction may be waiting for an X-lock on an item, while a sequence of other transactions request and are granted an S-lock on the same item.

### 2. 两段锁协议 Two phase locking 

- Implementing the Simple Lock based protocol (or Binary Locking) has its own disadvantages. They does not guarantee Serializability. Schedules may **follow the preceding rules but a non-serializable schedule may result.**

- 事务遵循两段锁协议是保证可串行化调度的充分条件。例如以下操作满足两段锁协议，它是可串行化调度。

lock-x(A)...lock-s(B)...lock-s(C)...unlock(A)...unlock(C)...unlock(B)

- 但不是必要条件，例如以下操作不满足两段锁协议，但它还是可串行化调度。

lock-x(A)...unlock(A)...lock-s(B)...unlock(B)...lock-s(C)...unlock(C)

- **To guarantee serializablity**, we must follow some additional protocol concerning the positioning of locking and unlocking operations in every transaction. This is where the concept of Two Phase Locking(2-PL) comes in the picture, 2-PL ensures serializablity. Now, let’s dig deep!

- 加锁和解锁分为两个阶段进行

#### Growing Phase

New locks on data items may be acquired but none can be released.
#### Shrinking Phase

Existing locks may be released but no new locks can be acquired.

#### Examples
Transaction|S1|S2|S3|S4|S5|S6|S7|S8|S9|S10
----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
T1| LOCKS(A)||LOCKX(B)||UNLOCK(A)||UNLOCK(B)||||
T2| |LOCKS(A)||||LOCKX(C)||UNLOCK(A)|UNLCOK(C)

Transaction T1:
- Growing Phase is from steps 1-3.
- Shrinking Phase is from steps 5-7.
- Lock Point at 3

Transaction T2:
- Growing Phase is from steps 2-6.
- Shrinking Phase is from steps 8-9.
- Lock Point at 6

#### Lock point 
The Point at which the growing phase ends, i.e., when transaction takes the final lock it needs to carry on its work. 

#### Drawbacks 
- Cascading Rollback is possible under 2-PL.

<p align="center">
<img width = "400" height="400" src="https://www.geeksforgeeks.org/wp-content/uploads/12122.png">
</p>

- **级联回滚**: 是指数据库的一个事务的失败引起多个事务随之失败，都要各自回滚。

A **cascading rollback** occurs in database systems when a transaction (T1) causes a failure and a rollback must be performed. Other transactions dependent on T1's actions must also be rollbacked due to T1's failure, thus causing a cascading effect. That is, one transaction's failure causes many to fail.
Because of Dirty Read in T2 and T3 in lines 8 and 12 respectively, when T1 failed we have to rollback others also. Hence Cascading Rollbacks are possible in 2-PL.

- **”死锁“**： Deadlocks and Starvation is possible.

Schedule:   Lock-X1(A)   Lock-X2(B)  Lock-X1(B)  Lock-X2(A)
Drawing the precedence graph, you may detect the loop. So Deadlock is also possible in 2-PL.

Two-phase locking may also limit the amount of concurrency that occur in a schedule because a Transaction may not be able to release an item after it has used it.

#### Strict 2-PL

In addition to the lock being 2-Phase all Exclusive(X) Locks held by the transaction be released until after the Transaction Commits.

- Following Strict 2-PL ensures that our schedule is:
  **Recoverable**
  **Cascadeless(No dirty read)**

Hence it gives us freedom from Cascading Abort which was still there in Basic 2-PL and moreover guarantee Strict Schedules **but still Deadlocks are possible!**

## MySQL 隐式与显示锁定

MySQL 的 InnoDB 存储引擎采用两段锁协议，会根据隔离级别在需要的时候自动加锁，并且所有的锁都是在同一时刻被释放，这被称为隐式锁定。

InnoDB 也可以使用特定的语句进行显示锁定：

```sql
SELECT ... LOCK In SHARE MODE;
SELECT ... FOR UPDATE;
```

## Deadlock 

死锁（Deadlock） 所谓死锁：是指两个或两个以上的进程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程。由于资源占用是互斥的，当某个进程提出申请资源后，使得有关进程在无外力协助下，永远分配不到必需的资源而无法继续运行，这就产生了一种特殊现象死锁。

### Deadlock prevention 
1. 查询是否锁表
```sql
show OPEN TABLES where In_use > 0;
```
2. 查询进程（如果您有SUPER权限，您可以看到所有线程。否则，您只能看到您自己的线程）
```sql
show processlist
```
3. 杀死进程id（就是上面命令的id列）
```sql
kill id
```
如果系统资源充足，进程的资源请求都能够得到满足，死锁出现的可能性就很低，否则就会因争夺有限的资源而陷入死锁。其次，进程运行推进顺序与速度不同，也可能产生死锁。 产生死锁的四个必要条件：

- 互斥条件：一个资源每次只能被一个进程使用。

- 请求与保持条件：一个进程因请求资源而阻塞时，对已获得的资源保持不放。

- 不剥夺条件：进程已获得的资源，在末使用完之前，不能强行剥夺。

- 循环等待条件：若干进程之间形成一种头尾相接的循环等待资源关系。
虽然不能完全避免死锁，但可以使死锁的数量减至最少。将死锁减至最少可以增加事务的吞吐量并减少系统开销，因为只有很少的事务回滚，而回滚会取消事务执行的所有工作。由于死锁时回滚而由应用程序重新提交。

**下列方法有助于最大限度地降低死锁：**

按同一顺序访问对象

避免事务中的用户交互

保持事务简短并在一个批处理中

使用低隔离级别

使用绑定连接

# 隔离级别

## READ UNCOMMITTED

最低的隔离等级，允许其他事务看到没有提交的数据，会导致脏读。

- 该隔离级别的事务会读到其它未提交事务的数据，此现象也称之为 脏读 。
- 事务中的修改，即使没有提交，对其它事务也是可见的。
- 最后一步读取到了 mysql 终端 1 中未提交的事务（没有 commit 提交动作），即产生了 脏读 ，大部分业务场景都不允许脏读出现，但是此隔离级别下数据库的并发是最好的。(Trade off between concurrency & serializability)

## READ COMMITTED

被读取的数据可以被其他事务修改，这样可能导致不可重复读。也就是说，事务读取的时候获取读锁，但是在读完之后立即释放(不需要等事务结束)，而写锁则是事务提交之后才释放，释放读锁之后，就可能被其他事务修改数据。该等级也是 SQL Server 默认的隔离等级。

- 一个事务只能读取已经提交的事务所做的修改。换句话说，一个事务所做的修改在提交之前对其它事务是不可见的。
- 一个事务可以读取另一个已提交的事务，多次读取会造成不一样的结果，此现象称为不可重复读问题，Oracle 和 SQL Server 的默认隔离级别。

## REPEATABLE READ

所有被 Select 获取的数据都不能被修改，这样就可以避免一个事务前后读取数据不一致的情况。但是却没有办法控制幻读，因为这个时候其他事务不能更改所选的数据，但是可以增加数据，即前一个事务有读锁但是没有范围锁，为什么叫做可重复读等级呢？那是因为该等级解决了下面的不可重复读问题。

- 保证在同一个事务中多次读取同一数据的结果是一样的。

- 该隔离级别是 MySQL 默认的隔离级别，在同一个事务里， select 的结果是事务开始时时间点的状态，因此，同样的 select 操作读到的结果会是一致的，但是，会有 幻读 现象。MySQL 的 InnoDB 引擎可以通过 next-key locks 机制（参考下文 行锁的算法 一节）来避免幻读。

> 引申：现在主流数据库都使用 MVCC 并发控制，使用之后RR（可重复读）隔离级别下是不会出现幻读的现象。

## SERIALIZABLE

所有事务一个接着一个的执行，这样可以避免幻读 (phantom read)，对于基于锁来实现并发控制的数据库来说，串行化要求在执行范围查询的时候，需要获取范围锁，如果不是基于锁实现并发控制的数据库，则检查到有违反串行操作的事务时，需回滚该事务。

- 强制事务串行执行，这样多个事务互不干扰，不会出现并发一致性问题。

- 在该隔离级别下事务都是串行顺序执行的，MySQL 数据库的 InnoDB 引擎会给读操作隐式加一把读共享锁，从而避免了脏读、不可重读复读和幻读问题。

该隔离级别需要加锁实现，因为要使用加锁机制保证同一时间只有一个事务执行，也就是保证事务串行执行。 串行化是4种事务隔离级别中隔离效果最好的，解决了脏读、可重复读、幻读的问题，但是效果最差，它将事务的执行变为顺序执行，与其他三个隔离级别相比，它就相当于单线程，后一个事务的执行必须等待前一个事务结束。



<p align="center">
<img width="500" height="400" src="https://camo.githubusercontent.com/68344d74dd0563e4c38dfed11c713f84f71a00cc/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230373232333430303738372e706e67">
</p>

隔离级别|	脏读|	不可重复读|	幻读
-----|-----|-----|-----|
读未提交|	可以出现|	可以出现|	可以出现
读提交|	不允许出现|	可以出现|	可以出现
可重复读|	不允许出现|	不允许出现|	可以出现|
序列化|	不允许出现|	不允许出现|	不允许出现|

> 从上往下，隔离强度逐渐增强，性能逐渐变差。采用哪种隔离级别要根据系统需求权衡决定，其中，可重复读是 MySQL 的默认级别。

> 只有串行化的隔离级别解决了全部这 3 个问题，其他的 3 个隔离级别都有缺陷。


# MVCC

多版本并发控制（Multi-Version Concurrency Control, MVCC）是 MySQL 的 InnoDB 存储引擎实现隔离级别的一种具体方式，
- 用于**实现提交读和可重复读这两种隔离级别**。
- 而未提交读隔离级别总是读取最新的数据行，要求很低，无需使用 MVCC。
- **可串行化隔离级别需要对所有读取的行都加锁，单纯使用 MVCC 无法实现。**

## 基本思想
在封锁一节中提到，加锁能解决多个事务同时执行时出现的并发一致性问题。在实际场景中读操作往往多于写操作，因此又引入了读写锁来避免不必要的加锁操作，例如读和读没有互斥关系。读写锁中读和写操作仍然是互斥的，而 MVCC 利用了多版本的思想，写操作更新最新的版本快照，而读操作去读旧版本快照，没有互斥关系，这一点和 CopyOnWrite 类似。

- 在 MVCC 中事务的修改操作 **DELETE、INSERT、UPDATE）会为数据行新增一个版本快照**
- 脏读和不可重复读最根本的原因是事务**读取到其它事务未提交的修改**。在事务进行读取操作时，为了解决脏读和不可重复读问题，**MVCC 规定只能读取已经提交的快照。当然一个事务可以读取自身未提交的快照，这不算是脏读**


## 版本号

- 系统版本号 SYS_ID：是一个递增的数字，每开始一个新的事务，系统版本号就会自动递增。
- 事务版本号 TRX_ID ：事务开始时的系统版本号。

## Undo 日志

MVCC 的多版本指的是多个版本的快照，快照存储在 Undo 日志中，该日志通过回滚指针 ROLL_PTR 把一个数据行的所有快照连接起来。

例如在 MySQL 创建一个表 t，包含主键 id 和一个字段 x。我们先插入一个数据行，然后对该数据行执行两次更新操作。

```sql
INSERT INTO t(id, x) VALUES(1, "a");
UPDATE t SET x="b" WHERE id=1;
UPDATE t SET x="c" WHERE id=1;
```

因为没有使用 START TRANSACTION 将上面的操作当成一个事务来执行，根据 MySQL 的 AUTOCOMMIT 机制，每个操作都会被当成一个事务来执行，所以上面的操作总共涉及到三个事务。快照中除了记录事务版本号 TRX_ID 和操作之外，还记录了一个 bit 的 DEL 字段，用于标记是否被删除。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/09832513cf5a63e15816143a204052677c46fc0c/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230383136343830383231372e706e67">
</p>

INSERT、UPDATE、DELETE 操作会创建一个日志，并将事务版本号 TRX_ID 写入。DELETE 可以看成是一个特殊的 UPDATE，还会额外将 DEL 字段设置为 1。

## ReadView

MVCC 维护了一个 ReadView 结构，主要包含了当前系统未提交的事务列表 TRX_IDs {TRX_ID_1, TRX_ID_2, ...}，还有该列表的最小值 TRX_ID_MIN 和 TRX_ID_MAX。

<p align="center">
<img width="500" height="300" src="https://camo.githubusercontent.com/4d58315fa3b98e4b09cc51b9debaf9ce27b1c312/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f696d6167652d32303139313230383137313434353637342e706e67">
</p>

在进行 SELECT 操作时，根据数据行快照的 TRX_ID 与 TRX_ID_MIN 和 TRX_ID_MAX 之间的关系，从而判断数据行快照是否可以使用：

- TRX_ID < TRX_ID_MIN，表示该数据行快照时在当前所有未提交事务之前进行更改的，因此可以使用。

- TRX_ID > TRX_ID_MAX，表示该数据行快照是在事务启动之后被更改的，因此不可使用。

- TRX_ID_MIN <= TRX_ID <= TRX_ID_MAX，需要根据隔离级别再进行判断：

    * 提交读：如果 TRX_ID 在 TRX_IDs 列表中，表示该数据行快照对应的事务还未提交，则该快照不可使用。否则表示已经提交，可以使用。
    * 可重复读：都不可以使用。因为如果可以使用的话，那么其它事务也可以读到这个数据行快照并进行修改，那么当前事务再去读这个数据行得到的值就会发生改变，也就是出现了不可重复读问题。

在数据行快照不可使用的情况下，需要沿着 Undo Log 的回滚指针 ROLL_PTR 找到下一个快照，再进行上面的判断。

## 快照读与当前读

### 1. 快照读

MVCC 的 SELECT 操作是快照中的数据，不需要进行加锁操作。

```sql
SELECT * FROM table ...;
```

### 2. 当前读

MVCC 其它会对数据库进行修改的操作（INSERT、UPDATE、DELETE）需要进行加锁操作，从而读取最新的数据。可以看到 MVCC 并不是完全不用加锁，而只是避免了 SELECT 的加锁操作。

```sql
INSERT;
UPDATE;
DELETE;
```

在进行 SELECT 操作时，可以强制指定进行加锁操作。以下第一个语句需要加 S 锁，第二个需要加 X 锁。

```sql
SELECT * FROM table WHERE ? lock in share mode;
SELECT * FROM table WHERE ? for update;
```

# Next-Key Locks

Next-Key Locks 是 MySQL 的 InnoDB 存储引擎的一种锁实现。

MVCC 不能解决幻影读问题，Next-Key Locks 就是为了解决这个问题而存在的。在可重复读（REPEATABLE READ）隔离级别下，使用 MVCC + Next-Key Locks 可以解决幻读问题。

## Record Locks
锁定一个记录上的索引，而不是记录本身。


如果表没有设置
