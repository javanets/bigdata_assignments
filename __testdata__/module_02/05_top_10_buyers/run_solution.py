import sys
import solution
import _common



def main():
    try:
        solution.SOURCE_PATH = _common.SOURCE_PATH
    except AttributeError:
        print("Файл решения должен содержать глобальные переменные SOURCE_PATH и TARGET_PATH", file=sys.stderr)
        exit(1)

    solution.main()



if __name__ == "__main__":
    main()
