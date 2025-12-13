import pathlib
import re


for org_file in pathlib.Path('posts').glob('*.org'):
    with org_file.open('rt', errors='ignore') as org:
        with org_file.with_suffix('.md').open('wt') as md:
            md.write('---\n')
            in_header = True
            in_html_export = False
            in_source = False
            in_quote = False
            in_math = False
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
                if line.startswith('|-') and line.endswith('-|\n'):
                    line = re.sub(r"^\|-", "| ", line)
                    line = re.sub(r"-\|$", " |", line)
                    line = re.sub(r"-\+-", " | ", line)
                line = re.sub(r"^\s*#\+begin_src ?", "```", line)
                line = re.sub(r"^\s*#\+end_src", "```", line)
                line = re.sub(r"^\s*#\+begin_example", "```", line)
                line = re.sub(r"^\s*#\+end_example", "```", line)
                if line.startswith('#+begin_quote'):
                    in_quote = True
                    continue
                if line.startswith('#+end_quote'):
                    in_quote = False
                    continue
                if line.strip().startswith('```'):
                    in_source = not in_source
                if in_source:
                    md.write(line)
                    continue
                if line.startswith('$$'):
                    in_math = not in_math
                if in_math:
                    md.write(line)
                    continue
                line = re.sub(r"^\*+(?= )", lambda s: '#'*len(s[0]), line)
                line = re.sub(r"^: ", "    ", line)
                line = re.sub(r"(?<=\W)\*\w[^\*]+\*", lambda s: '**'+s[0].strip('*')+'**', line)
                line = re.sub(r"(?<=\W)\/\S[^\/]+\/(?=\W)", lambda s: '_'+s[0].strip('/')+'_', line)
                line = re.sub(r"(?<!^)\[fn:([^\]]+)\]", lambda s: f'[^{s.group(1)}]', line)
                line = re.sub(r"^\[fn:([^\]]+)\]", lambda s: f'[^{s.group(1)}]:', line)
                line = re.sub(r"\\\\$", "  ", line)
                line = re.sub(r"(?<=\W)~\S[^~]*~", lambda s: '`'+s[0].strip('~')+'`', line)
                line = re.sub(r"(?<=\W)=\S[^=]*=", lambda s: '`'+s[0].strip('=')+'`', line)
                line = re.sub(r"(?<=\W)\+\S[^\+]+\+(?=\W)", lambda s: '~~'+s[0].strip('+')+'~~', line)
                line = re.sub(r"\[\[(.+?)\]\[(.*?)\]\]", lambda s: f'[{s.group(2)}]({s.group(1)})', line)
                line = re.sub(r"\[\[(.+?)\]\]", lambda s: f'![{pathlib.Path(s.group(1)).stem}]({s.group(1)})', line)
                line = re.sub(r"<([0-9]{4})-([0-9]{1,2})-([0-9]{1,2}) ([0-9]{1,2}):([0-9]{1,2})>", 
                              lambda s: f'{s.group(1)}-{int(s.group(2)):02d}-{int(s.group(3)):02d} {int(s.group(4)):02d}:{int(s.group(5)):02d}', line)
                if in_quote:
                    line = '> ' + line
                md.write(line)