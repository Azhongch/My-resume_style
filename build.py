import json
from jinja2 import Template

# 1. 讀取資料
with open('resume_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 讀取模板 (這就是你原本那段 HTML)
with open('template.html', 'r', encoding='utf-8') as f:
    template_str = f.read()

# 3. 使用 Jinja2 渲染 (這能處理 for 迴圈)
template = Template(template_str)
output_html = template.render(data=data)

# 4. 產出網頁
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

print("✅ index.html 更新成功！")
