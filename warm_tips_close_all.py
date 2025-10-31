import tkinter as tk
import random
import sys

def close_all_windows(root, current_window=None):
    """关闭所有窗口并退出程序"""
    # 关闭当前窗口（如果提供）
    if current_window:
        current_window.destroy()
    
    # 关闭主窗口
    root.destroy()
    
    # 退出程序
    sys.exit()

def show_warm_tip(root):
    """显示一个温馨提示窗口"""
    # 创建顶级窗口
    window = tk.Toplevel(root)
    
    # 获取屏幕宽高
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # 随机窗口位置（确保窗口完全显示在屏幕内）
    window_width = 250
    window_height = 100  # 增加高度以容纳内容
    
    # 计算随机位置
    max_x = screen_width - window_width
    max_y = screen_height - window_height
    x = random.randint(0, max_x) if max_x > 0 else 0
    y = random.randint(0, max_y) if max_y > 0 else 0
    
    # 设置窗口标题和大小位置
    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # 提示文字列表
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己',
        '我想你了', '梦想成真', '期待下一次见面',
        '金榜题名', '顺顺利利', '早点休息',
        '愿所有烦恼都消失', '别熬夜', '今天过得开心嘛',
        '天冷了，多穿衣服', '加油你是最棒的', '享受每一天',
        '保持耐心', '相信自己', '学会放松',
        '注意休息', '你很棒', '坚持就是胜利',
        '保持乐观', '珍惜当下', '平安喜乐'
    ]
    
    # 随机选择提示文字
    tip = random.choice(tips)
    
    # 多样的背景颜色和对应的文字颜色（确保对比度）
    color_schemes = [
        ('lightpink', 'darkred'),        # 浅粉背景，深红文字
        ('skyblue', 'darkblue'),         # 天蓝背景，深蓝文字
        ('lightgreen', 'darkgreen'),     # 浅绿背景，深绿文字
        ('lavender', 'indigo'),          # 薰衣草紫背景，靛蓝文字
        ('lightyellow', 'darkorange'),   # 浅黄背景，深橙文字
        ('plum', 'purple'),              # 李子紫背景，紫色文字
        ('coral', 'darkred'),            # 珊瑚橙背景，深红文字
        ('bisque', 'sienna'),            # 陶土色背景，赭色文字
        ('aquamarine', 'teal'),          # 海蓝宝石背景，青绿色文字
        ('mistyrose', 'maroon'),         # 雾玫瑰色背景，栗色文字
        ('honeydew', 'olive'),           # 蜜瓜色背景，橄榄色文字
        ('lavenderblush', 'purple'),     # 薰衣草粉背景，紫色文字
        ('oldlace', 'brown'),            # 旧蕾丝色背景，棕色文字
        ('lightcyan', 'navy'),           # 浅青色背景，藏青色文字
        ('lemonchiffon', 'darkgoldenrod'),# 柠檬雪纺色背景，深金色文字
        ('lightcoral', 'darkred'),       # 浅珊瑚色背景，深红文字
        ('lightsteelblue', 'steelblue'), # 轻钢蓝色背景，钢蓝色文字
        ('lightgoldenrodyellow', 'goldenrod'), # 浅金rodyellow背景，金rod文字
        ('linen', 'peru'),               # 亚麻色背景，秘鲁色文字
        ('aliceblue', 'blue')            # 爱丽丝蓝背景，蓝色文字
    ]
    
    # 随机选择颜色方案
    bg_color, text_color = random.choice(color_schemes)
    
    # 设置整个窗口的背景颜色
    window.config(bg=bg_color)
    
    # 创建主框架，覆盖整个窗口
    main_frame = tk.Frame(window, bg=bg_color)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # 创建标签并显示文字
    label = tk.Label(
        main_frame,
        text=tip,
        bg=bg_color,
        fg=text_color,  # 使用对比色文字
        font=('微软雅黑', 16, 'bold'),
        wraplength=window_width - 20,
        justify=tk.CENTER
    )
    label.pack(pady=(0, 15), fill=tk.BOTH, expand=True)
    
    # 创建关闭按钮框架
    button_frame = tk.Frame(main_frame, bg=bg_color)
    button_frame.pack(fill=tk.X)
    
    # 创建关闭按钮（点击后关闭整个程序）
    close_btn = tk.Button(
        button_frame,
        text='关闭程序',
        command=lambda: close_all_windows(root, window),
        bg=text_color,          # 使用文字颜色作为按钮背景
        fg=bg_color,           # 使用背景颜色作为按钮文字
        font=('微软雅黑', 11, 'bold'),
        width=12,
        bd=0,                  # 无边框
        relief=tk.FLAT,        # 扁平样式
        activebackground=text_color,
        activeforeground=bg_color
    )
    close_btn.pack(side=tk.RIGHT, pady=5)
    
    # 窗口置顶显示
    window.attributes('-topmost', True)
    
    # 窗口总是在最前面
    window.lift()

def schedule_next_tip(root, interval=3000):
    """安排下一个提示窗口的显示"""
    # 显示新的提示窗口
    show_warm_tip(root)
    
    # 继续安排下一个提示
    root.after(interval, schedule_next_tip, root, interval)

def main():
    # 创建主窗口（隐藏）
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    
    # 立即显示第一个提示窗口
    show_warm_tip(root)
    
    # 安排后续的提示窗口，每3秒一个
    root.after(1000, schedule_next_tip, root, 1000)
    
    # 运行主事件循环
    root.mainloop()

if __name__ == '__main__':
    main()
