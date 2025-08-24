from wallet import Wallet
import json
import random
import time
import multiprocessing
from aevo import AevoClient
import requests


# Loading the wallets information from the data.json file including the private key, wallet, and proxy data
def initializeWallets():
    wallets = []
    f = open("data.json")
    data = json.load(f)
    for info in data:
        wal = Wallet(**info)
        wallets.append(wal)

    return wallets


# After waiting a random period of time, a transaction will be made for the inputted wallet
def txLoop(wal):
    info = wal.getAevoInfo()
    aevo = AevoClient(
        signing_key=info[0],
        wallet_address=info[1],
        api_key=info[2],
        api_secret=info[3],
        env="mainnet",
    )

    while True:
        n = random.randint(240, 300)  # 240-330 = 4-5.5hrs
        print(f"{wal.getName()}: tx delay for {n} minutes")
        time.sleep(n * 60)
        wal.tx(aevo)


def ProxyTester(wal):
    while True:
        n = random.randint(180, 240)  # 180-240 = 3-4hrs
        print(f"{wal.getName()}: sleep for {n} minutes")
        time.sleep(n * 60)
        proxies = proxies = {"http": wal.getProxy(), "https": wal.getProxy()}

        response = requests.get("https://ipv4.icanhazip.com", proxies=proxies)
        print(f"{wal.getName()}: {response.text[0:18]}")


# -------------------MAIN-------------------
if __name__ == "__main__":
    # Initialize all the wallets from data.json if program restarts
    MASTER_WALLETS = initializeWallets()

    # Multiprocessing - create new process for each wallet
    processes = [
        multiprocessing.Process(target=txLoop, args=(i,)) for i in MASTER_WALLETS
    ]

    # Start all of the processes
    for process in processes:
        process.start()

    # Wait for processes to end (will prob never get past this point)
    for process in processes:
        process.join()

    print("Done!")
