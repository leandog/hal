
from messagehandler import *

class Test_MessageHandler:

    def message_with_body(self, body):
        return {'id':'foo42', 'body': body}

    def test_should_ignore_returns_True_for_arbitrary_message(self):
        assert MessageHandler(None).should_ignore(self.message_with_body('@joe, dude, what is up?'))

    def test_should_ignore_returns_False_if_message_contains_at_hal(self):
        assert not MessageHandler(None).should_ignore(self.message_with_body('@hal, dude, what is up?'))

    def test_should_ignore_returns_True_if_message_contains_at_halbert(self):
        assert MessageHandler(None).should_ignore(self.message_with_body('@halbert, dude, what is up?'))

    def test_should_ignore_returns_False_for_Hal(self):
        assert not MessageHandler(None).should_ignore(self.message_with_body('Hal, open the pod bay doors.'))

    def test_should_ignore_returns_True_when_id_is_empty_string(self):
        assert MessageHandler(None).is_replayed_message({'body':'testing...', 'id':''})

    def test_should_ignore_returns_True_when_id_is_None(self):
        assert MessageHandler(None).is_replayed_message({'body':'testing...', 'id':None})

