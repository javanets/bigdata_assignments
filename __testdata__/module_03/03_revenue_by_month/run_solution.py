from datetime import date
from yt.wrapper import YtClient, yt_dataclass
from _common import run_query, get_paths


@yt_dataclass
class MonthValue:
    month: str
    value: float


def execute_query(query):
    paths = get_paths()
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    run_query(client, query)
    data = client.read_table_structured(paths.TEST_TARGET_PATH, MonthValue)

    for mv in sorted(data, key=lambda x: x.month):
        print(mv.month, round(mv.value, 3), sep="\t")




def main():
    paths = get_paths()
    with open("solution.py", "r") as f:
        query = f.read()
    query = query.replace(paths.INITIAL_SOURCE_PATH, paths.TEST_SOURCE_PATH)
    query = query.replace(paths.INITIAL_TARGET_PATH, paths.TEST_TARGET_PATH)
    execute_query(query)


if __name__ == "__main__":
    main()