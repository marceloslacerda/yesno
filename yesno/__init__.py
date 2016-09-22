__version__ = '0.0.0'
YES_S = 'yes'
NO_S = 'no'
YES = True
NO = False
INVALID = None

def str_to_bool(s):
    s = s.strip()
    if (s.lower() == YES_S) | (s.lower() == YES_S[0]):
        return YES
    elif (s.lower() == NO_S) | (s.lower() == NO_S[0]):
        return NO
    else:
        return INVALID

def input_to_bool(query, default='', exit_on_sigint=True, punctuation='?',
                  return_string=False):
    try:
        if default:
            string = input('{}[{}]{} '.format(query, default, punctuation))
            if not string:
                string = default
        else:
            string = input('{}{} '.format(query, punctuation))
    except KeyboardInterrupt:
        if exit_on_sigint:
            exit(1)
        else:
            raise
    if return_string:
        return string, str_to_bool(string)
    else:
        return str_to_bool(string)

def input_until_bool(query, error='{} is not one of {}', default='',
                     exit_on_sigint=True, punctuation='?'):
    while True:
        result = input_to_bool(query, default, exit_on_sigint, punctuation, True)
        if result[1] is not None:
            return result[1]
        else:
            print(error.format(result[0], [YES_S, NO_S]))
