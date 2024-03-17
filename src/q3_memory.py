from typing import List, Tuple
import pandas as pd
import ujson


def read_jsonl_fast(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(ujson.loads(line))
    return pd.DataFrame(data)

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    data = read_jsonl_fast(file_path)
    matches = data["content"].str.extractall(r"@(\S+?) ")
    sol = [(row[0], row['count']) for row in matches[0].value_counts().nlargest(10).reset_index().to_dict('records')]
    return sol