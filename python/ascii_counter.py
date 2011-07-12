
def inc_ascii_counter(counter, min_digit='A', max_digit='Z'):
    """Increment an ascii string treated as a counter, e.g. 'AAA' -> 'AAB'.
   
    If the result exceeds the maximum value, it goes back to minimum,
    e.g. 'ZZZ' -> 'AAA'

    >>> inc_ascii_counter('AAA')
    'AAB'
    >>> inc_ascii_counter('AAZ')
    'ABA'
    >>> inc_ascii_counter('ZZZ')
    'AAA'
    >>> inc_ascii_counter('ZAZ')
    'ZBA'
    >>> inc_ascii_counter('aaa', 'a', 'z')
    'aab'
    >>> inc_ascii_counter('zzz', 'a', 'z')
    'aaa'
    """
    out = []
    for d in reversed(list(counter)):
        if d >= max_digit:
            # carry ...
            out.insert(0, min_digit)
        else:
            out.insert(0, chr(ord(d) + 1))
            break
   
    return counter[0:len(counter) - len(out)] + ''.join(out)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
