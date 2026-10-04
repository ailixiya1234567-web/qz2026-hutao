import json
def analyze_log(filepath: str) -> dict:
    result = {
        "total" :0,
        "by-level" : {},
        "by-user" : {},
        "last-error" : None,
    }


    try:
        with open("app.jsonl", "r", encoding="utf-8"):
            for line in file:
                pass
    except FileExistsError:
        return result
    
    
    
    
    return result

