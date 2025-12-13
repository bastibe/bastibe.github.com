import pathlib
import time
import tomllib
import collections

import mistune

def main():
    root_path = pathlib.Path(__file__).parent
    config_path = root_path / 'bsbr.toml'
    config = tomllib.loads(config_path.read_text(encoding='utf-8'))
    drafts_path = root_path / config['drafts_folder']
    posts_path = root_path / config['posts_folder']
    base_url = config['base_url']    

    # Create a Markdown parser
    markdown_parser = mistune.create_markdown()

    # Iterate through all files in the drafts directory
    Post = collections.namedtuple('Post', ['path', 'metadata', 'body'])
    posts = []
    for file in posts_path.glob('*.md'):
        markdown = file.read_text(encoding='utf-8')
        front_matter, markdown = split_frontmatter(markdown)
        metadata = parse_frontmatter(front_matter)
        page_url = f"{base_url}/posts/{file.stem}.html"
        body = markdown_parser(markdown)
        html = assemble_post(config, metadata, page_url, body, base_url)
        output_path = root_path / f"{file.stem}.html"
        output_path.write_text(html, encoding='utf-8')
        posts.append(Post(output_path, metadata, body))
    posts = sorted(posts, key=lambda post: post.metadata['date'], reverse=True)
    
    # create archive.html page
    html = assemble_archive(config, posts, base_url)
    archive_path = root_path / 'archive.html'
    archive_path.write_text(html, encoding='utf-8')
    
    # create index.html page
    html = assemble_index(config, posts, base_url, num_posts=config['index_num_posts'])
    index_path = root_path / 'index.html'
    index_path.write_text(html, encoding='utf-8')

def split_frontmatter(text):
    front_matter_start = text.find('---')
    front_matter_end = text.find('---', front_matter_start + 3)
    front_matter = text[front_matter_start + 3:front_matter_end]
    markdown = text[front_matter_end + 3:]
    return front_matter, markdown


def parse_frontmatter(text):
    frontmatter = {}
    for line in text.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value
    return frontmatter


def assemble_post(config, metadata, page_url, body, base_url, is_index=False):
    date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
    tags = [tag.strip() for tag in metadata['filetags'].split(',')]
    taglist = ', '.join(f'<a href="{base_url}/tag-{tag}.html">{tag}</a>' for tag in tags)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
{f'<meta name="description" content="{metadata["description"]}">' if 'description' in metadata else ''}
<link rel="alternate"
      type="application/rss+xml"
      href="{config['base_url']}/rss.xml"
      title="RSS feed for {config['base_url']}">
<title>{metadata['title']}</title>
{config['site_meta']}
</head>
<body>
{config['page_header']}
<div id="content">
{f'<div class="post-date">{date}</div>' if not is_index else ''}
{f'<h1 class="post-title"><a href="{page_url}">{metadata["title"]}</a></h1>' if not is_index else ''}
{body}
<div class="taglist"><a href="{base_url}/tags.html">Tags</a>: {taglist}</div>
{f'<div id="comments">\n{config["page_comments"]}\n</div>' if not is_index else ''}
</div>
<div id="postamble" class="status">
{config['page_footer']}
</div>
</body>
</html>
"""


def assemble_archive(config, posts, base_url):
    content = ['<h1>Archive</h1>']
    for post_path, metadata, body in posts:
        post_url = f"{base_url}/posts/{post_path.stem}.html"
        date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
        content.append(f'<div class="post-date">{date}</div><h2 class="post-title"><a href="{post_url}">{metadata["title"]}</a></h2>')
    html = '\n'.join(content)

    return assemble_post(config, {'title': 'Archive', 'date': time.strftime('%Y-%m-%d'), 'filetags': ''}, 
                         f"{base_url}/archive.html", html, base_url, is_index=True)


def assemble_index(config, posts, base_url, num_posts=5):
    content = []
    for post_path, metadata, body in posts[:num_posts]:
        post_url = f"{base_url}/posts/{post_path.stem}.html"
        date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
        content.append(f"""
<div class="post-date">{date}</div><h2 class="post-title"><a href="{post_url}">{metadata["title"]}</a></h2>
{body}
""")
    html = '\n'.join(content)

    return assemble_post(config, {'title': 'Home', 'date': time.strftime('%Y-%m-%d'), 'filetags': ''}, 
                         f"{base_url}/index.html", html, base_url, is_index=True)


if __name__ == "__main__":
    main()