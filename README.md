## 头像拼接

版本说明

```
python: 3.6.2

PIL: 4.2.1
requests: 2.18.4
numpy: 1.13.3
```

### API操作

```python
from merge_qq_img import Merge

# uin_lst是由QQ号构造的列表
mer = Merge(uin_lst)
# 获取头像，并解析头像为numpy数组
mer.get_array()
# 使用numpy进行合成，PIL保存图片, xx.png为图片名
mer.merge_pic("xx.png")
```

300多个好友，大约在1分钟以内完成

### 效果如下

[7x7图片](https://raw.githubusercontent.com/wnma3mz/qq-pic-Splice/master/imgs/output1.png)

[17x17图片](https://raw.githubusercontent.com/wnma3mz/qq-pic-Splice/master/imgs/output2.png)


### TO-DO

[] 规范API

[] 添加注释

[] 添加测试代码

[] 增加协程`asyncio`