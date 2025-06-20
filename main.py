import datetime
import locale

def show_today_info():
    """显示今天的详细日期和时间信息"""
    
    # 获取当前日期和时间
    now = datetime.datetime.now()
    today = datetime.date.today()
    
    # 设置中文显示（如果系统支持）
    try:
        locale.setlocale(locale.LC_TIME, 'zh_CN.UTF-8')
    except:
        pass  # 如果设置失败就使用默认语言
    
    # 星期几的中文对照
    weekdays_cn = {
        0: '星期一',
        1: '星期二', 
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日'
    }
    
    # 输出基本日期信息
    print("=" * 40)
    print("📅 今日日期信息")
    print("=" * 40)
    
    print(f"📆 今天是：{today.year}年{today.month}月{today.day}日")
    print(f"🗓️  星期：{weekdays_cn[today.weekday()]}")
    print(f"⏰ 当前时间：{now.strftime('%H:%M:%S')}")
    
    # 输出更多详细信息
    print("\n" + "=" * 40)
    print("📊 详细信息")
    print("=" * 40)
    
    print(f"🌍 完整日期：{now.strftime('%Y年%m月%d日 %A')}")
    print(f"📅 今年第{today.timetuple().tm_yday}天")
    print(f"📊 今年第{today.isocalendar()[1]}周")
    print(f"🌙 今月第{(today.day - 1) // 7 + 1}周")
    
    # 判断是否为闰年
    is_leap = (today.year % 4 == 0 and today.year % 100 != 0) or (today.year % 400 == 0)
    print(f"📈 {today.year}年是{'闰年' if is_leap else '平年'}")
    
    # 计算距离年底还有多少天
    year_end = datetime.date(today.year, 12, 31)
    days_to_year_end = (year_end - today).days
    print(f"⏳ 距离年底还有{days_to_year_end}天")
    
    # 输出不同格式的日期
    print("\n" + "=" * 40)
    print("🔄 不同格式显示")
    print("=" * 40)
    
    print(f"标准格式：{today.strftime('%Y-%m-%d')}")
    print(f"美式格式：{today.strftime('%m/%d/%Y')}")
    print(f"欧式格式：{today.strftime('%d/%m/%Y')}")
    print(f"ISO格式：{today.isoformat()}")
    print(f"时间戳：{int(now.timestamp())}")

import datetime

# 简洁版本
def simple_today_info():
    """简洁版本的今日信息"""
    now = datetime.datetime.now()
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    
    print(f"今天是：{now.year}年{now.month}月{now.day}日")
    print(f"星期：{weekdays[now.weekday()]}")
    print(f"当前时间：{now.strftime('%H:%M:%S')}")

# 运行程序
if __name__ == "__main__":
    show_today_info()

