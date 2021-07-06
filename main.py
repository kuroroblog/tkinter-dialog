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

# simpledialog.Dialogクラスを継承したCustomDialogクラスを作成する。
# 1. 新しくクラスを作成する
# 2. 新しく作成するクラスにsimpledialog.Dialogのクラスを継承する
class CustomDialog(simpledialog.Dialog):
    # じゃんけんの手の情報を格納する変数
    handList = [
        'グー',
        'チョキ',
        'パー',
    ]
    # 現在選択されているラジオボタンの値を格納する変数
    variable = None

    # 3. body関数, buttonbox関数, apply関数をオーバーライドしてカスタマイズする
    def body(self, master):
        # bodyを親要素として、label Widgetを作成する。
        # text : テキスト情報
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(master, text='じゃんけんの手を選択してください。')
        # bodyを親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

        # 現在選択されているラジオボタンの値を文字列変数として扱う。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        self.variable = tk.StringVar()
        for hand in self.handList:
            # bodyを親要素として、radiobutton Widgetを作成する。
            # value : ラジオボタン自身が持つ値の設定。グー or チョキ or パー
            # variable : 現在選択中のラジオボタンの値を設定。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
            # command : ラジオボタンを選択した場合に、実行する関数を設定。self.switchButtonStateとする。
            # text : ラジオボタンを説明するテキスト。
            # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
            radiobutton = tk.Radiobutton(master, value=hand, variable=self.variable, command=self.switchButtonState, text=hand)
            # bodyを親要素として、radiobutton Widgetをどのように配置するのか?
            # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
            radiobutton.pack(side=tk.LEFT, padx=5, pady=5)

    # 3. body関数, buttonbox関数, apply関数をオーバーライドしてカスタマイズする
    def buttonbox(self):
        # buttonboxを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self)
        # buttonboxを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # command : ボタンを選択した場合に、実行する関数を設定する。self.okとする。
        # state : ボタンの状態を設定する。ラジオボタンが選択されていない初期状態では、tk.DISABLEDにして選択できないようにする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        self.selectBtn = tk.Button(frame, text="Select", width=10, command=self.ok, state=tk.DISABLED)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.selectBtn.pack(side=tk.LEFT, padx=5, pady=5)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # command : ボタンを選択した場合に、実行する関数を設定する。self.cancelとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        self.cancelBtn = tk.Button(frame, text="Cancel", width=10, command=self.cancel)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.cancelBtn.pack(side=tk.LEFT, padx=5, pady=5)

    def switchButtonState(self):
        # ラジオボタンが選択された場合に、Selectボタンを有効化する。
        if self.selectBtn['state'] == tk.DISABLED:
            self.selectBtn['state'] = tk.NORMAL

    # 3. body関数, buttonbox関数, apply関数をオーバーライドしてカスタマイズする
    def apply(self):
        # dialogを閉じた後に、ラジオボタンの選択結果を出力する。
        print(self.variable.get())


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

    # CustomDialog(root)
