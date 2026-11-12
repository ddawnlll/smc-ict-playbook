import json

with open(r'C:\Users\dresden\Documents\edge\analysis\videos_index.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

groups = [(1, 11), (12, 22), (23, 33), (34, 44), (45, 54)]

for g_idx, (start, end) in enumerate(groups, 1):
    sub = [v for v in videos if start <= v['index'] <= end]
    print(f"=== GROUP {g_idx}: {len(sub)} videos ({start} to {end}) ===")
    for v in sub:
        print(f"  [{v['index']:02d}] {v['filename']}")
