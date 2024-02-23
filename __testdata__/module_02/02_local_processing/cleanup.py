import os
from yt.wrapper import YtClient
from _common import TEST_DIR


def main():
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    client.remove(TEST_DIR, recursive=True, force=True)
    
    try:
        os.remove("solution_output")
    except FileNotFoundError:
        pass

    try:
        os.remove("solution.py")
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
