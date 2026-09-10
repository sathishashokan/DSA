# def insert_at_bottom(stack, temp):
#     if not stack:
#         stack.append(temp)
#         return
#
#     val = stack.pop()
#     insert_at_bottom(stack, temp)
#
#     stack.append(val)
#
#
# def reverse_stack(stack):
#     if stack:
#         temp = stack.pop()
#         reverse_stack(stack)
#         insert_at_bottom(stack, temp)


# def minimumDeletions(nums):
#     if len(nums) == 1:
#         return 1
#
#     small = 0
#     large = 0
#
#     for i, num in enumerate(nums):
#         if num > nums[large]:
#             large = i
#         if num < nums[small]:
#             small = i
#
#     if small < large:
#         res1 = large + 1
#         res2 = len(nums) - small
#         small += 1
#         large = len(nums) - large
#     else:
#         res1 = small + 1
#         res2 = len(nums) - large
#         large += 1
#         small = len(nums) - small
#
#     res3 = small + large
#
#
#     return min(res1, res2, res3)
#
# nums = [2,10,7,5,4,1,8,6]
# nums = [0,-4,19,1,8,-2,-3,5]
# print(minimumDeletions(nums))

# arr1 = [4,1,3,5]
# print(selection_main(arr1))
# print(arr1)
# print(total)
# stk = [4,3,1,2]
# stk1 = [10, 20, -5, 7, 15]
# reverse_stack(stk)
# print(stk)
import math


# def solveSudoku(board):
#     rows = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]
#     empty = []
#
#     # Initialize sets
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == '.':
#                 empty.append((row, col))
#             else:
#                 num = board[row][col]
#                 box = (row // 3) * 3 + (col // 3)
#
#                 rows[row].add(num)
#                 cols[col].add(num)
#                 boxes[box].add(num)
#     return empty

    # def solve():
    #     for row in range(9):
    #         for col in range(9):
    #             if board[row][col] == '.':
    #                 for num in '123456789':
    #                     if is_valid(row, col, num):
    #                         board[row][col] = num
    #                         if solve():
    #                             return True
    #                         board[row][col] = '.'
    #                 return False
    #     return True

    # def is_valid(row, col, num):
    #     for i in range(9):
    #         if board[row][i] == num or board[i][col] == num:
    #             return False
    #     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    #     for i in range(start_row, start_row + 3):
    #         for j in range(start_col, start_col + 3):
    #             if board[i][j] == num:
    #                 return False
    #     return True
# board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]

# print(solveSudoku(board))

# board = [
#  ["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]
# ]

# board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
#
# print(isValidSudoku(board))
# for row in board:
#     print(row)

# def helper(p, up):
#     if not up:
#         res = [p]
#         return res
#
#     left = helper(p + [up[0]], up[1:])
#     right = helper(p, up[1:])
#     left.extend(right)
#     return left
import asyncio
import time
import random

# Store all events in a timeline for later analysis
async_timeline_events = []
# Keep track of background tasks we'll gather at the end
tasks = []

# Capture the start time to calculate relative timestamps
initial_timestamp = time.monotonic()


def log_event(timeline, task, event):
    """
    Log an event with timestamp to visualize when operations start and end
    You can simply ignore this this does not serve any pupose in the pipeline.
    Args:
        timeline: List to append the event to
        task: Name/ID of the task
        event: Description of what happened (e.g., START or END)
    """
    timestamp = time.monotonic() - initial_timestamp  # Calculate time since start
    timeline.append({
        "task": task,
        "event": event,
        "timestamp": timestamp,
    })
    print(f"[{timestamp:.2f}] {event}: {task}")


async def async_db_operation(step):
    """
    Simulate a database write operation (like saving analytics or logs)

    In real applications, this would be writing data to a database,
    which is I/O-bound and benefits from asynchronous execution.
    """
    task_id = f"log_{step}"
    log_event(async_timeline_events, task_id, "START")  # just logging time
    # Simulate variable database operation time
    await asyncio.sleep(random.uniform(0.3, 3.0))
    log_event(async_timeline_events, task_id, "END")  # just logging time


async def async_llm_call(prompt):
    """
    Simulate a call to a Large Language Model API

    In real applications, this would be a network request to an API like
    OpenAI, Anthropic, or a self-hosted LLM service.
    """
    task_id = f"llm_{prompt[:10]}"
    log_event(async_timeline_events, task_id, "START")  # just logging time
    # LLM calls often take longer than other API calls
    await asyncio.sleep(random.uniform(0.5, 3.2))
    log_event(async_timeline_events, task_id, "END")  # just logging time
    return f"LLM result: {prompt}"


async def async_http_call(endpoint):
    """
    Simulate an HTTP request to an external API

    In real applications, this could be fetching data from a REST API,
    microservice, or other web service.
    """
    task_id = f"http_{endpoint.replace('/', '')}"
    log_event(async_timeline_events, task_id, "START")  # just logging time
    # Simulate variable network latency
    await asyncio.sleep(random.uniform(0.4, 4.0))
    log_event(async_timeline_events, task_id, "END")  # just logging time
    return f"HTTP result from {endpoint}"


async def run_async_pipeline():
    """
    Main workflow that coordinates the execution of different async operations

    This demonstrates both:
    1. Dependent tasks (using 'await') - where we need results immediately
    2. Background tasks (using create_task) - where we can fire and forget
    """
    log_event(async_timeline_events, "main_pipeline", "START_PIPELINE")

    # DEPENDENT TASK: We need the LLM result before proceeding
    llm_result = await async_llm_call("What's the user intent?")
    # BACKGROUND TASK: Log the result to the database, but don't wait for it
    tasks.append(asyncio.create_task(async_db_operation("llm_result")))

    # DEPENDENT TASK: We need this HTTP result for our business logic
    http1 = await async_http_call("/api/data")
    # BACKGROUND TASK: Log this API call, but don't block on it
    tasks.append(asyncio.create_task(async_db_operation("http1")))

    # DEPENDENT TASK: We need this data too before proceeding
    http2 = await async_http_call("/api/details")
    # BACKGROUND TASK: Another non-blocking logging operation
    tasks.append(asyncio.create_task(async_db_operation("http2")))

    # DEPENDENT TASK: Generate a summary using the LLM with collected data
    summary = await async_llm_call("Summarize everything")
    # BACKGROUND TASK: Log the summary generation
    tasks.append(asyncio.create_task(async_db_operation("summary")))

    log_event(async_timeline_events, "main_pipeline", "END_PIPELINE")

    # Wait for all background tasks to complete before exiting
    # This ensures all logging operations finish properly
    # This will run without gathering all tasks as well, you can try
    await asyncio.gather(*tasks)


# Fix for running asyncio in environments like Jupyter notebooks
import nest_asyncio

nest_asyncio.apply()

# Reset the timer before starting
initial_timestamp = time.monotonic()

print("\n--- Running Async Pipeline ---\n")
# Run the main async workflow
asyncio.run(run_async_pipeline())
print(async_timeline_events)
print(tasks)
