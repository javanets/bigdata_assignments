import os
import time
from hashlib import md5
from random import randint
import yt.yson as yson


def get_paths():
    class Paths:
        pass
    paths = Paths()

    paths.INITIAL_SOURCE_PATH = "//home/student/logs/user_activity_log"
    paths.INITIAL_TARGET_PATH = "//home/student/assignments/revenue_by_month/output"
    paths.TEST_DIR = f"//home/student/__testdata__/module_03/03_revenue_by_month/tmp-{get_session_id()}"
    paths.TEST_SOURCE_PATH = f"{paths.TEST_DIR}/input"
    paths.TEST_TARGET_PATH = f"{paths.TEST_DIR}/output"

    return paths



def generate_session_id():
    drop_session_id()
    session_id = md5(str(randint(0, 1000000000)).encode("utf-8")).hexdigest()
    with open(".session_id", "w") as f:
        f.write(session_id)



def get_session_id():
    if not os.path.exists(".session_id"):
        generate_session_id()

    with open(".session_id", "r") as f:
        return f.read().strip()



def drop_session_id():
    try:
        os.remove(".session_id")
    except FileNotFoundError:
        pass



def run_query(client, query, read_result=False):
    query_id = client.start_query("yql", query)

    while True:
        # https://github.com/ytsaurus/ytsaurus/blob/b7bbc4eaed891e422351479c98503930d3d106ca/yt/yt/tests/library/yt_queries.py#L3

        query = client.get_query(query_id, attributes=["state", "error"])

        state = query["state"]
        if state in ("failed", "aborted"):
            raise ValueError(f"Query failed with error: {query['error']}")
        elif state == "completed":
            break
        time.sleep(0.1)
        
    
    if read_result:
        result_bytes = client.read_query_result(query_id, result_index=0).read()
        result = list(yson.loads(result_bytes, yson_type="list_fragment"))
        return result
