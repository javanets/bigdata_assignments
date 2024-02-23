import sys
import solution
import _common
from datetime import date
from yt.wrapper import YtClient, yt_dataclass



@yt_dataclass
class ActionFreq:
    action: str
    avg_per_user: float



def fingerprint():
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    data = client.read_table_structured(_common.TARGET_PATH, ActionFreq)

    for af in sorted(data, key=lambda x: x.action):
        print(af.action, round(af.avg_per_user, 3), sep="\t")



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
