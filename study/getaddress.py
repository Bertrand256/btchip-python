from btchip.btchip import *
from btchip.btchipUtils import compress_public_key,format_transaction, get_regular_input_script
import sys

def main():
#	dongle = getDongle(True)
	dongle = getDongle(False)
	app = btchip(dongle)
	mpath = "44'/5'/0'/0"

	for i in range(11):
		addr_path = mpath + '/' + str(i)
		nodedata = app.getWalletPublicKey(addr_path)
		publicKey = compress_public_key(nodedata.get('publicKey'))
		address   = (nodedata.get('address')).decode("utf-8")
		print(addr_path, address)


if __name__ == '__main__':
    main()
