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

    except FileNotFoundError:
        return result
    
    
    
    
    return result

