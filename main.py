import time
import random
import atexit
from termcolor import cprint
import logging
from web3 import Web3
import json
import requests
from web3.middleware import geth_poa_middleware
from web3.middleware import latest_block_based_cache_middleware

RPC = "https://polygon.llamarpc.com"
web3 = Web3(Web3.HTTPProvider(RPC))

web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3.middleware_onion.inject(latest_block_based_cache_middleware, layer=0)

STG_contract_address = "0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590"
Loke_contract = "0x3AB2DA31bBD886A7eDF68a6b60D3CDe657D3A15D"

logging.basicConfig(level=logging.INFO)


def intToDecimal(qty, decimal):
    return int(qty * 10 ** decimal)
    

def to_checksum_address(address):
    return web3.to_checksum_address(address)


def get_balance(private_key):
    wallet_address = web3.eth.account.from_key(private_key).address
    STG_abi = load_abi_from_file('STG_abi.json')
    checksum_address = to_checksum_address(STG_contract_address)
    contract = web3.eth.contract(address=checksum_address, abi=STG_abi)
    token_balance = contract.functions.balanceOf(wallet_address).call()
    decimals = 18
    STG_balance = token_balance / 10 ** decimals
    return STG_balance
    time.sleep(1)


def load_abi_from_file(file_path):
    with open(file_path, 'r') as f:
        STG_abi = json.load(f)
        return STG_abi
          
    with open(file_path, 'r') as f:
        loke_abi = json.load(f)
        return loke_abi

def gas_price():
    gas_price_wei = web3.eth.gas_price
    return gas_price_wei
    
def get_current_gas_limit():
    latest_block = web3.eth.get_block("latest")
    return latest_block["gasLimit"]


def get_transaction_receipt(tx_hash):
    max_retries = 3
    retries = 0
    while retries < max_retries:
        try:
            tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
            if tx_receipt is not None:
                return tx_receipt
            else:
                print(f"Transaction with hash: '{tx_hash.hex()}' not found. Retrying...")
                retries += 1
                time.sleep(30) 
        except Exception as e:
            print(f"Error while getting transaction receipt: {e}")
            retries += 1
            time.sleep(5)

    return None


def wait_for_low_gas_price():
    while True:
        current_gas_price = gas_price()
        gas_price_gwei = current_gas_price / 10 ** 9
        print(f"Current gas price: {gas_price_gwei}")

        if gas_price_gwei <= 200:
            break  # Выходим из цикла, если gas_price_gwei опустилось ниже 200
        else:
            print("Gas price is too high. Waiting for 30 seconds...")
            time.sleep(30)  


wait_for_low_gas_price()


def approve(private_key, spender, amount):
    try:
        wallet_address = web3.eth.account.from_key(private_key).address
        wallet = to_checksum_address(wallet_address)
        STG_abi = load_abi_from_file('STG_abi.json')     
        token = to_checksum_address(STG_contract_address)
        contract = web3.eth.contract(address=token, abi=STG_abi)
        decimals = 18
        amount_in_wei = int(amount * 10 ** decimals)
        
        spender_address = to_checksum_address(spender)
        nonce = web3.eth.get_transaction_count(wallet_address)
        gas_price_wei = gas_price()
        gas_limit = get_current_gas_limit()
        tx = {
            'nonce': nonce,
            'from': wallet,
            'gasPrice': gas_price_wei,
            'gas': 500000,
            'chainId': 137,
            'value': 0,
        }
        
       
        contract_txn = contract.functions.approve(spender_address, amount_in_wei).build_transaction(tx)
        
        
        signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=private_key)
        
        
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        time.sleep(10)
        
                         
        print(f'\n>>> STG approve | https://polygonscan.com/tx/{web3.to_hex(tx_hash)}') 
         
        
        tx_receipt = get_transaction_receipt(tx_hash)
        if tx_receipt is not None and tx_receipt['status'] == 1:
            print("Транзакция выполнена успешно!")
        else:
            print("Транзакция не удалась или еще не подтверждена.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

        
        with open("wallets_with_errors.txt", "a") as error_file:
            error_file.write(f"Wallet address: {web3.to_hex(tx_hash)}, Transaction hash: {web3.to_hex(tx_hash)}\n")       

     
def create_lock(private_key, valuem, unlock_time):
    try:
        wallet_address = web3.eth.account.from_key(private_key).address
        wallet = to_checksum_address(wallet_address)
        Loke_abi = load_abi_from_file('loke_abi.json')

        contract_address = to_checksum_address(Loke_contract)
        contract = web3.eth.contract(address=contract_address, abi=Loke_abi)
        decimals = 18
        amount = web3.from_wei(get_balance(private_key), 'ether')
        gas_price_wei = gas_price()                
        nonce = web3.eth.get_transaction_count(wallet_address)
        value = int(valuem * 0.99)
               
        tx = {
            'nonce': nonce,
            'from': wallet,
            'gasPrice': gas_price_wei,
            'gas': 500000,
            'chainId': 137,
            'value': 0,
        }
       
        contract_txn = contract.functions.create_lock(value, unlock_time).build_transaction(tx) 
        
        
        signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=private_key)
        
      
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        print(f'\n>>> STG stake | https://polygonscan.com/tx/{web3.to_hex(tx_hash)}')
        time.sleep(10)
        
        
        tx_receipt = get_transaction_receipt(tx_hash)
        if tx_receipt is not None and tx_receipt['status'] == 1:
            print("Транзакция выполнена успешно!")
        else:
            print("Транзакция не удалась или еще не подтверждена.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

        
        with open("wallets_with_errors.txt", "a") as error_file:
            error_file.write(f"Wallet address: {web3.to_hex(tx_hash)}, Transaction hash: {web3.to_hex(tx_hash)}\n")
def exit_handler():
    print("                 Тебе понравилось? ʕ ᵔᴥᵔ ʔ \n", )
    print("             FeedBacK : https://t.me/MyKlondike  \n", )
    print("             Чат 🐸:  https://t.me/Klondike_Talks  \n", )
    print("         🍩: 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0  ", )
atexit.register(exit_handler)

if __name__ == "__main__":
    with open("private_keys.txt", "r") as f:
        private_keys_list = [row.strip() for row in f]
        
    total_wallets = len(private_keys_list)
    processed_wallets = 0

    for private_key in private_keys_list:
        processed_wallets += 1
        STG_balance = get_balance(private_key)
        wallet_address = web3.eth.account.from_key(private_key).address
        print(f"Обработка кошелька {processed_wallets} из {total_wallets}")
        print(f"Баланс STG в кошельке {wallet_address}: {STG_balance}")
        
        current_gas_price = gas_price()
        gas_price_gwei = current_gas_price / 10**9
        print(f"Current gas price: {gas_price_gwei}")
        
        
        spender_address = "0x3AB2DA31bBD886A7eDF68a6b60D3CDe657D3A15D"
        amount_to_approve = STG_balance  
        approve(private_key, spender_address, amount_to_approve)
        print(f"Жду approve {10} секунд...")
        time.sleep(10)
        
        # Выполнение функции create_lock                  
        valuem = intToDecimal(STG_balance, 18)  
        unlock_time = 1783748761  
        create_lock(private_key, valuem, unlock_time)
                
        # Генерируем случайную задержку от 100 до 300 секунд
        random_delay = random.randint(100, 300)
        print(f"Жду {random_delay} секунд перед обработкой следующего кошелька...")
        time.sleep(random_delay)

  
