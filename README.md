# pairwise-cubeshadow-seam-bias

## 领域

游戏、图形与多媒体

## 主题

点光源立方阴影接缝

## 说明

面边缘 guard、斜率偏置与逐面失效。

初始状态下 `graphics/cubeshadow_seam_bias.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
