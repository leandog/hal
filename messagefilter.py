
import re

class MessageFilter:
    def is_addressed_to_me(self, msg):
        return re.search(r'\bhal\b', msg['body'], re.IGNORECASE) != None

