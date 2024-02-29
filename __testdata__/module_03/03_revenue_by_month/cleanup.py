import os
from yt.wrapper import YtClient
from _common import get_paths, drop_session_id


def main():
    paths = get_paths()
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    try:
        client.remove(paths.TEST_DIR, recursive=True, force=True)
    except:
        pass
    
    try:
        os.remove("solution_output")
    except FileNotFoundError:
        pass

    try:
        os.remove("solution.py")
    except FileNotFoundError:
        pass

    drop_session_id()


if __name__ == "__main__":
    main()
