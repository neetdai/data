# 跳跃链表

## 参考网址
* [浅析SkipList跳跃表原理及代码实现](http://blog.csdn.net/ict2014/article/details/17394259)

跳跃链表比起一般的链表来说,优势在于查询速度较快,以内存的空间换取查询的时间.

因为跳跃链表是跨了节点去查询的,链表的查询时间是根据目标节点所在的位置与链表的头部相隔多少个节点

---

### 初始化
我们先建立SkipList的节点

```python
    class Node (object):

        def __init__ (self,key,value):
            self.key = key
            self.value = value
            self.level = []
```

然后再建立SkipList

```python
    class SkipList (object):

        __slot__ = ["__maxLevel","__head","__tail","__rand"]

        def __init__ (self,maxLevel = 5,rand = 0.25):
            self.__head = Node(0,"")
            self.__tail = Node(255,"")
            self.__maxLevel = maxLevel
            self.__rand = rand

            index = 0
            while index < maxLevel:
                self.__head.level.insert(index,self.__tail)
                index += 1
```

这一段代码的意思是说,将head所有层都指向tail(为什么要这样做呢,我们来看看SkipList的插入)

        |------|     |------|
        | head | --> | tail |
        |------|     |------|

        |------|     |------|
        | head | --> | tail |
        |------|     |------|

        |------|     |------|
        | head | --> | tail |
        |------|     |------|

---

### 插入

```python
    def Insert (self,key,value):

        if self.__tail.key <= key:
            self.__tail.key = key + 1

        level = self.__randLevel()      

        node = Node(key,value)

        for index in range(0,level):
            prev = self.__head
            while prev.level[index].key <= key:
                prev = prev.level[index]

            if prev.key == key:
                prev.value = value
                break
            else:
                node.level.append(prev.level[index])
                prev.level[index] = node


    def __randLevel (self):
        l = 1
        while l <= self.__maxLevel and random.random() < self.__rand:
            l += 1
        return l
```

解释一下这两个方法有什么用:

1. 首先要根据 Insert的参数 key 和 value 创建对应的节点,但是一开始是没有层数的,所以就使用 randLevel 这个方法来随机生成节点的层数
2. 生成了节点后,根据层数循环查询该层中 小于并最接近key 的那一个节点,新节点的那一层的next将指向它的next,它的next指向新节点

如图

原来是这样的

        |------|                                            |------|
        | head | -----------------------------------------> | tail |
        |------|                                            |------|

        |------|                                            |------|
        | head | -----------------------------------------> | tail |
        |------|                                            |------|

        |------|                                            |------|
        | head | -----------------------------------------> | tail |
        |------|                                            |------|

然后 Insert(1,"hello world"),随机到层数是1

        |------|                                            |------|
        | head | -----------------------------------------> | tail |
        |------|                                            |------|

        |------|                                            |------|
        | head | -----------------------------------------> | tail |
        |------|                                            |------|

        |------|                  |------|                  |------|
        | head | ---------------> |  1   | ---------------> | tail |
        |------|                  |------|                  |------|

---
在我想象中的跳跃链表就像是一个很奇怪的二维数组,例

        |------|                  |------|                  |------|
        | head | ---------------> |   3  |----------------> | tail |(最高层)
        |------|                  |------|                  |------|

        |------|                  |------|     |------|     |------|
        | head | ---------------> |   3  | --> |   4  | --> | tail |
        |------|                  |------|     |------|     |------|

        |------|     |------|     |------|     |------|     |------|
        | head | --> |  1   | --> |   3  | --> |   4  | --> | tail |(最底层)
        |------|     |------|     |------|     |------|     |------|

会像这样跨过一些节点.

假设我要查找 4的节点,从最高层的head开始,先查找同一层是否有指向4这个节点,结果查到3这个节点后就没有了,所以从3这个节点的最高层向下一层查找,然后就找到了4这个节点
