#write program for round robin
#testcase 10,5,8
from collections import deque
def find(task,time):
    queue = deque(task)
    ids = deque(i + 1 for i in range(len(task)))
    run_count = 0

    while queue:
        current_time = queue.popleft()
        current_id = ids.popleft()

        run_time = min(current_time, time)
        print(f"Task {current_id} runs for {run_time} units")
        run_count += 1

        if current_time > time:
            queue.append(current_time - time)
            ids.append(current_id)

    print(f"Total runs taken {run_count}" )







task=[10,5,8]
time=4
find(task,time)