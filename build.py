import json
import sys
import os

try:
    from jinja2 import Template
except ImportError:
    print("❌ 錯誤：尚未安裝 jinja2。")
    sys.exit(1)

def run_build():
    try:
        # 讀取資料
        if not os.path.exists('resume_data.json'):
            print("❌ 錯誤：找不到 resume_data.json")
            return

        with open('resume_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 讀取模板
        if not os.path.exists('template.html'):
            print("❌ 錯誤：找不到 template.html")
            return

        with open('template.html', 'r', encoding='utf-8') as f:
            template_str = f.read()

        # 渲染
        template = Template(template_str)
        output = template.render(data=data)

        # 產出
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(output)
        
        print("✅ index.html 成功更新")

    except Exception as e:
        print(f"❌ 發生非預期錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_build()