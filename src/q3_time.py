from typing import List, Tuple
from collections import defaultdict
import pandas as pd
import heapq
import ujson
import re


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    conteo = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            linea = ujson.loads(line)
            for user in re.findall(r"@(\S+?) ", linea["content"]):
                conteo[user] += 1

    return heapq.nlargest(10, conteo.items(), key=lambda x: x[1])