import messagehandler
import sleekxmpp

JABBER_ID   = '12552_63278@chat.hipchat.com'
NICKNAME    = 'Hal 9000'
PASSWORD    = 'foobearlives!'
ROOM_ID     = '12552_leandog@conf.hipchat.com'

class Hal(sleekxmpp.ClientXMPP):

    def __init__(self):
        print "Booting..."
        sleekxmpp.ClientXMPP.__init__(self, JABBER_ID, PASSWORD)
        self.message_handler = messagehandler.MessageHandler(self)
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data Forms
        self.register_plugin('xep_0045') # MUC
        self.register_plugin('xep_0060') # PubSub
        self.auto_authorize = True
        self.auto_subscribe = True
        self.add_event_handler('session_start', self.session_start)
        self.add_event_handler('groupchat_message', self.muc_message)

    def session_start(self, event):
        self.get_roster()
        self.send_presence()
        self.plugin['xep_0045'].joinMUC(ROOM_ID, NICKNAME, wait=True)

    def muc_message(self, msg):
        self.message_handler.handle(msg)

    def reply(self, msg, body):
        self.send_message(mto = msg['from'].bare, mbody = body, mtype = 'groupchat')

