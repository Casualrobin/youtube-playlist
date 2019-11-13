def validate_url(_url):
    if "youtube.com" not in _url:
        return False
    elif _url.__contains__(' '):
        return False
    else:
        return True


def validate_output_location(_output):
    if _output == "terminal" or _output == "txt" or _output == "csv":
        return True
    else:
        return False