#!/usr/bin/env python3
"""
Bundles ui.json + topics.json + keywords/*.json into dist/bundle.json.
Run locally or automatically via GitHub Actions on push to main.
"""
import json
import os
import glob

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

ui     = load(os.path.join(root, 'ui.json'))
topics = load(os.path.join(root, 'topics.json'))

keyword_files = sorted(glob.glob(os.path.join(root, 'keywords', '*.json')))
keywords = [load(f) for f in keyword_files]

bundle = {
    'meta': {
        'version': '1.0',
        'languages': ui['languages'],
    },
    'ui':       ui['strings'],
    'topics':   topics,
    'keywords': keywords,
}

out_dir = os.path.join(root, 'dist')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'bundle.json')

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(bundle, f, ensure_ascii=False, indent=2)

print(f"Bundled {len(keywords)} keywords into dist/bundle.json")
