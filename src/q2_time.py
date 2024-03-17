from typing import List, Tuple
from collections import defaultdict
import pandas as pd
import heapq
import emoji
import ujson


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    conteo = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            linea = ujson.loads(line)
            for emo in [i['emoji'] for i in emoji.emoji_list(linea["content"])]:
                conteo[emo] += 1

    return heapq.nlargest(10, conteo.items(), key=lambda x: x[1])
