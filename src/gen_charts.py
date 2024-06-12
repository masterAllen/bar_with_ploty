'''
使用 Plotly 绘制直方图
'''
import numpy as np
import plotly.graph_objects as go

def run(now_data, title):
    if len(now_data) == 0:
        return go.Figure(data=[])

    # 横纵坐标数据
    barx = np.arange(0, len(now_data))
    bary = now_data

    # ! 文字处理
    sumy = np.sum(bary)
    # 加文字，判断当前柱子是否够长，够长就不显示，不够长
    textvs = [str(int(y)) if y/sumy<0.01 else '' for y in bary]
    # 文字位置，判断当前柱子长度，长则 inside（本例不需要，因为够长时文字是空）
    textps = ['outside' if y/sumy<0.01 else 'inside' for y in bary]

    dict_text = {
        'textfont': {
            'size': 15,
            'color': 'black',
        },
        # 'textposition': 'outside',    # 位置: inside, outside, auto
        'textposition': textps,         # 位置: inside, outside, auto
        'textangle': 90,                # 文字进行旋转 (不加就是 auto)
        'constraintext': 'none',        # 取消文字大小自动调整
    }

    barfig = go.Bar(
        x=barx, y=bary, 
        text=textvs, **dict_text
    )

    fig = go.Figure(data=[barfig])

    # ! 调整样式
    dict_layout = {
        # 柱子之间的间隙
        'bargap': 0.1, 

        # 坐标间隔，从 tick0 开始
        'xaxis': {
            'tickmode': 'linear',
            'tick0': 0,
            'dtick': 1,
            'title': '像素值',
        },
        'yaxis': {
            'title': '数量',
        },

        # 标题
        'title': title,

        # 大小
        'height': 300,
        # 'width': 300, 
        'margin': dict(t=40,b=40,l=0,r=0),
    }

    fig.update_layout(**dict_layout)
    return fig