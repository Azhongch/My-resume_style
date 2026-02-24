import json
import os

try:
    from jinja2 import Template
except ImportError:
    print("❌ 錯誤：尚未安裝 jinja2，請確認 build.yml 中有 pip install jinja2")
    exit(1)

# 讀取檔案
try:
    with open('resume_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('template.html', 'r', encoding='utf-8') as f:
        template_str = f.read()
    
    # 渲染網頁
    template = Template(template_str)
    output_html = template.render(data=data)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output_html)
    print("✅ 恭喜！index.html 已成功生成")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")
    exit(1)
