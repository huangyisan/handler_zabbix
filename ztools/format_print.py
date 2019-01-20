

def print_load(title, content):
    Asterisk = '*'
    if '\n' in title:
        title_list = title.split('\n')
        max_len = max(title_list, key=len)
        Asterisk = Asterisk * len(max_len)
    else:
        max_len = len(title)
        Asterisk = Asterisk * max_len
    print(Asterisk + '\n' + title + '\n' + Asterisk + '\n' + content)
