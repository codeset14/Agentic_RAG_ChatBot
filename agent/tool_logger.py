import time

def run_tool_with_logging(tool_name, tool_fn, *args, **kwargs):
    start = time.time()
    result = tool_fn(*args, **kwargs)
    end = time.time()

    observation = {
        "tool_name": tool_name,
        "input": kwargs or args,
        "output": str(result)[:1000],
        "latency_ms": round((end - start) * 1000, 2),
    }

    return result, observation
