import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the regex resilient to newlines
pattern = r'<a href="([^"]+)" class="blog-card">\s*<div class="blog-card-img"\s*style="([^"]+)">(.*?)</div>\s*<div class="blog-card-body">\s*<span class="tag-pill" style="([^"]+)">(.*?)</span>\s*<h3 class="blog-card-title">\s*(.*?)\s*</h3>\s*<p style="([^"]+)">(.*?)</p>\s*</div>\s*</a>'

def repl(match):
    href, img_style, img_content, tag_style, tag_content, title, p_style, p_content = match.groups()
    return f"""<details class="blog-card">
            <summary class="blog-card-summary">
              <div class="blog-card-img" style="{img_style}">{img_content}</div>
              <div class="blog-card-body-summary">
                <span class="tag-pill" style="{tag_style}">{tag_content}</span>
                <h3 class="blog-card-title">{title}</h3>
                <span class="chevron">▼</span>
              </div>
            </summary>
            <div class="blog-card-content">
              <p style="{p_style}">{p_content}</p>
              <a href="{href}" class="blog-link-btn">Read Full Article →</a>
            </div>
          </details>"""

new_html = re.sub(pattern, repl, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
