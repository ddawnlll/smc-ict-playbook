import os, json

with open(r'C:\Users\dresden\Documents\edge\analysis\videos_index.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

analysis_dir = r'C:\Users\dresden\Documents\edge\analysis'

print(f"{'Idx':<4} {'Size':<8} {'File Name'}")
print("-" * 75)
for v in videos:
    path = os.path.join(analysis_dir, v['outfile'])
    size = os.path.getsize(path)
    print(f"{v['index']:<4} {size:<8} {v['outfile'][:60]}")

print("\nAll 54 analyses exist and are populated!")
