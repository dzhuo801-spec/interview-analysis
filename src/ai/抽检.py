import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
lab = pd.read_csv(os.path.join(BASE, "output", "访谈标签表.csv"))
s = lab.sample(10, random_state=42).sort_values("id")

for _, r in s.iterrows():
    print(r["id"], "|", r["text"])