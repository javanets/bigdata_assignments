import sys
import solution
import _common
from datetime import datetime
from itertools import groupby
from yt.wrapper import YtClient, yt_dataclass



@yt_dataclass
class SessionizedUserEvent:
    sessionid: str
    userid: str
    timestamp: datetime
    action: str
    value: float
    testids: str



def fingerprint():
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    data = client.read_table_structured(_common.TARGET_PATH, SessionizedUserEvent)

    for (userid, sessionid), events in groupby(data, key=lambda ue: (ue.userid, ue.sessionid)):
        events_list = list(events)
        first_moment = events_list[0].timestamp.isoformat()[:19]
        last_moment = events_list[-1].timestamp.isoformat()[:19]
        print(userid, first_moment, last_moment, sep="\t")



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
