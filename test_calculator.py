from calculator import add, subtract, multiply, divide

tests = [
    ("add(3, 4)",        add(3, 4),        7),
    ("add(-1, 1)",       add(-1, 1),       0),
    ("subtract(10, 3)", subtract(10, 3),  7),
    ("subtract(0, 5)",  subtract(0, 5),  -5),
    ("multiply(4, 5)",  multiply(4, 5),  20),
    ("multiply(-2, 3)", multiply(-2, 3), -6),
    ("divide(10, 2)",   divide(10, 2),    5.0),
    ("divide(7, 2)",    divide(7, 2),     3.5),
    ("divide(5, 0)",    divide(5, 0),     "エラー: 0で割ることはできません"),
]

all_pass = True
for name, result, expected in tests:
    ok = result == expected
    status = "PASS" if ok else "FAIL"
    if not ok:
        all_pass = False
    print(f"[{status}] {name} => {result}  (期待値: {expected})")

print()
print("全テスト合格" if all_pass else "失敗したテストがあります")
