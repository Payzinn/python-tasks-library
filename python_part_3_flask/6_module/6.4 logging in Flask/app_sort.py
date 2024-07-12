import heapq
import json
import logging
from typing import List
import time
from typing import Callable, Any, Optional
import functools

from flask import Flask, request

app = Flask(__name__)

logger = logging.getLogger("sort")

def timer_with_precision(_func: Optional[Callable] = None) -> Callable:
    def timer_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            run = end - start
            logger.debug(f'Функция {func.__name__} работала {run}')
            return result
        return wrapped_func
    if _func is None:
        return timer_decorator
    else:
        return timer_decorator(_func)

@timer_with_precision()
def bubble_sort(array: List[int]) -> List[int]:
   n = len(array)

   for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

   return array

@timer_with_precision()
def tim_sort(array: List[int]) -> List[int]:
   array.sort()
   return array

@timer_with_precision()
def heap_sort(array: List[int]) -> List[int]:
   data = []

   for val in array:
       heapq.heappush(data, val)

   return [heapq.heappop(data) for _ in range(len(data))]

algorithms = {
   "bubble": bubble_sort,
   "tim": tim_sort,
   "heap": heap_sort,
}


@app.route("/<algorithm_name>/", methods=["POST"])
def sort_endpoint(algorithm_name: str):
   if algorithm_name not in algorithms:
       return f"Bad algorithm name, acceptable values are {algorithms.keys()}", 400

   form_data = request.get_data(as_text=True)

   array = json.loads(form_data)

   result = algorithms[algorithm_name](array)

   return json.dumps(result)

if __name__ == "__main__":
   logging.basicConfig(level=logging.DEBUG)
   logger.info("Started sort server")
   app.config["WTF_CSRF_ENABLED"] = False
   app.run(debug=True)