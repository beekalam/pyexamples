import pyrad.packet
from pyrad.client import Client
from pyrad.dictionary import Dictionary
from User import User
import pyrad.tools

class constants:
    host = "localhost"


class nassim:
    def __init__(self, host, port=None):
        self.host = host
        self.port = port
        self.nas_ip_address = '192.168.155.93'
        self.nas_port_type  = 'virtual'
        self.nas_called_station_id = '94.74.128.22'
        self.nas_calling_station_id = '94.74.128.22'
        self.frame_protocol = 'PPP'
        self.service_type = 'Framed-User'
        self.dictionary = Dictionary("dictionary", "dictionary")
        self.interimupdate = 60
        self.shared_secret = "testing123"
        self.Nas_Identifier = "localhost"
        self.srv = Client(server=constants.host, secret="testing123", dict=Dictionary("dictionary", "dictionary"))
        self.userlist = []

    def send_auth_packet(self):
        user = User("bob","passbob")
        # req = self.srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name="alice", NAS_Identifier="localhost")
        req = self.srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name=user.username, NAS_Identifier="localhost")
        req["User-Password"] = req.PwCrypt(user.password)
        reply = self.srv.SendPacket(req)
        if reply.code == pyrad.packet.AccessAccept:
            return True
        return False
        # if reply.code == pyrad.packet.AccessAccept:
        #     print "access accepted"
        # else:
        #     print "access denied"
        #
        # print "Attributes returned by server:"
        # for i in reply.keys():
        #     print "%s: %s" % (i, reply[i])

nsim = nassim(constants.host)
counter = 1
while True:

    if nsim.send_auth_packet():
        counter += 1
        if counter % 10000 == 0:
            print "." * 100
            print counter
