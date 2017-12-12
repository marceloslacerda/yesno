import sys

if sys.version_info[0] == 2:
    input = raw_input

__version__ = '0.0.1'
YES_S = 'yes'
NO_S = 'no'
YES = True
NO = False
INVALID = None

def str_to_bool(s):
    """Turns a string to a boolean or None if the supplied string doesn't match
the value of yes, no, y or n (case insensitive)."""
    s = s.strip()
    if (s.lower() == YES_S) | (s.lower() == YES_S[0]):
        return YES
    elif (s.lower() == NO_S) | (s.lower() == NO_S[0]):
        return NO
    else:
        return INVALID

def input_to_bool(query, default='', exit_on_sigint=True, punctuation='?',
                  return_string=False):
    """Queries the user via stdin/stdout for yes or no, returns the equivalent
boolean.


    Arguments:
    query          -- The question to ask the user
    default        -- The default answer to expect from the user
                      default('' no default)
    exit_on_sigint -- Determines whether to exit after a SIGINT or to raise
                      KeyboardInterruptException
    punctuation    -- What kind of punctuation to terminate the query with
    return_string  -- Whether to return the user input with the boolean value.
"""
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
    """Works like input_to_bool except it retries if the answer is invalid.


    Arguments:
    query          -- The question to ask the user
    error          -- The error message to print when a invalid answer is given
                      default('' no default)
    exit_on_sigint -- Determines whether to exit after a SIGINT or to raise
                      KeyboardInterruptException
    punctuation    -- What kind of punctuation to terminate the query with"""

    while True:
        result = input_to_bool(query, default, exit_on_sigint, punctuation, True)
        if result[1] is not None:
            return result[1]
        else:
            print(error.format(result[0], [YES_S, NO_S]))
