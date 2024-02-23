from yt.wrapper import YtClient


SOURCE_PATH = "//home/student/logs/user_activity_log"

TARGET_PATH = "//home/student/assignments/churned_in_may/output"



def main():
    client = YtClient(proxy="127.0.0.1:8000", config={"proxy": {"enable_proxy_discovery": False}})
    ...



if __name__ == "__main__":
    main()
