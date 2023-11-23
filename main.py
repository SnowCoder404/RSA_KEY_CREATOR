#
#   Copyright © 2023, SnowCoder404
#
from Crypto.PublicKey import RSA


def genarate():
    private_key = RSA.generate(4096)
    key_data = open('secret_key', 'wb')
    key_data.write(private_key.export_key("PEM"))
    key_data.close()
    public_key = private_key.publickey()
    key_data = open('public_key', 'wb')
    key_data.write(public_key.export_key("PEM"))


genarate()
