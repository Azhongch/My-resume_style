import json
import os
from jinja2 import Template

def build_resume():
    # 讀取資料
    try:
        with open('resume_data.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        with open('template.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
    except Exception as e:
        print(f"檔案讀取失敗: {e}")
        return

    # 執行渲染 - 明確定義 data=json_data 解決 UndefinedError
    template = Template(template_content)
    try:
        rendered_html = template.render(data=json_data)
        
        # 輸出檔案
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(rendered_html)
            
        print("✅ 網頁生成成功！請打開 index.html 檢視成果。")
    except Exception as e:
        print(f"渲染失敗: {e}")

if __name__ == "__main__":
    build_resume()
