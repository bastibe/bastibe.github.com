import pathlib
import re


for org_file in pathlib.Path('posts').glob('*.org'):
    with org_file.open('rt', errors='ignore') as org:
        with org_file.with_suffix('.md').open('wt') as md:
            md.write('---\n')
            in_header = True
            in_html_export = False
            for line in org:
                if not line.startswith('#+') and in_header:
                    in_header = False
                    md.write('---\n')
                line = re.sub(r"^#\+(title|date|description|filetags): ?", lambda s: f'{s.group(1).lower()}: ', line,
                              flags=re.IGNORECASE)
                if line.startswith('#+begin_export html'):
                    in_html_export = True
                    continue
                if line.startswith('#+end_export') and in_html_export:
                    in_html_export = False
                    continue
                if in_html_export:
                    md.write(line)
                    continue
                line = re.sub(r"^\*+", lambda s: '#'*len(s[0]), line)
                line = re.sub(r"^: ", "    ", line)
                line = re.sub(r"\*[^*]+\*", lambda s: '**'+s[0].strip('*')+'**', line)
                line = re.sub(r"\/[^*]+\/", lambda s: '_'+s[0].strip('/')+'_', line)
                line = re.sub(r"^#\+begin_src ?", "```", line)
                line = re.sub(r"^#\+end_src", "```", line)
                line = re.sub(r"\\\\$", "  ", line)
                line = re.sub(r"~[^~]+~", lambda s: '`'+s[0].strip('~')+'`', line)
                line = re.sub(r"\[\[(.+?)\]\[(.*?)\]\]", lambda s: f'[{s.group(2)}]({s.group(1)})', line)
                line = re.sub(r"\[\[(.+?)\]\]", lambda s: f'![{pathlib.Path(s.group(1)).stem}]({s.group(1)})', line)
                line = re.sub(r"<([0-9]{4})-([0-9]{1,2})-([0-9]{1,2}) [0-9]{1,2}:[0-9]{1,2}>", 
                              lambda s: f'{s.group(1)}-{int(s.group(2)):02d}-{int(s.group(3)):02d}', line)
                md.write(line)