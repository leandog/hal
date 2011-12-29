
import re

class MessageHandler:

    def __init__(self, reply_sender):
        self.reply_sender = reply_sender

    def handle(self, msg):
        if self.should_ignore(msg):
            return
        self.reply_sender.reply(msg, "I'm sorry %s, I can't do that." % msg['mucnick'])

    def should_ignore(self, msg):
        if not self.is_addressed_to_me(msg):
            return True
        if self.is_replayed_message(msg):
            return True
        return False

    def is_addressed_to_me(self, msg):
        return re.search(r'\bhal\b', msg['body'], re.IGNORECASE) != None

    def is_replayed_message(self, msg):
        return msg['id'] == None or msg['id'] == ''

    def extract_command(self, msg):
        return re.sub(r'^\s*@hal\b\s*', '', msg['body'], re.IGNORECASE)

