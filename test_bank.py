from bank import value

#test greeting which starts with "hello"
def test_helo():
    assert value("hello") == "$0"
    assert value("hello, how are you?") == "$0"

#test greeting which starts with "h"
def test_h():
    assert value("how are you?") == "$20"
    assert value("how it's going?") == "$20"

#test other greetings
def test_greeting():
    assert value("what's up, bro?") == "$100"
    assert value("gamarjoba") == "$100"
