
import os, re, glob
from PIL import Image, ImageDraw, ImageFont
#現在のファイルの位置を取得する。
path = os.getcwd()

# EXIFから撮影を取得
def get_datetime(img):
    exif = img._getexif()
    for id, val in exif.items():
        if id == 36867:
            return val
    return ''

#保存用の新しいファイルを作成する。
os.chdir('../')
WD = os.getcwd()
NUMBER = 1
DIR = WD + "\\" + str(NUMBER)
for curDir, dirs, files in os.walk(WD):
    for WKDIR in dirs:
        if WKDIR in DIR:
            NUMBER = NUMBER + 1
            DIR = WD + "\\" + str(NUMBER)

os.mkdir(DIR)

#指定したファイル以下のファイルを開く。
for curDir, dirs, files in os.walk(path):
    for file in files:
        if 'JPG' in file:
#開いたファイルの中の画像を、保存用のファイルに保存する。
            file_path = os.path.join(curDir, file)
            img = Image.open(file_path)

#画像の日時を取得
            text_datetime = get_datetime(img)
            text_date = text_datetime.split()[0]    # 時刻を切り離す。
            text_date = text_date.replace(':','-')   # 年月日の区切り文字を変更

#テキスト表示位置を決定
            img_resize = img.resize((320,240))
            pos_x = img_resize.size[0]-150
            pos_y = img_resize.size[1]-30

#画像にテキストを追記
            obj_draw = ImageDraw.Draw(img_resize)
            obj_font = ImageFont.truetype("C:\\Users\\y-maesaki\\Downloads\\ipagp00303\\ipagp.ttf", 24)
            obj_draw.text((pos_x+1, pos_y+1), text_date, fill=(0,0,0),     font=obj_font)
            obj_draw.text((pos_x, pos_y),     text_date, fill=(255,160,0), font=obj_font)
            img_resize.save(DIR + '\\' + file)