def hex_to_rgb(hex_color):
    """
    将十六进制颜色代码转换为RGB元组
    
    参数:
        hex_color: 十六进制颜色代码，例如'#FF0000'
    
    返回:
        RGB元组 (r, g, b)，值范围在0-1之间
    """
    # 移除'#'前缀
    hex_color = hex_color.lstrip('#')
    # 将十六进制转换为RGB
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b)

def rgb_to_hex(rgb):
    """
    将RGB元组转换为十六进制颜色代码
    
    参数:
        rgb: RGB元组 (r, g, b)，值范围在0-1之间
    
    返回:
        十六进制颜色代码，例如'#FF0000'
    """
    r, g, b = rgb
    # 将0-1范围转换为0-255范围
    r = min(255, max(0, int(r * 255)))
    g = min(255, max(0, int(g * 255)))
    b = min(255, max(0, int(b * 255)))
    # 转换为十六进制
    return f'#{r:02x}{g:02x}{b:02x}'

def interpolate_color(color1, color2, t):
    """
    在两个颜色之间进行线性插值
    
    参数:
        color1: 第一个RGB颜色元组
        color2: 第二个RGB颜色元组
        t: 插值参数，范围[0,1]
    
    返回:
        插值后的RGB颜色元组
    """
    r = color1[0] * (1 - t) + color2[0] * t
    g = color1[1] * (1 - t) + color2[1] * t
    b = color1[2] * (1 - t) + color2[2] * t
    return (r, g, b)

def get_rainbow_color(value, vmin=-1000, vmax=1000):
    """
    将[-1000, 1000]范围内的值映射到彩虹色阶。
    
    参数:
        value: 需要映射的值
        vmin: 数据范围的最小值，默认为-1000
        vmax: 数据范围的最大值，默认为1000
    
    返回:
        RGB颜色元组 (r, g, b)，值范围在0-1之间
    """
    # 彩虹色阶定义
    colors = [
        (0.0,  '#FF0000'),   # 红，t=0.0
        (0.25, '#FF7F00'),   # 橙，t=0.25
        (0.5,  '#FFFF00'),   # 黄，t=0.5
        (0.75, '#00FF00'),   # 绿，t=0.75
        (1.0,  '#8B00FF')    # 紫，t=1.0
    ]
    
    # 将颜色转换为RGB
    rgb_colors = [(pos, hex_to_rgb(color)) for pos, color in colors]
    
    # 将值归一化到[0,1]范围
    norm_value = (value - vmin) / (vmax - vmin)
    # 确保值在[0,1]范围内
    norm_value = max(0, min(1, norm_value))
    
    # 找到对应的颜色区间
    for i in range(len(rgb_colors) - 1):
        pos1, color1 = rgb_colors[i]
        pos2, color2 = rgb_colors[i + 1]
        
        if pos1 <= norm_value <= pos2:
            # 计算在当前区间内的相对位置
            t = (norm_value - pos1) / (pos2 - pos1)
            # 在两个颜色之间进行插值
            return interpolate_color(color1, color2, t)
    
    # 如果值超出范围，返回边界颜色
    if norm_value <= 0:
        return rgb_colors[0][1]
    else:
        return rgb_colors[-1][1]

def get_rainbow_color_hex(value, vmin=-1000, vmax=1000):
    """
    将[-1000, 1000]范围内的值映射到彩虹色阶，并返回十六进制颜色代码。
    
    参数:
        value: 需要映射的值
        vmin: 数据范围的最小值，默认为-1000
        vmax: 数据范围的最大值，默认为1000
    
    返回:
        十六进制颜色代码，例如'#FF0000'
    """
    rgb = get_rainbow_color(value, vmin, vmax)
    return rgb_to_hex(rgb)

# 示例用法
if __name__ == "__main__":
    # 测试不同值的颜色映射
    test_values = [-1000, -500, 0, 500, 1000]
    
    print("值 -> RGB颜色 -> 十六进制颜色")
    for val in test_values:
        rgb = get_rainbow_color(val)
        hex_color = get_rainbow_color_hex(val)
        print(f"{val} -> {rgb} -> {hex_color}") 