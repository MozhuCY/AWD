# AWD

usage:

```python
from AWD import *

xxx = AWD("pwn1.log")
flag = exp(ip,port)
xxx.join(ip,flag)
```

新建flag提交线程

可以使用Log函数直接往log文件里写，使用tail -f监控log，直接避开pwntools一坨一坨的Log盖住了我们感兴趣的部分