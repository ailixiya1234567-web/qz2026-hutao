from main import analyze_log


print(f"正常json日志:{analyze_log('q1/app.jsonl')}")




print(f"不正常json日志:{analyze_log('q1/empty.jsonl')}")

