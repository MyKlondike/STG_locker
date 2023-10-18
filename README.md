# Polygon STG Staker

The script interacts with the Polygon blockchain using the `web3` library to create locks for your STG tokens on the Polygon network. These locks enable you to participate in voting on the Snapshot platform.

## Features

### 1. Approve Spending

The script facilitates the approval of spending for a specific amount of STG tokens from multiple wallets. 

### 2. Create Lock

The script offers the ability to create locks for STG tokens. 

### 3. Gas Price Monitoring

To ensure cost-effectiveness, the script continually monitors the current gas price on the Polygon network. It waits for the gas price to drop below a certain threshold (200 Gwei).

## Configuration

The script reads private keys from the "private_keys.txt" file, each representing a different wallet. It processes each wallet by performing the following steps:

1. Retrieves the STG token balance for the wallet.
2. Approves spending for a specified spender address.
3. Creates a lock for a portion of the wallet's STG tokens.
4. Adds a random delay between wallet processing to avoid overwhelming the network.

## Prerequisites

- Python 3.x

## How to Use

1. Prepare a "private_keys.txt" file containing the private keys of the wallets you want to process.
2. pip install -r requirements.txt
3. Modify: `amount_to_approve`, and `unlock_time` variables as needed.
4. Run the script using your preferred Python interpreter: `python3 main.py`.

**Disclaimer:** This script is provided as-is and does not constitute financial or investment advice. Use it at your own risk. The developers of this script are not responsible for any losses incurred.

**FeedBacK ADDRESS:  0xe93081718a75818Be2eB1E1336c8c2AC930e44e0**


========================================================================================================================================================================================

# Polygon STG Staker

Скрипт взаимодействует с блокчейном Polygon с использованием библиотеки `web3` для создания блокировок ваших токенов STG в сети Polygon. Эти блокировки позволяют вам участвовать в голосованиях на платформе Snapshot.

## Возможности

### 1. Утверждение Расходов

Скрипт облегчает процесс утверждения расходов для определенного количества токенов STG из нескольких кошельков.

### 2. Создание Блокировки

Скрипт предоставляет возможность создавать блокировки для токенов STG.

### 3. Мониторинг Цен на Газ

Скрипт постоянно мониторит текущую цену на газ в сети Polygon. Он ожидает, пока газ не опустится ниже определенного порога (200 Gwei).

## Настройка

Скрипт считывает приватные ключи из файла "private_keys.txt", каждый ключ представляет собой данные одного кошелька. Он обрабатывает каждый кошелек, выполняя следующие шаги:

1. Получает баланс токенов STG кошелька.
2. Утверждает расходы для указанного получателя.
3. Создает блокировку для части токенов STG кошелька.
4. Добавляет случайную задержку между обработкой кошельков для избежания перегрузки сети.

## Предварительные требования

- Python 3.x

## Инструкция по использованию

1. Подготовьте файл "private_keys.txt", содержащий приватные ключи кошельков, которые вы хотите обработать.
2. Выполните установку зависимостей: `pip install -r requirements.txt`
3. При необходимости измените переменные `amount_to_approve` и `unlock_time`.
4. Запустите скрипт с помощью выбранного вами интерпретатора Python: `python3 main.py`.

**Отказ от ответственности:** Этот скрипт предоставляется "как есть" и не является финансовым или инвестиционным советом. Используйте его на свой страх и риск. Разработчики этого скрипта не несут ответственности за возможные потери.

**Адрес для обратной связи: 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0**
