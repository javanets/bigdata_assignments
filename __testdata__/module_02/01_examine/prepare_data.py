import sys
import os
import json
from yt.wrapper import YtClient, yt_dataclass
from _common import SOURCE_PATH


@yt_dataclass
class CoolTableRow:
    name: str
    rating: int


def main():
    if len(sys.argv) < 2:
        raise ValueError("prepare_data should be invoked with <test dir argument")
    test_params_path = os.path.join(sys.argv[1], "params")

    with open(test_params_path, "r") as file:
        params = json.load(file)

    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    
    client.remove(SOURCE_PATH, recursive=True, force=True)

    for node in params["map_nodes"]:
        client.create("map_node", f"{SOURCE_PATH}/{node}", recursive=True, force=True)
    

    for table in params["tables"]:
        client.write_table_structured(
            f"{SOURCE_PATH}/{table['name']}",
            CoolTableRow,
            [CoolTableRow(f"Last name {i}", i) for i in range(int(table["rows"]))],
            table_writer={"block_size": 512, "desired_chunk_size": 1024}
        )


if __name__ == "__main__":
    main()
