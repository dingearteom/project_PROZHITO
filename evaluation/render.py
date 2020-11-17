from markup import mix
from ipymarkup import format_span_ascii_markup, format_span_box_markup
from IPython.display import display, HTML
from ipymarkup.palette import palette, PURPLE, RED, GREEN
from ipymarkup import show_span_box_markup, show_span_ascii_markup

def render_ascii_markup(*args, **kwargs):
    __attributes__ = ['right_markup', 'given_markup', 'File_Name', 'IPy']
    d = {}
    d['File_Name'] = 'compare.txt'
    d['IPy'] = False

    for key, value in zip(__attributes__, args):
        d[key] = value
    d.update(kwargs)

    if ('right_markup' in d and 'given_markup' in d):
        markup = mix(d['right_markup'], d['given_markup'])
    else:
        markup = d['right_markup']
    if (not d['IPy']):
        lines = format_span_ascii_markup(markup.text, markup.spans)
        with open(f'{d["File_Name"]}', 'w') as compare:
            for line in lines:
                compare.write(line + '\n')
    else:
        show_span_ascii_markup(markup.txt, markup.spans)

def render_box_markup(*args, **kwargs):
    __attributes__ = ['right_markup', 'given_markup', 'File_Name', 'IPy', 'palette']
    d = {}
    d['File_Name'] = 'compare.html'
    d['IPy'] = False

    for key, value in zip(__attributes__, args):
        d[key] = value
    d.update(kwargs)

    if ('right_markup' in d and 'given_markup' in d):
        markup = mix(d['right_markup'], d['given_markup'])
        if (not 'palette' in d):
            palette_ = palette(PER_FIRST=PURPLE, PER_BOTH=GREEN, PER_SECOND=RED)
        else:
            palette_ = d['palette']
    else:
        markup = d['right_markup']
        if (not 'palette' in d):
            palette_ = palette(PER=GREEN, LOC=PURPLE)
        else:
            palette_ = d['palette']

    if (not d['IPy']):
        lines = format_span_box_markup(markup.text, markup.spans, palette=palette_)
        html = HTML(''.join(lines))
        with open(f"{d['File_Name']}", 'w') as compare:
            compare.write(html.data)
    else:
        show_span_box_markup(markup.text, markup.spans, palette=palette_)

