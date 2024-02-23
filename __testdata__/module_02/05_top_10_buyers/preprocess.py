import sys


def main():
    with open("solution.py", "r") as file:
        contents = file.read()
    
    try:
        assert "map" in contents
        assert "reduce" in contents
    except AssertionError:
        print("Решение не содержит все необходимые конструкции.", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)
    
    if "TablePath" not in contents:
        print("Используйте TablePath в сочетании с указанием диапазона для эффективного чтения данных с кластера.", file=sys.stderr)

    try:
        assert "write_table" not in contents
    except AssertionError:
        print("Решение содержит конструкции, запрещённые в данной задаче.", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)
