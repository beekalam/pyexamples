import argparse, socket
from datetime import datetime
import binascii
import pyrad.tools

import md5, struct, types, random, UserDict

try:
    import hashlib

    md5_constructor = hashlib.md5
except ImportError:
    # BBB for python 2.4
    md5_constructor = md5.new

import six

MAX_BYTES = 65535
IP = '94.74.128.14'
PORT = 1700


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    # data = text.encode('ascii')
    data = create_packet()
    sock.sendto(data, (IP, PORT))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)  # Danger!
    # text = data.decode('ascii')
    (code, id, length, authenticator) = struct.unpack("!BBH16s", data[0:20])

    print "code: " + str(code)
    print "id: " + str(id)
    print "autheticator: " + str(authenticator)
    print "address: " + str(address)

    text = data
    print('The server {} replied {!r}'.format(address, text))


def encode_attr(key, value):
    if type(key) == types.TupleType:
        value = struct.pack("!L", key[0]) + \
                encode_attr(key[1], value)
        key = 26

    return struct.pack("!BB", key, (len(value) + 2)) + value


def encode_attrs(dic):
    result = ""
    for (code, datalst) in dic.items():
        # for data in datalst:
        result += encode_attr(code, datalst)

    return result


def create_packet():
    # MIKROTIK                = 14988 (VENDOR CODE)
    # DisconnectRequest       = 40
    # DisconnectAck           = 41
    # DisconnectNack          = 42

    packet_code = 40
    mikrotik_vendor_id = 14988
    packet_id = random.randrange(1, 256)
    secret = "123123"

    dict = {}
    dict_attrs = {}
    dict_attrs[1] = "xbstest"  # "User-Name"
    # dict_attrs[4] = EncodeAddress("94.74.128.14") # "NAS-IP-Address"
    dict_attrs[4] = EncodeAddress("94.74.128.14")  # "NAS-IP-Address"
    dict_attrs[44] = "81a00986"  # "Acct-Session-Id"
    # dict[(mikrotik_vendor_id, packet_code)] = dict_attrs

    attr = encode_attrs(dict_attrs)
    header = struct.pack("!BBH", packet_code, packet_id, (20 + len(attr)))
    # authenticator = md5_constructor(header[0:4] + 16 * six.b('\x00') + attr + secret).digest()
    authenticator = md5.new(header[0:4] + 16 * six.b('\x00') + attr + secret).digest()
    # authenticator = CreateAuthenticator()

    return header + authenticator + attr


def CreateAuthenticator():
    data = ""
    for i in range(16):
        data += chr(random.randrange(0, 256))

    return data



############################################
############ TOOLS #########################
############################################


def EncodeString(str):
    assert len(str) <= 253

    return str


def EncodeAddress(addr):
    (a, b, c, d) = map(int, addr.split("."))
    return struct.pack("BBBB", a, b, c, d)


def EncodeInteger(num):
    return struct.pack("!I", num)


def EncodeDate(num):
    return struct.pack("!I", num)


def DecodeString(str):
    return str


def DecodeAddress(addr):
    return ".".join(map(str, struct.unpack("BBBB", addr[:4])))


def DecodeInteger(num):
    return (struct.unpack("!I", num[:4]))[0]


def DecodeDate(num):
    return (struct.unpack("!I", num[:4]))[0]


def EncodeAttr(datatype, value):
    if datatype == "string":
        return EncodeString(value)
    elif datatype == "ipaddr":
        return EncodeAddress(value)
    elif datatype == "integer":
        return EncodeInteger(value)
    elif datatype == "date":
        return EncodeDate(value)
    else:
        return value


def DecodeAttr(datatype, value):
    if datatype == "string":
        return DecodeString(value)
    elif datatype == "ipaddr":
        return DecodeAddress(value)
    elif datatype == "integer":
        return DecodeInteger(value)
    elif datatype == "date":
        return DecodeDate(value)
    else:
        return value


############################################

if __name__ == '__main__':
    client(1700)

#
# Version $Id: dictionary,v 1.2 2004/12/23 16:53:33 farshad_kh Exp $
#
#   This file contains dictionary translations for parsing
#   requests and generating responses.  All transactions are
#   composed of Attribute/Value Pairs.  The value of each attribute
#   is specified as one of 4 data types.  Valid data types are:
#
#   string  - 0-253 octets
#   ipaddr  - 4 octets in network byte order
#   integer - 32 bit value in big endian order (high byte first)
#   date    - 32 bit value in big endian order - seconds since
#                   00:00:00 GMT,  Jan.  1,  1970
#
#   FreeRADIUS includes extended data types which are not defined
#   in RFC 2865 or RFC 2866.  These data types are:
#
#   abinary - Ascend's binary filter format.
#   octets  - raw octets, printed and input as hex strings.
#         e.g.: 0x123456789abcdef
#
#
#   Enumerated values are stored in the user file with dictionary
#   VALUE translations for easy administration.
#
#   Example:
#
#   ATTRIBUTE     VALUE
#   ---------------   -----
#   Framed-Protocol = PPP
#   7       = 1 (integer encoding)
#

