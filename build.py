import json
import os
from jinja2 import Template

def build_resume():
    # 獲取當前腳本所在資料夾路徑，確保 GitHub Action 執行時能正確找到檔案
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'resume_data.json')
    template_path = os.path.join(base_dir, 'template.html')
    output_path = os.path.join(base_dir, 'index.html')

    try:
        # 1. 讀取資料
        with open(json_path, 'r', encoding='utf-8') as f:
            resume_data = json.load(f)
        
        # 2. 讀取模板
        with open(template_path, 'r', encoding='utf-8') as f:
            template_source = f.read()

        # 3. 渲染 (關鍵：明確指定 data=resume_data)
        template = Template(template_source)
        html_output = template.render(data=resume_data)
        
        # 4. 寫入 index.html
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_output)
            
        print("Successfully built index.html")
    except Exception as e:
        print(f"Build failed: {str(e)}")
        exit(1) # 讓 GitHub Action 知道失敗了

if __name__ == "__main__":
    build_resume()