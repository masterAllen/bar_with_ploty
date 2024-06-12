import os
os.chdir(os.path.dirname(__file__))

import numpy as np
from string import Template

import gen_tables, gen_charts

machines = ['Machine-A', 'Machine-B']
versions = ['Version-1', 'Version-2']
conditions = ['AAA', 'BBB', 'CCC', 'DDD']

# 生成表格
table_in_html = gen_tables.run(conditions, versions, machines)

# 生成直方图的 figure
charts = []
for i, machine in enumerate(machines):
    for j, version in enumerate(versions):
        for k, condition in enumerate(conditions):
            now_data = np.load(f'../data/{i}-{j}-{k}.npy')
            now_title = f'{machine} {version} {condition}'

            now_fig = gen_charts.run(now_data, now_title)
            charts.append(now_fig)

# 有一个空图，用于占位
chart_in_html = f'''
    <div style="display: none">
        {gen_charts.run([], '').to_html(full_html=False, include_plotlyjs=True)}
    </div>
'''

# 将直方图 figure 转为 html
one_chart_str = '''
    <div id="chart" style="display: block">
        {CHART}
    </div>
'''
for idx, now_fig in enumerate(charts):
    chart_in_html += one_chart_str.format(CHART=now_fig.to_html(full_html=False, include_plotlyjs=False))

# 生成最终的 html 文件
with open('../result.html', 'w', encoding='utf-8') as f:
    template = Template(open('template.html', 'rb').read().decode('utf-8'))
    result = template.substitute(TABLES=table_in_html, CHARTS=chart_in_html)
    f.writelines(result)

