import os
import re
from pathlib import Path
from urllib.parse import quote

docs_path = Path('C:/PROGRAMMING/PROJECTS/NosFuimosdeFinca/docs/04-system-modeling')

def fix_image_links(path):
    content = path.read_text('utf-8')
    original = content
    
    # 1. Fix [[Image Name.png]] format
    # Example: ![[Html → Body-3.png]] or ![[PROJECTS/.../Html → Body-1.png]]
    # We want to extract just the basename.
    def wikilink_repl(match):
        full_path = match.group(1)
        basename = os.path.basename(full_path)
        encoded = quote(basename)
        return f'![{basename}]({encoded})'
    
    content = re.sub(r'!\[\[(.*?)\]\]', wikilink_repl, content)
    
    # 2. Fix ![alt](<Image Name.png>) format, and any trailing ).png)
    # Example: ![Gestión de Fincas - Hub (Wireframe Desktop).png](<Gestión de Fincas - Hub (Wireframe Desktop).png>).png)
    def standard_repl(match):
        alt = match.group(1)
        url = match.group(2)
        # If the URL is wrapped in <>, remove them
        if url.startswith('<') and url.endswith('>'):
            url = url[1:-1]
        
        basename = os.path.basename(url)
        encoded = quote(basename)
        return f'![{alt}]({encoded})'
    
    # regex matches ![alt](url) optionally followed by .png) or similar garbage
    # We use a greedy match for alt, but non-greedy for url up to the first ) that seems to close the url
    # Actually, the angle brackets make it easier: \!\[(.*?)\]\(\<(.*?)\>\)(?:\.png\))?
    content = re.sub(r'!\[(.*?)\]\(\<(.*?)\>\)(?:\.png\))?', standard_repl, content)
    
    if content != original:
        path.write_text(content, 'utf-8')
        print(f"Fixed: {path.relative_to(docs_path)}")

for root, dirs, files in os.walk(docs_path):
    for f in files:
        if f.endswith('.md'):
            fix_image_links(Path(root) / f)

print("Done")
