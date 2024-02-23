from yt.wrapper import YtClient


SOURCE_PATH = "//home/student/logs/user_activity_log"

TARGET_PATH = "//home/student/assignments/user_sessions/output"



def main():
    client = YtClient(proxy="127.0.01:8000", config={"proxy": {"enable_proxy_discovery": False}})
    ...



if __name__ == "__main__":
    main()
