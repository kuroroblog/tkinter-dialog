import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import filedialog

# filedialogのaskdirectoryのdialogを表示する。
def getAskDirectory():
    # ディクレトリを選択するためのdialogになります。
    # 戻り値 : Chooseを選択してディレクトリを開いた場合 : ディレクトリパス, Cancelを選択した場合 : ''
    directoryName = filedialog.askdirectory()
    # レスポンスの内容を表示する。
    print("ask directory", directoryName)

# filedialogのasksaveasfilenameのdialogを表示する。
def getAskSaveAsFileName():
    # 単数ファイルを保存するためのdialogになります。
    # ※筆者のMac OS環境ではファイル保存されませんでした。
    # 戻り値 : Saveを選択してファイルを保存した場合 : ファイルパス, Cancelを選択した場合 : ''
    filename = filedialog.asksaveasfilename()
    # レスポンスの内容を表示する。
    print("ask save as file name", filename)

# filedialogのaskopenfilenamesのdialogを表示する。
def getAskOpenFileNames():
    # 複数ファイルを選択するためのdialogになります。
    # 戻り値 : Openを選択してファイルを開いた場合 : (ファイルパス1, ファイルパス2), Cancelを選択した場合 : ''
    filenames = filedialog.askopenfilenames()
    # レスポンスの内容を表示する。
    print("ask open file names", filenames)

# filedialogのaskopenfilenameのdialogを表示する。
def getAskOpenFileName():
    # 単数ファイルを選択するためのdialogになります。
    # 戻り値 : Openを選択してファイルを開いた場合 : ファイルパス, Cancelを選択した場合 : ''
    filename = filedialog.askopenfilename()
    # レスポンスの内容を表示する。
    print("ask open file name", filename)

# filedialogのasksaveasfileのdialogを表示する。
def getAskSaveAsFile():
    # 単数ファイルを保存するためのdialogになります。
    # write only
    # 戻り値 : Saveを選択してファイルを保存した場合 : ファイル情報, Cancelを選択した場合 : None
    fileData = filedialog.asksaveasfile()
    # レスポンスの内容を表示する。
    print("ask save as file", fileData)

# filedialogのaskopenfilesのdialogを表示する。
def getAskOpenFiles():
    # 複数ファイル選択するためのdialogになります。
    # read only
    # 戻り値 : Openを選択してファイルを開いた場合 : [ファイル情報1, ファイル情報2, ...], Cancelを選択した場合 : ''
    fileData = filedialog.askopenfiles()
    # レスポンスの内容を表示する。
    print("ask open files", fileData)

# filedialogのaskopenfileのdialogを表示する。
def getAskOpenFile():
    # 単数ファイル選択するためのdialogになります。
    # read only
    # 戻り値 : Openを選択してファイルを開いた場合 : ファイル情報, Cancelを選択した場合 : None
    fileData = filedialog.askopenfile()
    # レスポンスの内容を表示する。
    print("ask open file", fileData)

# simpledialogのaskfloatのdialogを表示する。
def getAskFloat():
    # 浮動小数点数で答える質問を提供するsimpledialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : 値入力を促すメッセージ内容
    # 戻り値 : OKを選択した場合 : 浮動小数点数, Cancelを選択した場合 : None
    res = simpledialog.askfloat("好きな浮動小数点数はなんですか?", "好きな浮動小数点数を入力してください。")
    # レスポンスの内容を表示する。
    print("askfloat", res)

# simpledialogのaskintegerのdialogを表示する。
def getAskInteger():
    # 整数で答える質問を提供するsimpledialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : 値入力を促すメッセージ内容
    # 戻り値 : OKを選択した場合 : 整数, Cancelを選択した場合 : None
    res = simpledialog.askinteger("好きな整数はなんですか?", "好きな整数を入力してください。")
    # レスポンスの内容を表示する。
    print("askinteger", res)

# simpledialogのaskstringのdialogを表示する。
def getAskString():
    # 文字列で答える質問を提供するsimpledialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : 値入力を促すメッセージ内容
    # 戻り値 : OKを選択した場合 : 文字列, Cancelを選択した場合 : None
    res = simpledialog.askstring("アンパンマンで好きなキャラクターは?", "好きなキャラクターを入力してください。")
    # レスポンスの内容を表示する。
    print("askstring", res)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    # Windowの非表示
    root.withdraw()

    # simpledialog list
    # getAskString()
    # getAskInteger()
    # getAskFloat()

    # filedialog list
    # getAskOpenFile()
    # getAskOpenFiles()
    # getAskSaveAsFile()
    # getAskOpenFileName()
    # getAskOpenFileNames()
    # getAskSaveAsFileName()
    # getAskDirectory()
