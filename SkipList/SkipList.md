# 跳跃链表

## 参考网址
* [浅析SkipList跳跃表原理及代码实现](http://blog.csdn.net/ict2014/article/details/17394259)

跳跃链表比起一般的链表来说,优势在于查询速度较快,以内存的空间换取查询的时间.

因为跳跃链表是跨了节点去查询的,链表的查询时间是根据目标节点所在的位置与链表的头部相隔多少个节点

---

### 初始化
我们先建立SkipList的节点

```
    class Node (object):

        def __init__ (self,key,value):
            self.key = key
            self.value = value
            self.level = []
```

然后再建立SkipList

```
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

