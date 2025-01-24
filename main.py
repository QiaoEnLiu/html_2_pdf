from xhtml2pdf import pisa

fileName = input("輸入檔名：") + ".pdf"
fileContent = input("輸入文本：")

# 讀取 HTML 文件
with open("www//template.html", "r") as html_file:
    html = html_file.read()
    
html = html.replace("#Title#", fileName)
html = html.replace("#Content#", fileContent)

# 使用 'wb' 模式寫入 PDF
with open(fileName, "wb") as pdf_file:
    pisa.CreatePDF(html, dest=pdf_file)