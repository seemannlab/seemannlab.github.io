import json
import re

with open('_data/publications.json', 'r', encoding='utf-8') as f:
    html = f.read()

publications = []
current_year = None

# Split by year headers
year_pattern = r'<h2[^>]*>(\d{4})</h2>'
pub_pattern = r'<div class="pub_container">(.*?)</div>\s*(?=<div|$)'

# Find all years
for year_match in re.finditer(year_pattern, html):
    current_year = int(year_match.group(1))
    year_pos = year_match.end()
    
    # Find publications after this year
    next_year = re.search(year_pattern, html[year_pos:])
    end_pos = year_pos + next_year.start() if next_year else len(html)
    
    year_section = html[year_pos:end_pos]
    
    for pub_match in re.finditer(pub_pattern, year_section, re.DOTALL):
        pub_html = pub_match.group(1)
        
        # Extract title
        title_match = re.search(r'<h3>(.*?)</h3>', pub_html)
        title = title_match.group(1).strip() if title_match else ""
        
        # Extract authors
        author_match = re.search(r'<p>\s*(.*?)\s*<cite>', pub_html, re.DOTALL)
        authors = author_match.group(1).strip() if author_match else ""
        authors = re.sub(r'<[^>]+>|&nbsp;|&#32;', ' ', authors).strip()
        
        # Extract citation
        cite_match = re.search(r'<cite>(.*?)</cite>', pub_html)
        citation = cite_match.group(1).strip() if cite_match else ""
        
        # Extract URLs
        pubmed_match = re.search(r'href="(https://[^"]*pubmed[^"]*)"', pub_html)
        paper_match = re.search(r'href="(https://doi\.org[^"]*)"', pub_html)
        
        publications.append({
            'year': current_year,
            'title': title,
            'authors': authors,
            'citation': citation,
            'pubmed_url': pubmed_match.group(1) if pubmed_match else None,
            'paper_url': paper_match.group(1) if paper_match else None
        })

with open('_data/publications_clean.json', 'w', encoding='utf-8') as f:
    json.dump(publications, f, indent=2, ensure_ascii=False)

print(f"✓ Converted {len(publications)} publications to publications_clean.json")
