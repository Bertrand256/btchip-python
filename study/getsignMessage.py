from btchip.btchip import *
from btchip.btchipUtils import *
import sys
import base64
import time


def main():
#    dongle = getDongle(True)
    dongle = getDongle(False)
    app = btchip(dongle)
    

    msg = "test1234 4321"

    #addr_path = "44'/5'/0'/0/0"
    addr_path = "44'/5'/0'/0/0"
    nodedata = app.getWalletPublicKey(addr_path)
    publicKey = compress_public_key(nodedata.get('publicKey'))
    address   = (nodedata.get('address')).decode("utf-8")    

    info = app.signMessagePrepare(addr_path, msg)
    signature = app.signMessageSign()

    rLength = signature[3]
    r = signature[4 : 4 + rLength]
    sLength = signature[4 + rLength + 1]
    s = signature[4 + rLength + 2:]
    if rLength == 33:
        r = r[1:]
    if sLength == 33:
        s = s[1:]

    work = bytes(chr(27 + 4 + (signature[0] & 0x01)), "utf-8") + r + s
    sig = base64.b64encode(work).decode("utf-8")

    print("path : %s, addr : %s, msg : \"%s\", sig : %s" % (addr_path, address, msg, sig))

if __name__ == '__main__':
    main()


