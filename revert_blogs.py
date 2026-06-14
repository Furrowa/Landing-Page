import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find details blocks
pattern = r'<details class="blog-card">\s*<summary class="blog-card-summary">\s*<div class="blog-card-img" style="([^"]+)">(.*?)</div>\s*<div class="blog-card-body-summary">\s*<span class="tag-pill" style="([^"]+)">(.*?)</span>\s*<h3 class="blog-card-title">(.*?)</h3>\s*<span class="chevron">▼</span>\s*</div>\s*</summary>\s*<div class="blog-card-content">\s*<p style="([^"]+)">(.*?)</p>\s*<a href="([^"]+)" class="blog-link-btn">Read Full Article →</a>\s*</div>\s*</details>'

def repl(match):
    img_style, img_content, tag_style, tag_content, title, p_style, p_content, href = match.groups()
    return f"""<a href="{href}" class="blog-card">
            <div class="blog-card-img" style="{img_style}">{img_content}</div>
            <div class="blog-card-body">
              <span class="tag-pill" style="{tag_style}">{tag_content}</span>
              <h3 class="blog-card-title">{title}</h3>
              <p style="{p_style}">{p_content}</p>
            </div>
          </a>"""

new_html = re.sub(pattern, repl, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
