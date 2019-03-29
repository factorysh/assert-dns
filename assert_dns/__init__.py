from dns import resolver


def txt(domain):
    try:
        answers = resolver.query(domain, 'TXT')
    except resolver.NoAnswer:
        pass
    else:
        for answer in answers:
            for string in answer.strings:
                yield string.split(b'=', 1)


def mx(domain):
    try:
        answers = resolver.query(domain, 'MX')
    except resolver.NoAnswer:
        pass
    else:
        for answer in answers:
            yield answer.to_text().split(' ', 1)


if __name__ == "__main__":
    import sys
    from pprint import pprint

    d = sys.argv[1]
    print(d)
    pprint(dict(txt(d)))
    pprint(list(mx(d)))
