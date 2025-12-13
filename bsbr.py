import pathlib
import time
import tomllib
import collections

import mistune
import pygments
import pygments.lexers
import pygments.formatters.html

class CodeHighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = pygments.lexers.get_lexer_by_name(info, stripall=True)
            formatter = pygments.formatters.html.HtmlFormatter()
            return pygments.highlight(code, lexer, formatter)
        return '<pre><code>' + mistune.escape(code) + '</code></pre>'


Post = collections.namedtuple('Post', ['path', 'metadata', 'body'])


def main():
    root_path = pathlib.Path(__file__).parent
    config_path = root_path / 'bsbr.toml'
    config = tomllib.loads(config_path.read_text(encoding='utf-8'))
    drafts_path = root_path / config['drafts_folder']
    posts_path = root_path / config['posts_folder']
    base_url = config['base_url']

    posts = collect_posts(config, posts_path, root_path, base_url)
    drafts = collect_posts(config, drafts_path, root_path, base_url)

    # create post pages
    for path, metadata, body in posts + drafts:
        page_url = f"{base_url}/{path.stem}.html"
        html = assemble_post(config, metadata, page_url, body, base_url)
        output_path = root_path / f"{path.stem}.html"
        output_path.write_text(html, encoding='utf-8')
        
    # create archive.html page
    html = assemble_archive(config, posts, base_url)
    archive_path = root_path / 'archive.html'
    archive_path.write_text(html, encoding='utf-8')
    
    # create index.html page
    html = assemble_index(config, posts[:config['index_num_posts']], base_url)
    index_path = root_path / 'index.html'
    index_path.write_text(html, encoding='utf-8')

    # create rss.xml file
    xml = assemble_rss(config, posts, base_url)
    rss_path = root_path / 'rss.xml'
    rss_path.write_text(xml, encoding='utf-8')

    # create tag pages
    tags = sort_posts_by_tag(posts)
    for tag, tagged_posts in tags:
        html = assemble_index(config, tagged_posts, base_url, title=f'Posts tagged "{tag}"')
        tag_path = root_path / f'tag-{tag}.html'
        tag_path.write_text(html, encoding='utf-8')
    html = assemble_tag_archive(config, tags, base_url)
    tags_path = root_path / 'tags.html'
    tags_path.write_text(html, encoding='utf-8')


def collect_posts(config, posts_path, root_path, base_url):
    markdown_parser = mistune.create_markdown(renderer=CodeHighlightRenderer(), escape=False, plugins=['footnotes'])
    posts = []
    for file in posts_path.glob('*.md'):
        text = file.read_text(encoding='utf-8')
        metadata, markdown = parse_frontmatter(text)
        body = markdown_parser(markdown)
        posts.append(Post(file, metadata, body))
    posts = sorted(posts, key=lambda post: post.metadata['date'], reverse=True)
    return posts


def parse_frontmatter(text):
    frontmatter = {}
    for line in text.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value
        if line.strip() == '---' and frontmatter:
            break
    front_matter_end = text.find('---', text.find('---') + 3)
    markdown = text[front_matter_end + 3:]
    return frontmatter, markdown


def assemble_post(config, metadata, page_url, body, base_url, is_index=False):
    date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
    tags = [tag.strip() for tag in metadata['filetags'].split(' ')]
    taglist = ', '.join(f'<a href="{base_url}/tag-{tag}.html">{tag}</a>' for tag in tags if tag != 'nocomments')
    no_comments = 'nocomments' in tags

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
<div class="taglist"><a href="{base_url}/tags.html">Tags</a>: {taglist or 'none'}</div>
{f'<div id="comments">\n{config["page_comments"]}\n</div>' if (not is_index) and (not no_comments) else ''}
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
        post_url = f"/{post_path.stem}.html"
        date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
        content.append(f'<div class="post-date">{date}</div><h2 class="post-title"><a href="{post_url}">{metadata["title"]}</a></h2>')
    html = '\n'.join(content)

    return assemble_post(config, {'title': 'Archive', 'date': time.strftime('%Y-%m-%d'), 'filetags': ''}, 
                         f"{base_url}/archive.html", html, base_url, is_index=True)


def assemble_index(config, posts, base_url, title=''):
    content = []
    if title:
        content.append(f'<h1>{title}</h1>')
    for post_path, metadata, body in posts:
        post_url = f"{base_url}/{post_path.stem}.html"
        date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
        content.append(f"""
<div class="post-date">{date}</div><h2 class="post-title"><a href="{post_url}">{metadata["title"]}</a></h2>
{body}
""")
    html = '\n'.join(content)

    return assemble_post(config, {'title': 'Home', 'date': time.strftime('%Y-%m-%d'), 'filetags': ''}, 
                         f"{base_url}/index.html", html, base_url, is_index=True)


def assemble_rss(config, posts, base_url):
    items = []
    for post_path, metadata, body in posts:
        post_url = f"{base_url}/{post_path.stem}.html"
        pub_date = time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.strptime(metadata['date'], '%Y-%m-%d'))
        items.append(f"""<item>
<title>{metadata['title']}</title>
<description><![CDATA[{body}]]></description>
<category>{metadata['filetags']}</category>
<link>{post_url}</link>
<guid>{post_url}</guid>
<pubDate>{pub_date}</pubDate>
</item>""")
    rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>{config['site_title']}</title>
<description>{config['site_title']}</description>
<link>{config['base_url']}</link>
<lastBuildDate>{time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime())}</lastBuildDate>
{'\n'.join(items)}
</channel>
</rss>"""
    return rss


def sort_posts_by_tag(posts):
    tag_dict = collections.defaultdict(list)
    for post in posts:
        tags = [tag.strip() for tag in post.metadata['filetags'].split(' ')]
        for tag in tags:
            if tag not in tag_dict:
                tag_dict[tag] = []
            tag_dict[tag].append(post)
    for tag in tag_dict:
        tag_dict[tag] = sorted(tag_dict[tag], key=lambda post: post.metadata['date'], reverse=False)
    return sorted(tag_dict.items())


def assemble_tag_archive(config, tagged_posts, base_url):
    content = ['<h1 class="title">Tags</h1>']
    for tag, posts in tagged_posts:
        content.append(f'<h1 class="tags-title">Posts tagged "{tag}":</h1>')
        for post_path, metadata, body in posts:
            post_url = f"{base_url}/{post_path.stem}.html"
            date = time.strftime(config['date_format'], time.strptime(metadata['date'], '%Y-%m-%d'))
            content.append(f'<div class="post-date">{date}</div><h2 class="post-title"><a href="{post_url}">{metadata["title"]}</a></h2>')
    html = '\n'.join(content)

    return assemble_post(config, {'title': 'Archive', 'date': time.strftime('%Y-%m-%d'), 'filetags': ''}, 
                         f"{base_url}/archive.html", html, base_url, is_index=True)


if __name__ == "__main__":
    main()