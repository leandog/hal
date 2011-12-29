
from messagehandler import *
from dingus import Dingus, DontCare

class Test_MessageHandler:

    def message_with_body(self, body):
        return {'id':'foo42', 'body':body, 'mucnick':'Dave'}

    def test_ignores_arbitrary_message(self):
        assert MessageHandler(None).should_ignore(self.message_with_body('@joe, dude, what is up?'))

    def test_does_not_ignore_messages_containing_at_hal(self):
        assert not MessageHandler(None).should_ignore(self.message_with_body('@hal, dude, what is up?'))

    def test_ignores_messages_contains_at_halbert(self):
        assert MessageHandler(None).should_ignore(self.message_with_body('@halbert, dude, what is up?'))

    def test_does_not_ignore_messages_containing_Hal(self):
        assert not MessageHandler(None).should_ignore(self.message_with_body('Hal, open the pod bay doors.'))

    def test_ignores_messages_with_empty_string_for_id(self):
        assert MessageHandler(None).is_replayed_message({'body':'testing...', 'id':''})

    def test_ignores_messages_with_None_for_id(self):
        assert MessageHandler(None).is_replayed_message({'body':'testing...', 'id':None})

    def test_response_Im_sorry_Dave_for_unrecognized_commands(self):
        reply_sender = Dingus('reply_sender')
        MessageHandler(reply_sender).handle(self.message_with_body('@hal flarxlebrabt it.'))
        assert len(reply_sender.calls('reply', DontCare, "I'm sorry Dave, I can't do that.")) == 1

        

