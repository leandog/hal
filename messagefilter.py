
import re

class MessageFilter:
    def is_addressed_to_me(self, msg):
        return re.search(r'\bhal\b', msg['body'], re.IGNORECASE) != None

    def is_replayed_message(self, msg):
        return False

