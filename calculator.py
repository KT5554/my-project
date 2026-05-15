# calculator.py - 四則演算ができる電卓プログラム

def add(a, b):
    # 足し算
    return a + b

def subtract(a, b):
    # 引き算
    return a - b

def multiply(a, b):
    # 掛け算
    return a * b

def divide(a, b):
    # 割り算（0で割ろうとした場合はエラーメッセージを返す）
    if b == 0:
        return "エラー: 0で割ることはできません"
    return a / b

def main():
    print("===== 電卓プログラム =====")
    print("演算子を選んでください:")
    print("  1: 足し算 (+)")
    print("  2: 引き算 (-)")
    print("  3: 掛け算 (*)")
    print("  4: 割り算 (/)")
    print("  q: 終了")
    print("=========================")

    while True:
        # メニューの選択
        choice = input("\n演算子 (1/2/3/4/q): ").strip()

        if choice == "q":
            print("電卓を終了します。")
            break

        if choice not in ("1", "2", "3", "4"):
            print("1〜4またはqを入力してください。")
            continue

        # 数値の入力
        try:
            a = float(input("1つ目の数値: "))
            b = float(input("2つ目の数値: "))
        except ValueError:
            print("数値を入力してください。")
            continue

        # 選択した演算を実行
        if choice == "1":
            result = add(a, b)
            symbol = "+"
        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"
        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"
        elif choice == "4":
            result = divide(a, b)
            symbol = "/"

        print(f"結果: {a} {symbol} {b} = {result}")

# このファイルを直接実行したときだけ main() を呼び出す
if __name__ == "__main__":
    main()
