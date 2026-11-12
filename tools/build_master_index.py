import os, json, re

with open(r'C:\Users\dresden\Documents\edge\analysis\videos_index.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

analysis_dir = r'C:\Users\dresden\Documents\edge\analysis'

index_lines = []
index_lines.append("# Master Index: Institutional SMC & Price Action Video Library")
index_lines.append("\nThis master index catalogs all **54 comprehensive video strategy breakdowns** extracted from the `imperial-research` video collection. Every breakdown includes Strategy & Concept Overview, Step-by-Step Setup Mechanics, Trade Execution Plan (Entry, Stop Loss, Invalidation, Take Profit), and Key Nuances/Traps.\n")
index_lines.append("| # | Video Title | Core Strategy / Concept | Analysis File |")
index_lines.append("| :--- | :--- | :--- | :--- |")

for v in videos:
    idx = v['index']
    title = v['filename'].replace('.mp4', '')
    outfile = v['outfile']
    filepath = os.path.join(analysis_dir, outfile)
    
    # Read first few lines or concept overview from the file
    concept = "Institutional SMC / Price Action Strategy"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            m = re.search(r'\*\*Core Concept:\*\*\s*(.+)', content)
            if not m:
                m = re.search(r'- Core concept:\s*(.+)', content)
            if m:
                concept = m.group(1).strip()
                # truncate concept if too long
                if len(concept) > 85:
                    concept = concept[:82] + "..."
    
    link = f"[{outfile}](file:///{filepath.replace(os.sep, '/')})"
    index_lines.append(f"| **{idx:02d}** | {title} | {concept} | {link} |")

master_index_content = "\n".join(index_lines)

with open(r'C:\Users\dresden\Documents\edge\MASTER_INDEX.md', 'w', encoding='utf-8') as out:
    out.write(master_index_content)

print("Generated MASTER_INDEX.md successfully!")
