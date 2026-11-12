import json, os

with open(r'C:\Users\dresden\Documents\edge\analysis\videos_index.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

existing = set(os.listdir(r'C:\Users\dresden\Documents\edge\analysis'))

missing = []
for v in videos:
    if v['outfile'] not in existing:
        missing.append(v)

print(f'Total videos: {len(videos)}, Existing md files: {len(videos)-len(missing)}, Missing: {len(missing)}')
for m in missing:
    print(f"Missing: [{m['index']}] {m['outfile']}")
