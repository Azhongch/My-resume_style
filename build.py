import json
import os
from jinja2 import Template

def build_resume():
    # 1. 讀取 JSON 資料
    try:
        with open('resume_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("錯誤：找不到 resume_data.json 檔案")
        return

    # 2. 讀取 HTML 模板
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("錯誤：找不到 template.html 檔案")
        return

    # 3. 使用 Jinja2 進行渲染
    # 我們將 JSON 內容直接解包傳入模板
    template = Template(template_content)
    rendered_html = template.render(**data)

    # 4. 輸出最終的 index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print("✨ 恭喜！網頁已成功生成：index.html")
    print(f"🔗 本地預覽路徑: file://{os.path.abspath('index.html')}")

if __name__ == "__main__":
    build_resume()
