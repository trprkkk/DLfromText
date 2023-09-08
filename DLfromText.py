import re
import requests

# テキストファイルのパスを指定
file_path = "Your text file pass"

# ファイルを開いて中身を読み込みます
with open(file_path, "r",encoding="utf-8_sig") as file:
    text = file.read()

# 正規表現パターンを定義します
pattern = r'https:[^ ]*\.m4a'

# 正規表現パターンに一致するすべての文字列を抽出します
matches = re.findall(pattern, text)

# 抽出されたリンクごとにダウンロードを試みます
for link in matches:
    try:
        # ファイルをダウンロード
        response = requests.get(link)
        
        # ダウンロードが成功した場合、ファイルを保存
        if response.status_code == 200:
            filename = link.split("/")[-1]  # ファイル名を抽出
            with open(filename, "wb") as output_file:
                output_file.write(response.content)
            print(f"ダウンロード成功: {filename}")
        else:
            print(f"ダウンロード失敗: {link}")
    except Exception as e:
        print(f"エラー: {e}")
