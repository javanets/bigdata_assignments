import os
import sys
from _common import generate_session_id, get_paths


def main():
    generate_session_id()

    paths = get_paths()

    with open("solution.py", "r") as file:
        contents = file.read()
    contents = contents.lower()
    try:
        assert "select" in contents
        assert "insert" in contents
    except AssertionError:
        print("Решение не содержит все необходимые конструкции.", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)
    
    try:
        assert paths.INITIAL_SOURCE_PATH in contents
    except AssertionError:
        print(f"Решение не считывает данные по пути `{paths.INITIAL_SOURCE_PATH}`", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)
    
    try:
        assert paths.INITIAL_TARGET_PATH in contents
    except AssertionError:
        print(f"Решение не записывает данные по пути `{paths.INITIAL_TARGET_PATH}`", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)

    try:
        pass
    except AssertionError:
        print("Решение содержит конструкции, запрещённые в данной задаче.", file=sys.stderr)
        print("Если вы не согласны с вердиктом, обратитесь в чат поддержки.", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)
