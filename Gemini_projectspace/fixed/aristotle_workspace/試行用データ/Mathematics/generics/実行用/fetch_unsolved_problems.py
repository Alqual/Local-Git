import urllib.request
import json
import os
import re

def fetch_wikipedia_data():
    url = "https://en.wikipedia.org/w/api.php?action=parse&page=List_of_unsolved_problems_in_mathematics&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    print("Fetching data from Wikipedia API...")
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    return data

def extract_h3_lists(html_content):
    # A simple regex to find <h3> associated problems in Wikipedia's HTML output
    # This is a very basic programmatic extraction for trace purposes.
    sections = {}
    current_section = "General"
    
    # Split by h2 or h3 to get sections
    parts = re.split(r'<h[23][^>]*><span[^>]*id="([^"]+)"[^>]*>(.*?)</span>', html_content)
    
    # parts format: [html_before, id1, title1, html_between, id2, title2, ...]
    if len(parts) > 0:
        for i in range(1, len(parts), 3):
            section_id = parts[i]
            section_title = parts[i+1]
            section_html = parts[i+2]
            
            # Find list items
            items = re.findall(r'<li>(.*?)</li>', section_html, re.DOTALL)
            # Clean HTML tags from items
            clean_items = [re.sub(r'<[^>]+>', '', item).strip() for item in items]
            clean_items = [item for item in clean_items if item] # remove empty
            
            if clean_items:
                # Strip edit links from title
                clean_title = re.sub(r'<[^>]+>', '', section_title).strip()
                sections[clean_title] = clean_items

    return sections

def main():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_file = os.path.join(base_dir, "raw_wikipedia_unsolved_problems.json")
    parsed_data_file = os.path.join(base_dir, "parsed_unsolved_problems.json")
    
    # Fetch raw data
    data = fetch_wikipedia_data()
    
    # Save raw trace
    with open(raw_data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved raw Wikipedia JSON to {raw_data_file}")
    
    # Parse and save structured trace
    html_content = data['parse']['text']['*']
    structured_data = extract_h3_lists(html_content)
    
    with open(parsed_data_file, 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, ensure_ascii=False, indent=2)
    print(f"Saved parsed structured JSON to {parsed_data_file}")
    
    # Summarize what we found
    print("\nSummary of extracted data:")
    for section, items in structured_data.items():
        print(f" - {section}: {len(items)} problems found")

if __name__ == "__main__":
    main()
