def get_args(arg=None):
    args = []
    if arg is not None:
        args = arg
    di = {}
    for i in range(0, len(args)-1):
        if args[i].startswith('-'):
            key = args[i].lower()
            value = args[i + 1].lower()
            di[key] = value

    return di