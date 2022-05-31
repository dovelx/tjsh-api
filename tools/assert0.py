import  re
import unittest
def assertRegex(text, expected_regex, msg=None):
    """Fail the test unless the text matches the regular expression."""
    if isinstance(expected_regex, (str, bytes)):
        assert expected_regex, "expected_regex must not be empty."
        expected_regex = re.compile(expected_regex)
        #print("expected_regex match")
        #return 1
    if not expected_regex.search(text):
        msg = msg or "Regex didn't match"
        msg = '%s: %r not found in %r' % (msg, expected_regex.pattern, text)
        #raise unittest.TestCase.failureException(msg)
        #print(msg)
        return 0
    return 1