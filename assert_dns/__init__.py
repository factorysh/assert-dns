from dns import resolver


def txt(domain):
    print(domain)
    try:
        answers = resolver.query(domain, 'TXT')
    except resolver.NoAnswer:
        pass
    else:
        for answer in answers:
            for string in answer.strings:
                yield string.split(b'=', 1)


if __name__ == "__main__":
    import sys
    from pprint import pprint

    pprint(dict(txt(sys.argv[1])))
