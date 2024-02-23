import sys
import solution
import _common
from datetime import date
from yt.wrapper import YtClient, yt_dataclass



@yt_dataclass
class UsersByMonth:
    month: str
    count: int



def fingerprint():
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    data = client.read_table_structured(_common.TARGET_PATH, UsersByMonth)

    for ud in sorted(data, key=lambda ud: ud.month):
        print(ud.month, "\t", ud.count)



def main():
    try:
        solution.SOURCE_PATH = _common.SOURCE_PATH
        solution.TARGET_PATH = _common.TARGET_PATH
    except AttributeError:
        print("Файл решения должен содержать глобальные переменные SOURCE_PATH и TARGET_PATH", file=sys.stderr)
        exit(1)

    solution.main()

    fingerprint()



if __name__ == "__main__":
    main()
