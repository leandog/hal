
from messagefilter import *

class Test_MessageFilter:

    def message_with_body(self, body):
        return {'body': body}

    def test_is_addressed_to_me_returns_False_for_arbitrary_message(self):
        assert not MessageFilter().is_addressed_to_me(self.message_with_body('@joe, dude, what is up?'))

    def test_is_addressed_to_me_returns_True_if_message_contains_at_hal(self):
        assert MessageFilter().is_addressed_to_me(self.message_with_body('@hal, dude, what is up?'))

    def test_is_addressed_to_me_returns_False_if_message_contains_at_halbert(self):
        assert not MessageFilter().is_addressed_to_me(self.message_with_body('@halbert, dude, what is up?'))

    def test_is_addressed_to_me_returns_True_for_Hal(self):
        assert MessageFilter().is_addressed_to_me(self.message_with_body('Hal, open the pod bay doors.'))

