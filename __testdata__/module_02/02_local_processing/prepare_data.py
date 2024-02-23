import sys
import os
import json
from datetime import datetime
from yt.wrapper import YtClient, yt_dataclass
from _common import TEST_DIR, SOURCE_PATH



@yt_dataclass
class UserEvent:
    userid: str
    timestamp: datetime
    action: str
    value: float
    testids: str



def read_source_file():
    with open("../../user_activity_log.tsv", "r") as f:
        next(f)  # skip header
        for line in f:
            row = line.strip().split("\t")
            row = row if len(row) == 5 else row + [""]
            yield UserEvent(
                userid=row[0],
                timestamp=datetime.fromisoformat(row[1]),
                action=row[2],
                value=float(row[3]),
                testids=row[4]
            )


def main():
    if len(sys.argv) < 2:
        raise ValueError("prepare_data should be invoked with <test dir argument")
    test_params_path = os.path.join(sys.argv[1], "params")

    with open(test_params_path, "r") as file:
        params = json.load(file)

    start, end, step = params["start"], params["end"], params["step"]

    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    client.remove(TEST_DIR, recursive=True, force=True)
    client.create("map_node", TEST_DIR, recursive=True, force=True)

    data = [r for r in read_source_file()]
    client.write_table_structured(
        SOURCE_PATH,
        UserEvent,
        data[start:end:step],
        table_writer={"block_size": 512 * 1024, "desired_chunk_size": 1024 * 1024}
    )


if __name__ == "__main__":
    main()
