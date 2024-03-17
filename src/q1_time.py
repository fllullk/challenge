from typing import List, Tuple
from datetime import datetime
import pandas as pd
from collections import defaultdict
import ujson
import heapq


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    conteo = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            conteo[datetime.fromisoformat(ujson.loads(line)["date"]).date()] += 1

    top_10_date = heapq.nlargest(10, conteo.items(), key=lambda x: x[1])
    conteos = {date: defaultdict(int) for date,_ in top_10_date}

    with open(file_path, 'r') as file:
        for line in file:
            date = datetime.fromisoformat(ujson.loads(line)["date"]).date()
            if date not in conteos:
                continue
            conteos[date][ujson.loads(line)["user"]["username"]] += 1
    sol = []
    for date, conteo in conteos.items():
        sol.append((date, max(conteo, key=conteo.get)))
    return sol
