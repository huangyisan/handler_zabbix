def print_load(title, content, status):
    Asterisk = '*'

    info = "INFO: "
    warning = "WARNING: "
    success = "SUCCESS: "
    error = "ERROR: "


    reason = "Reason: "
    recall_message = "Recall Message:\n"

    if '\n' in title:
        title_list = title.split('\n')
        max_len = max(title_list, key=len)
        Asterisk = Asterisk * len(max_len)
    else:
        max_len = len(title)
        Asterisk = Asterisk * max_len

    Asterisk += (len(status)+2) * "*"


    if status.lower() == "info":
        print(Asterisk + '\n' + info + title + '\n' + Asterisk + '\n' + content)

    elif status.lower() == "warning":
        print(Asterisk + '\n' + warning + title + '\n' + Asterisk + '\n' + content)

    elif status.lower() == "success":
        print(Asterisk + '\n' + success + title + '\n' + Asterisk + '\n' + recall_message + content)

    elif status.lower() == "error":
        print(Asterisk + '\n' + error + title + '\n' + Asterisk + '\n' + reason + content)

    else:
        print(Asterisk + '\n' + title + '\n' + Asterisk + '\n' + content)