#
#   Include compatibility dictionary for older users file. Move this
#   directive to the end of the file if you want to see the old names
#   in the logfiles too.
#
#   Following are the proper new names. Use these.
#
# ATTRIBUTE   User-Name           1   string
# ATTRIBUTE   User-Password       2   string
# ATTRIBUTE   CHAP-Password       3   octets
# ATTRIBUTE   NAS-IP-Address      4   ipaddr
# ATTRIBUTE   NAS-Port            5   integer
# ATTRIBUTE   Service-Type        6   integer
# ATTRIBUTE   Framed-Protocol     7   integer
# ATTRIBUTE   Framed-IP-Address   8   ipaddr
# ATTRIBUTE   Framed-IP-Netmask   9   ipaddr
# ATTRIBUTE   Framed-Routing      10  integer
# ATTRIBUTE   Filter-Id           11  string
# ATTRIBUTE   Framed-MTU          12  integer
# ATTRIBUTE   Framed-Compression  13  integer
# ATTRIBUTE   Login-IP-Host       14  ipaddr
# ATTRIBUTE   Login-Service       15  integer
# ATTRIBUTE   Login-TCP-Port      16  integer
# ATTRIBUTE   Reply-Message       18  string
# ATTRIBUTE   Callback-Number     19  string
# ATTRIBUTE   Callback-Id         20  string
# ATTRIBUTE   Framed-Route        22  string
# ATTRIBUTE   Framed-IPX-Network  23  ipaddr
# ATTRIBUTE   State               24  octets
# ATTRIBUTE   Class               25  octets
# ATTRIBUTE   Vendor-Specific     26  octets
# ATTRIBUTE   Session-Timeout     27  integer
# ATTRIBUTE   Idle-Timeout        28  integer
# ATTRIBUTE   Termination-Action  29  integer
# ATTRIBUTE   Called-Station-Id   30  string
# ATTRIBUTE   Calling-Station-Id  31  string
# ATTRIBUTE   NAS-Identifier      32  string
# ATTRIBUTE   Proxy-State         33  octets
# ATTRIBUTE   Login-LAT-Service   34  string
# ATTRIBUTE   Login-LAT-Node      35  string
# ATTRIBUTE   Login-LAT-Group     36  octets
# ATTRIBUTE   Framed-AppleTalk-Link   37  integer
# ATTRIBUTE   Framed-AppleTalk-Network 38 integer
# ATTRIBUTE   Framed-AppleTalk-Zone   39  string

# ATTRIBUTE   Acct-Status-Type    40  integer
# ATTRIBUTE   Acct-Delay-Time     41  integer
# ATTRIBUTE   Acct-Input-Octets   42  integer
# ATTRIBUTE   Acct-Output-Octets  43  integer
# ATTRIBUTE   Acct-Session-Id     44  string
# ATTRIBUTE   Acct-Authentic      45  integer
# ATTRIBUTE   Acct-Session-Time   46  integer
# ATTRIBUTE       Acct-Input-Packets  47  integer
# ATTRIBUTE       Acct-Output-Packets 48  integer
# ATTRIBUTE   Acct-Terminate-Cause    49  integer
# ATTRIBUTE   Acct-Multi-Session-Id   50  string
# ATTRIBUTE   Acct-Link-Count         51  integer
# ATTRIBUTE   Acct-Input-Gigawords    52      integer
# ATTRIBUTE   Acct-Output-Gigawords   53      integer
# ATTRIBUTE   Event-Timestamp         55      date

# ATTRIBUTE   CHAP-Challenge      60  string
# ATTRIBUTE   NAS-Port-Type       61  integer
# ATTRIBUTE   Port-Limit          62  integer
# ATTRIBUTE   Login-LAT-Port      63  integer

# ATTRIBUTE   Acct-Tunnel-Connection  68  string

# ATTRIBUTE   ARAP-Password           70      string
# ATTRIBUTE   ARAP-Features           71      string
# ATTRIBUTE   ARAP-Zone-Access        72      integer
# ATTRIBUTE   ARAP-Security           73      integer
# ATTRIBUTE   ARAP-Security-Data      74      string
# ATTRIBUTE   Password-Retry          75      integer
# ATTRIBUTE   Prompt                  76      integer
# ATTRIBUTE   Connect-Info            77  string
# ATTRIBUTE   Configuration-Token     78  string
# ATTRIBUTE   EAP-Message             79  string
# ATTRIBUTE   Message-Authenticator   80  octets
# ATTRIBUTE   ARAP-Challenge-Response 84  string  # 10 octets
# ATTRIBUTE   Acct-Interim-Interval   85      integer
# ATTRIBUTE   NAS-Port-Id             87  string
# ATTRIBUTE   Framed-Pool             88  string
# ATTRIBUTE   NAS-IPv6-Address    95  octets  # really IPv6
# ATTRIBUTE   Framed-Interface-Id 96  octets  # 8 octets
# ATTRIBUTE   Framed-IPv6-Prefix  97  octets  # stupid format
# ATTRIBUTE   Login-IPv6-Host     98  octets  # really IPv6
# ATTRIBUTE   Framed-IPv6-Route   99  string
# ATTRIBUTE   Framed-IPv6-Pool    100 string

# ATTRIBUTE   Digest-Response     206 string
# ATTRIBUTE   Digest-Attributes   207 octets  # stupid format
