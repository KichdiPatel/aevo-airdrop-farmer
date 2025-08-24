import asyncio

# from aevo import AevoClient
import json
import time
import random
import datetime


# Wallet class that makes transactions across multiple wallets much simpler
class Wallet:
    def __init__(self, name, private_key, address, api_key, api_secret, trading, proxy):
        self.name = name
        self.trading = trading
        self.privKey = private_key
        self.address = address
        self.api_key = api_key
        self.api_secret = api_secret
        self.proxy = proxy
        # self.aevo = AevoClient(
        #     signing_key=self.privKey,
        #     wallet_address=self.address,
        #     api_key=api_key,
        #     api_secret=api_secret,
        #     env="mainnet",
        # )

        # if not self.aevo.signing_key:
        #     raise Exception(
        #         "Signing key is not set. Please set the signing key in the AevoClient constructor."
        #     )

    def __str__(self):
        return f"{self.trading}"

    def getAevoInfo(self):
        return (self.privKey, self.address, self.api_key, self.api_secret)

    def getName(self):
        return self.name

    def getProxy(self):
        return self.proxy

    def updateJSON(self):
        i = int(self.name[-1])
        f = open("data.json")
        data = json.load(f)
        data[i - 1]["trading"] = self.trading

    # This opens a buy trade on the ETH perp on Aevo
    def openTrade(self, aevo):
        # Complete open trade tx
        response = aevo.rest_create_market_order(
            instrument_id=1, is_buy=True, quantity=0.08, proxy=self.proxy
        )

        # print(response)

        # Print result to console
        print(f"{self.name}: bought 0.01 contract")

        # Update object trading status
        self.trading = True

        # Write to File
        file = "logs/" + self.name + ".txt"
        f = open(file, "a")
        current_time = datetime.datetime.now()
        f.write(f"{current_time}: Open Trade\n")
        f.close()

        self.updateJSON()

    # This opens a sell trade on the ETH perp on Aevo which closes a buy trade
    def closeTrade(self, aevo):
        # Complete close trade tx
        response = aevo.rest_create_market_order(
            instrument_id=1, is_buy=False, quantity=0.08, proxy=self.proxy
        )

        # Print result to console
        print(f"{self.name}: closed 0.01 contract")

        # Update object trading status
        self.trading = False

        # Write to File
        file = "logs/" + self.name + ".txt"
        f = open(file, "a")
        current_time = datetime.datetime.now()
        f.write(f"{current_time}: Close Trade\n")
        f.close()

        self.updateJSON()

    def tx(self, aevo):
        if self.trading:
            self.closeTrade(aevo)
        else:
            self.openTrade(aevo)
            n = random.uniform(0.5, 2.5)
            time.sleep(n)
            self.closeTrade(aevo)
