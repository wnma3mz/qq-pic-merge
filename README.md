## 头像拼接

```python
# python版本
python: 3.6.2

# 第三方包
from PIL import Image
import requests
import numpy as np
```

### API操作

```python
from merge_qq_img import Merge
from merge_qq_img import GetQQImg

# 获取QQ好友QQ号的参数
bkn = "bkn"
cookie = "cookie"
# uin_lst是由QQ号组成的列表
uin_lst = list()

# 实例化对象
qq_img = GetQQImg(bkn=bkn, cookie=cookie)
# 获取QQ好友头像，并解析头像为numpy数组
pic_mat = qq_img.get_array()

# 实例化对象
mer = Merge(pic_mat)
# 使用numpy进行合成，PIL保存图片, xx.png为图片名
mer.merge_pic("xx.png")
```

时间: 300多个好友，大约在1分钟以内完成

### 效果如下

![7x7图片](https://i.loli.net/2018/03/22/5ab3c57b0f193.png)

![17x17图片](https://i.loli.net/2018/03/22/5ab3c54081d86.png)


### TO-DO

- [ ] 规范API

- [ ] 添加注释

- [ ] 添加测试代码

- [ ] 增加协程`asyncio`