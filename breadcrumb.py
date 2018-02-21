import re

def acronymize(s):
    WORDS_TO_IGNORE = [
        'the', 'of', 'in', 'from', 'by', 'with',
        'and', 'or', 'for', 'to', 'at', 'a'
    ]
    if len(s) > 30:
        s = ''.join(w[0].upper() for w in s.split('-')
                    if w not in WORDS_TO_IGNORE)
    return s

def to_label(path):
    if not path:
        path = 'home'
    path = path.split('/')[-1].split('?')[0].split('#')[0].split('.')[0]
    path = acronymize(path)
    path = path.replace('-', ' ')
    return path.upper()

def to_link(path = None):
    href = '/' + path + '/' if path else "/"
    return '<a href="{}">{}</a>'.format(href, to_label(path))

def to_active(path):
    return '<span class="active">{}</span>'.format(to_label(path))

def generate_bc(url, separator):
    url = re.sub(r'\Ahttps?://', '', url).rstrip('/')
    paths = url.split('/')[1:]
    if paths and paths[-1].startswith('index.'):
        paths.pop(-1)
    for i in range(1, len(paths)):
        paths[i] = '/'.join(paths[i - 1:i + 1])
    paths.insert(0, None)
    htmls = list(map(to_link, paths[:-1])) + [to_active(paths[-1])]
    return separator.join(htmls)


if __name__ == '__main__':
    url = "https://www.linkedin.com/in/giacomosorbi"
    print(generate_bc(url, ' : '))
    url = "www.agcpartners.co.uk/"
    print(generate_bc(url, ' : '))
    url = "www.agcpartners.co.uk"
    print(generate_bc(url, ' : '))
"""
Expected: &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt; - instead got: &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;a href="//www.linkedin.com/"&gt;WWW&lt;/a&gt; * &lt;a href="//www.linkedin.com/in/"&gt;IN&lt;/a&gt; * &lt;span class="active"&gt;GIACOMOSORBI&lt;/span&gt;
 The one used in the above test was my LinkedIn Profile; if you solved the kata this far and manage to get it, feel free to add me as a contact, message me about the language that you used and I will be glad to endorse you in that skill and possibly many others :)
 Log
Expected: &lt;span class="active"&gt;HOME&lt;/span&gt; - instead got: &lt;a href="/"&gt;HOME&lt;/a&gt; * &lt;span class="active"&gt;&lt;/span&gt;
 Log
 """
