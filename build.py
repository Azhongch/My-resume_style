import json

# 1. 讀取資料 (JSON)
with open('resume_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 2. 讀取模板 (HTML)
with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 3. 簡單的取代邏輯 (之後可以用 Jinja2 升級)
output = template.replace('{{ data.name }}', data['name'])
output = output.replace('{{ data.title }}', data['title'])
output = output.replace('{{ data.contact.email }}', data['contact']['email'])

# 4. 產出最終網頁檔案
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("✅ index.html 已經生成完畢！")
