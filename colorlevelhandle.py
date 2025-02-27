def value_to_color(value, vmin=-1000, vmax=1000):
    t = (value - vmin) / (vmax - vmin)  # 归一化到 [0,1]
    
    # 定义颜色节点（位置和RGB值）
    color_stops = [
        (0.0,   (255, 0, 0)),     # 红
        (0.25,  (255, 127, 0)),   # 橙
        (0.5,   (255, 255, 0)),   # 黄
        (0.75,  (0, 255, 0)),     # 绿
        (1.0,   (139, 0, 255))    # 紫
    ]
    
    # 找到相邻颜色节点
    for i in range(len(color_stops)-1):
        t0, rgb0 = color_stops[i]
        t1, rgb1 = color_stops[i+1]
        if t0 <= t <= t1:
            # 线性插值
            dt = t1 - t0
            interp = (t - t0) / dt
            r = int(rgb0[0] + (rgb1[0] - rgb0[0]) * interp)
            g = int(rgb0[1] + (rgb1[1] - rgb0[1]) * interp)
            b = int(rgb0[2] + (rgb1[2] - rgb0[2]) * interp)
            return f"#{r:02X}{g:02X}{b:02X}"
    
    return "#000000"  # 默认黑色

# 示例
print(value_to_color(-1000))  # #FF0000（红）
print(value_to_color(0))      # #FFFF00（黄）
print(value_to_color(1000))   # #8B00FF（紫）