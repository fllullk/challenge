from typing import List, Tuple
import pandas as pd
import emoji
import ujson


def read_jsonl_fast(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(ujson.loads(line))
    return pd.DataFrame(data)

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    data = read_jsonl_fast(file_path)
    matches = pd.Series([i['emoji'] for i in emoji.emoji_list(data["content"].str.cat())])
    sol = [(row['index'], row['count']) for row in matches.value_counts().nlargest(10).reset_index().to_dict('records')]
    return sol