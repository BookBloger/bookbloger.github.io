import os
import glob
from datetime import datetime

SITE_URL = "https://bookbloger.github.io"
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_FILE = os.path.join(REPO_DIR, "sitemap.xml")
ROBOTS_FILE = os.path.join(REPO_DIR, "robots.txt")

def generate_sitemap_and_robots():
    now_iso = datetime.now().strftime("%Y-%m-%d")
    
    # Priority mapping
    priority_map = {
        "index.html": ("1.0", "daily"),
        "pricing-table.html": ("0.95", "daily"),
        "campaign-squad.html": ("0.95", "daily"),
        "3d.html": ("0.9", "daily"),
        "top-posts.html": ("0.9", "daily"),
        "top-100-posts.html": ("0.9", "daily"),
    }
    
    html_files = sorted(glob.glob(f"{REPO_DIR}/**/*.html", recursive=True))
    
    urls = []
    for fpath in html_files:
        rel = os.path.relpath(fpath, REPO_DIR)
        
        # Determine URL
        if rel == "index.html":
            loc = f"{SITE_URL}/"
            prio, freq = priority_map["index.html"]
        elif rel in priority_map:
            loc = f"{SITE_URL}/{rel}"
            prio, freq = priority_map[rel]
        else:
            loc = f"{SITE_URL}/{rel}"
            prio, freq = ("0.8", "weekly")
            
        urls.append({
            "loc": loc,
            "lastmod": now_iso,
            "changefreq": freq,
            "priority": prio
        })
        
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
    ]
    
    for u in urls:
        xml_lines.append("  <url>")
        xml_lines.append(f"    <loc>{u['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        xml_lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        xml_lines.append(f"    <priority>{u['priority']}</priority>")
        xml_lines.append("  </url>")
        
    xml_lines.append("</urlset>")
    
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
        
    print(f"Generated {SITEMAP_FILE} with exactly {len(urls)} URLs matching 100% of HTML files on disk.")
    
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(ROBOTS_FILE, "w", encoding="utf-8") as f:
        f.write(robots_content)

if __name__ == "__main__":
    generate_sitemap_and_robots()
