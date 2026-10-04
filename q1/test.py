import json
def analyze_log(filepath: str) -> dict:
    result = {
        "total" :0,
        "by-level" : {},
        "by-user" : {},
        "last-error" : None,
    }


    try:
        with open(filepath, "r", encoding="utf-8")as file:
            for line in file:
                try:
                    log = json.loads(line)
                except json.JSONDecodeError:
                    continue
                result["total"]+=1
                level = log["level"]
                if level in result["by-level"]:
                    result["by-level"][level] += 1
                else:
                    result["by-level"][level] = 1
                user = log["user"]

                if user in result["by-user"]:
                    result["by-user"][user] += 1
                else:
                    result["by-user"][user] = 1
                if level == "ERROR":
                    result["last-error"] = log["message"]
    except FileNotFoundError:
        return result
    
    
    
    
    return result






a = '''{"timestamp": "2026-10-01 10:23:45", "level": "INFO", "message": "用户登录成功", "user": "张三"}
{"timestamp": "2026-10-01 10:24:01", "level": "ERROR", "message": "数据库连接失败", "user": "李四"}
{"timestamp": "2026-10-01 10:25:12", "level": "INFO", "message": "用户登出", "user": "张三"}
{"timestamp": "2026-10-01 10:26:30", "level": "ERROR", "message": "超时", "user": "李四"}
{"timestamp": "2026-10-01 10:27:00", "level": "INFO", "message": "任务完成", "user": "王五"}''' 



class Test:
    def __enter__(self):
        return a.splitlines()

    def __exit__(self, *args):
        pass


original_open = open


def test_open(*args, **kwargs):
    return Test()


open = test_open
try:
    print(analyze_log("测试路径"))
finally:
    open = original_open



'''测试是AI写的'''