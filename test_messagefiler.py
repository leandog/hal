
from messagefilter import *

class Test_MessageFilter:

    def test_is_addressed_to_me_returns_False_for_arbitrary_message(self):
        assert not MessageFilter().is_addressed_to_me('@joe, dude, what is up?')

    def test_is_addressed_to_me_returns_True_if_message_contains_at_hal(self):
        assert MessageFilter().is_addressed_to_me('@hal, dude, what is up?')



