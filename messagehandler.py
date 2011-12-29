
import re

class MessageHandler:
    def is_addressed_to_me(self, msg):
        return re.search(r'\bhal\b', msg['body'], re.IGNORECASE) != None

    def is_replayed_message(self, msg):
        return msg['id'] == None or msg['id'] == ''

