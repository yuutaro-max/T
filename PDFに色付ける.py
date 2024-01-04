#PyMuPDF 座標でテキストを検索できます。これを PyPDF2ハイライト方法 と組み合わせて使用​​すると、説
# 明していることを実現できます。または、 PyMuPDFを使用してテキストを強調表示する にすることもできます。
# PyMuPDFでテキストを検索して強調表示するためのサンプルコードは次のとおりです


import fitz
from PyPDF4 import PdfFileReader
import sys
import os

### READ IN PDF

#PDFのファイルの位置をdocumentに保存
input_pdf = sys.argv[1]

#PDFのページ数を取得
reader = PdfFileReader(input_pdf,strict=False)
word = ["協議", "提出","報告","承諾"]  # 強調表示したいキーワード

#PDFを開く
doc = fitz.open(input_pdf)

for i in range(len(reader.pages)):
    for keyword in word:
        page = doc[i]

        text = keyword
        text_instances = page.search_for(text)

        ### HIGHLIGHT
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)


### OUTPUT(出力)

output_pdf =  os.path.dirname(input_pdf) + "\\" + os.path.splitext(os.path.basename(input_pdf))[0] + "_copy1.pdf" # 出力PDFファイル
doc.save(output_pdf, garbage=4, deflate=True, clean=True)