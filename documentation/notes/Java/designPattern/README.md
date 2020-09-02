<!-- TOC -->

- [一、概述](#一概述)
    ​    - [设计模式怎么分类，每一类都有哪些？【蚂蚁金服内推】](#设计模式怎么分类每一类都有哪些蚂蚁金服内推)
    ​    - [设计模式怎么用到项目中？【阿里面经】](#设计模式怎么用到项目中阿里面经)
- [二、设计模式](#二设计模式)
    - [单例模式](#单例模式)
    - [工厂模式](#工厂模式)
    - [观察者模式](#观察者模式)
    - [适配器模式（Adapter）](#适配器模式adapter)
        - [意图](#意图)
        - [类型](#类型)
        - [类图](#类图)
        - [实现](#实现)
        - [JDK](#jdk)
    - [模仿方法模式](#模仿方法模式)
    - [策略模式（Strategy）](#策略模式strategy)
        - [意图](#意图-1)
        - [类图](#类图-1)
        - [与状态模式的比较](#与状态模式的比较)
        - [实现](#实现-1)
        - [JDK](#jdk-1)
            - [](#)
    - [责任链模式](#责任链模式)
    - [装饰者模式](#装饰者模式)
    - [迭代器模式（Iterator）](#迭代器模式iterator)
        ​    ​    - [所了解的设计模式，单例模式的注意事项，jdk源码哪些用到了你说的设计模式](#所了解的设计模式单例模式的注意事项jdk源码哪些用到了你说的设计模式)
- [三、设计模式常见问题](#三设计模式常见问题)
- [附录：参考资料](#附录参考资料)

<!-- /TOC -->
[Interview-Notebook/设计模式](https://github.com/CyC2018/Interview-Notebook/blob/master/notes/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.md)


# 一、概述

1、设计模式是人们在面对同类型软件工程设计问题所总结出的一些有用经验。模式不是代码，而是某类问题的通用设计解决方案

2、4人组Erich Gamma、Richard Helm、Ralph Johnson、John Vlissides总结写了《设计模式》

3、设计模式的优点和用途

4、学习设计模式最好的方式：在你的设计和以往的工程里寻找何处可以使用它们

5、设计模式的本质目的是使软件工程在维护性、扩展性、变化性、复杂度方面成O(N)

6、OO（Object Oriented）是原则，设计模式是具体方法、工具



万物皆对象
面向对象三大特性：封装、集成、多态
面向对象设计原则：开口合里最单依
重构原则：事不过三、三则重构
写且只写一次



### 设计模式怎么分类，每一类都有哪些？【蚂蚁金服内推】







### 设计模式怎么用到项目中？【阿里面经】








# 二、设计模式

## 单例模式

### Intent 
确保一个**类只有一个实例**，并提供该实例的**全局访问点**。

### Class diagram 
使用一个私有构造函数、一个私有静态变量以及一个公有静态函数来实现。

私有构造函数保证了不能通过构造函数来创建对象实例，只能通过公有静态函数返回唯一的私有静态变量。

<p>
<img width="400" height="400" src="https://camo.githubusercontent.com/8d7dcb581c89f61e908d7a6546760ec6bf0a0e7c/68747470733a2f2f63732d6e6f7465732d313235363130393739362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f65636131663432322d383338312d343039622d616430342d3938656633396165333862612e706e67">
</p>

### Implementation 
#### 懒汉式-线程不安全

- 以下实现中，私有静态变量 uniqueInstance 被延迟实例化，这样做的好处是，如果没有用到该类，那么就不会实例化 uniqueInstance，从而节约资源。

- **线程不安全**： 这个实现在多线程环境下是不安全的，如果多个线程能够同时进入 if (uniqueInstance == null) ，并且此时 uniqueInstance 为 null，那么会有多个线程执行 uniqueInstance = new Singleton(); 语句，这将导致实例化多次 uniqueInstance。

```java
public class Singleton {

    private static Singleton uniqueInstance;

    private Singleton() {
    }

    public static Singleton getUniqueInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }
}
```

#### 饿汉式-线程安全

线程不安全问题主要是由于 uniqueInstance 被实例化多次，采取直接实例化 uniqueInstance 的方式就不会产生线程不安全问题。

但是直接实例化的方式也丢失了延迟实例化带来的节约资源的好处。

```java
private static Singleton uniqueInstance = new Singleton();
```

#### 懒汉式-线程安全
只需要对 getUniqueInstance() 方法加锁，那么在一个时间点只能有一个线程能够进入该方法，从而避免了实例化多次 uniqueInstance。

但是当一个线程进入该方法之后，其它试图进入该方法的线程都必须等待，即使 uniqueInstance 已经被实例化了。这会让线程阻塞时间过长，因此该方法有性能问题，不推荐使用。
```java
public static synchronized Singleton getUniqueInstance() {
    if (uniqueInstance == null) {
        uniqueInstance = new Singleton();
    }
    return uniqueInstance;
}
```
#### 双重校验锁-线程安全
uniqueInstance 只需要被实例化一次，之后就可以直接使用了。加锁操作只需要对实例化那部分的代码进行，只有当 uniqueInstance 没有被实例化时，才需要进行加锁。

双重校验锁先判断 uniqueInstance 是否已经被实例化，如果没有被实例化，那么才对实例化语句进行加锁。

```java
public class Singleton {

    private volatile static Singleton uniqueInstance;

    private Singleton() {
    }

    public static Singleton getUniqueInstance() {
        if (uniqueInstance == null) {
            synchronized (Singleton.class) {
                if (uniqueInstance == null) {
                    uniqueInstance = new Singleton();
                }
            }
        }
        return uniqueInstance;
    }
}
```

- 考虑下面的实现，也就是只使用了一个 if 语句。在 uniqueInstance == null 的情况下，如果两个线程都执行了 if 语句，那么两个线程都会进入 if 语句块内。虽然在 if 语句块内有加锁操作，但是两个线程都会执行 uniqueInstance = new Singleton(); 这条语句，只是先后的问题，那么就会进行两次实例化。因此必须使用双重校验锁，也就是需要使用两个 if 语句：第一个 if 语句用来避免 uniqueInstance 已经被实例化之后的加锁操作，而第二个 if 语句进行了加锁，所以只能有一个线程进入，就不会出现 uniqueInstance == null 时两个线程同时进行实例化操作。

```java
if (uniqueInstance == null) {
    synchronized (Singleton.class) {
        uniqueInstance = new Singleton();
    }
}
```
- uniqueInstance 采用 volatile 关键字修饰也是很有必要的， uniqueInstance = new Singleton(); 这段代码其实是分为三步执行：

1. 为 uniqueInstance 分配内存空间
2. 初始化 uniqueInstance
3. 将 uniqueInstance 指向分配的内存地址

但是由于 JVM 具有指令重排的特性，执行顺序有可能变成 1>3>2。指令重排在单线程环境下不会出现问题，但是在多线程环境下会导致一个线程获得还没有初始化的实例。例如，线程 T1 执行了 1 和 3，此时 T2 调用 getUniqueInstance() 后发现 uniqueInstance 不为空，因此返回 uniqueInstance，但此时 uniqueInstance 还未被初始化。

- 使用 volatile 可以禁止 JVM 的指令重排，保证在多线程环境下也能正常运行。

#### 静态内部类实现
当 Singleton 类被加载时，静态内部类 SingletonHolder 没有被加载进内存。只有当调用 getUniqueInstance() 方法从而触发 SingletonHolder.INSTANCE 时 SingletonHolder 才会被加载，此时初始化 INSTANCE 实例，并且 JVM 能确保 INSTANCE 只被实例化一次。

这种方式不仅具有延迟初始化的好处，而且由 JVM 提供了对线程安全(final 不可变常量）的支持。

```java
public class Singleton {

    private Singleton() {
    }

    private static class SingletonHolder {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getUniqueInstance() {
        return SingletonHolder.INSTANCE;
    }
}
```



## 工厂模式

### 简单工厂
#### Intent 
在创建一个对象时不向客户暴露内部细节，并提供一个创建对象的通用接口。

#### Class diagram 
简单工厂把实例化的操作单独放到一个类中，这个类就成为简单工厂类，让简单工厂类来决定应该用哪个具体子类来实例化。

这样做能把客户类和具体子类的实现解耦，客户类不再需要知道有哪些子类以及应当实例化哪个子类。客户类往往有多个，如果不使用简单工厂，那么所有的客户类都要知道所有子类的细节。而且一旦子类发生改变，例如增加子类，那么所有的客户类都要进行修改。

### 工厂方法
#### Intent 
定义了一个创建对象的接口，但由子类决定要实例化哪个类。工厂方法把实例化操作推迟到子类。

#### Class diagram 
在简单工厂中，创建对象的是另一个类，而在工厂方法中，是由子类来创建对象。


### 抽象工厂

#### Intent 
提供一个接口，用于创建 相关的对象家族 。

#### Class diagram 
抽象工厂模式用到了工厂方法模式来创建单一对象，AbstractFactory 中的 createProductA() 和 createProductB() 方法都是让子类来实现，这两个方法单独来看就是在创建一个对象，这符合工厂方法模式的定义。

从高层次来看，抽象工厂使用了组合，即 Cilent 组合了 AbstractFactory，而工厂方法模式使用了继承。


## 观察者模式 

## 适配器模式（Adapter）

### 意图

把一个类接口转换成另一个用户需要的接口。适配器模式让那些接口不兼容的类可以一起工作 



[![img](https://github.com/CyC2018/Interview-Notebook/raw/master/pics/3d5b828e-5c4d-48d8-a440-281e4a8e1c92.png)](https://github.com/CyC2018/Interview-Notebook/blob/master/pics/3d5b828e-5c4d-48d8-a440-281e4a8e1c92.png)



### 类型

适配器模式的别名为包装器(Wrapper)模式，它既可以作为**类结构型模式**，也可以作为**对象结构型模式**。在适配器模式定义中所提及的接口是指广义的接口，它可以表示一个方法或者方法的集合。 

- 对象适配器：（传入对象）组合方式，但是更灵活推荐使用这种方式
- 类适配器：（多重继承）继承方式，效率更高



### 类图

[![img](https://github.com/CyC2018/Interview-Notebook/raw/master/pics/0f754c1d-b5cb-48cd-90e0-4a86034290a1.png)](https://github.com/CyC2018/Interview-Notebook/blob/master/pics/0f754c1d-b5cb-48cd-90e0-4a86034290a1.png)

 

### 实现

鸭子（Duck）和火鸡（Turkey）拥有不同的叫声，Duck 的叫声调用 quack() 方法，而 Turkey 调用 gobble() 方法。

要求将 Turkey 的 gobble() 方法适配成 Duck 的 quack() 方法，从而让火鸡冒充鸭子！

```java
public interface Duck {
    void quack();
}
```

```java
public interface Turkey {
    void gobble();
}
```

```java
public class WildTurkey implements Turkey {
    @Override
    public void gobble() {
        System.out.println("gobble!");
    }
}
```

```java
public class TurkeyAdapter implements Duck {
    Turkey turkey;

    public TurkeyAdapter(Turkey turkey) {
        this.turkey = turkey;
    }

    @Override
    public void quack() {
        turkey.gobble();
    }
}
```

```java
public class Client {
    public static void main(String[] args) {
        Turkey turkey = new WildTurkey();
        Duck duck = new TurkeyAdapter(turkey);
        duck.quack();
    }
}
```

### JDK

- [java.util.Arrays#asList()](http://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#asList%28T...%29)
- [java.util.Collections#list()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#list-java.util.Enumeration-)
- [java.util.Collections#enumeration()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#enumeration-java.util.Collection-)
- [javax.xml.bind.annotation.adapters.XMLAdapter](http://docs.oracle.com/javase/8/docs/api/javax/xml/bind/annotation/adapters/XmlAdapter.html#marshal-BoundType-)





## 模仿方法模式







## 策略模式（Strategy）

2018/7/11

### 意图

- 定义一系列算法，封装每个算法，并使它们可以互换。
- 策略模式可以让算法独立于使用它的客户端。

### 类图

- Strategy 接口定义了一个算法族，它们都具有 behavior() 方法。
- Context 是使用到该算法族的类，其中的 doSomething() 方法会调用 behavior()，setStrategy(in Strategy) 方法可以动态地改变 strategy 对象，也就是说能动态地改变 Context 所使用的算法。

[![img](https://github.com/CyC2018/Interview-Notebook/raw/master/pics/1fc969e4-0e7c-441b-b53c-01950d2f2be5.png)](https://github.com/CyC2018/Interview-Notebook/blob/master/pics/1fc969e4-0e7c-441b-b53c-01950d2f2be5.png)

### 与状态模式的比较

状态模式的类图和策略模式类似，并且都是能够动态改变对象的行为。

但是状态模式是通过状态转移来改变 Context 所组合的 State 对象，而策略模式是通过 Context 本身的决策来改变组合的 Strategy 对象。

所谓的状态转移，是指 Context 在运行过程中由于一些条件发生改变而使得 State 对象发生改变，注意必须要是在运行过程中。

状态模式主要是用来解决状态转移的问题，当状态发生转移了，那么 Context 对象就会改变它的行为；而策略模式主要是用来封装一组可以互相替代的算法族，并且可以根据需要动态地去替换 Context 使用的算法。

### 实现

设计一个鸭子，它可以动态地改变叫声。这里的算法族是鸭子的叫声行为。

```java
public interface QuackBehavior {
    void quack();
}
```

```java
public class Quack implements QuackBehavior {
    @Override
    public void quack() {
        System.out.println("quack!");
    }
}
```

```java
public class Squeak implements QuackBehavior{
    @Override
    public void quack() {
        System.out.println("squeak!");
    }
}
```

```java
public class Duck {
    private QuackBehavior quackBehavior;

    public void performQuack() {
        if (quackBehavior != null) {
            quackBehavior.quack();
        }
    }

    public void setQuackBehavior(QuackBehavior quackBehavior) {
        this.quackBehavior = quackBehavior;
    }
}
```

```java
public class Client {
    public static void main(String[] args) {
        Duck duck = new Duck();
        duck.setQuackBehavior(new Squeak());
        duck.performQuack();
        duck.setQuackBehavior(new Quack());
        duck.performQuack();
    }
}
```

```
squeak!
quack!
```

### JDK

- java.util.Comparator#compare()
- javax.servlet.http.HttpServlet
- javax.servlet.Filter#doFilter()



#### 



## 责任链模式







## 装饰者模式





## 迭代器模式（Iterator）

2018/7/16







- 反应器模式

 

1. 常用的八种掌握就行，原理，使用
2. 单例、工厂、观察者重点





##### 所了解的设计模式，单例模式的注意事项，jdk源码哪些用到了你说的设计模式 

- 所了解的设计模式 
  - 工厂模式：定义一个用于创建对象的接口，让子类决定实例化哪一个类， Factory Method 使一个类的实例化延迟到了子类。 
  - 单例模式：保证一个类只有一个实例，并提供一个访问它的全局访问点； 
  - 适配器模式：将一类的接口转换成客户希望的另外一个接口，Adapter 模式使得原本由于接口不兼容而不能一起工作那些类可以一起工作。 
  - 装饰者模式：动态地给一个对象增加一些额外的职责，就增加的功能来说， Decorator 模式相比生成子类更加灵活。 
  - 代理：为其他对象提供一种代理以控制对这个对象的访问 
  - 迭代器模式：提供一个方法顺序访问一个聚合对象的各个元素，而又不需要暴露该对象的内部表示。 
- 单例模式的注意事项 
  - 尽量使用懒加载 
  - 双重检索实现线程安全 
  - 构造方法为private 
  - 定义静态的Singleton instance对象和getInstance()方法 
- jdk源码中用到的设计模式 
  - 装饰器模式：IO流中 
  - 迭代器模式：Iterator 
  - 单利模式： java.lang.Runtime 
  - 代理模式：RMI 



# 三、设计模式常见问题





1.什么是高内聚，低耦合？





一个类只做一件事

一个方法只做一件事

写仅只写一次





# 附录：参考资料



卡奴达摩的专栏 - CSDN博客
https://blog.csdn.net/zhengzhb/article/category/926691/1



单例模式 - 23种设计模式 - 极客学院Wiki
http://wiki.jikexueyuan.com/project/java-design-pattern/singleton-pattern.html





https://www.bilibili.com/video/av18569541/



hexter 录制的课程 - 极客学院【23种设计模式】
http://my.jikexueyuan.com/hexter/record/



设计模式之禅

