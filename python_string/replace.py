# coding:utf-8

info = (
    '由于“软件危机”的产生，迫使人们不得不研究、改变软件开发的技术手段和管理方法。从此软件产生进入了软件工程时代。'
    '此阶段的特点是：硬件已向巨型化、微型化、网络化和智能化四个方向发展，数据库技术已成熟并广泛应用，第三代、'
    '第四代语言出现；第一代软件技术：结构化程序设计在数值计算领域取得优异成绩；第二代软件技术：软件测试技术、方法、'
    '原理用于软件生产过程；第三代软件技术：处理需求定义技术用于软件需求分析和描述。'
)
words = ['软件', '技术', '特点']

for word in words:
    if word in info:
        info = info.replace(word, '**')

print(info)
