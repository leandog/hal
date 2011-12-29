
class MessageFilter:
    def is_addressed_to_me(self, msg):
        return '@hal' in msg

