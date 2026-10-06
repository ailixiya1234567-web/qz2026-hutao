import json
def analyze_log(filepath: str) -> dict:
    result = {
        "total" :0,
        "by_level" : {},
        "by_user" : {},
        "last_error" : None,
    }

    #定义初始状态
    try:
        with open(filepath, "r", encoding="utf-8")as file: #以file为名字打开
            for line in file:      #逐行读取
                try:
                    log = json.loads(line)
                except json.JSONDecodeError:   #不得抛异常
                    continue
                result["total"]+=1
                level = log["level"]
                if level in result["by_level"]:    #查询,若有就加一，没有为初始，设为一
                    levels = result["by_level"]
                    levels[level] += 1
                else:
                    levels = result["by_level"]
                    levels[level] = 1
                user = log["user"]

                if user in result["by_user"]:
                    users = result["by_user"]  #同理
                    users[user] += 1
                else:
                    users = result["by_user"]
                    users[user] = 1
                if level == "ERROR":
                    result["last_error"] = log["message"]
    except FileNotFoundError:
        return result
    #不得抛异常要求，不得中断解析
    
    
    
    return result

