# STG_locker
Скрипт блокировки токенов STG на сети Polygon

### Содержание

1. [Требования](#требования)
2. [Установка](#установка)
3. [Функции](#функции)
4. [Настройка](#настройка)
5. [Обратная связь](#обратная-связь)

### Требования<a name="требования"></a>

- Python 3.x

### Установка<a name="установка"></a>

1. Подготовьте файл "private_keys.txt", содержащий приватные ключи кошельков, которые вы хотите обработать.
2. Установите зависимости: `pip install -r requirements.txt`
3. При необходимости отредактируйте переменные, такие как `amount_to_approve` и `unlock_time`.
4. Запустите скрипт с помощью выбранного вами интерпретатора Python: `python3 main.py`

### Функции<a name="функции"></a>

1. **Блокировка токенов STG:**
   - Скрипт считывает приватные ключи из файла "private_keys.txt", где каждый ключ представляет информацию для одного кошелька.
   - Он обрабатывает каждый кошелек, выполняя следующие шаги:

2. **Мониторинг газа:**
   - Отслеживает цены на газ в сети Polygon.
   - Ожидает, пока цены на газ не снизятся ниже 200 Gwei.

### Настройка<a name="настройка"></a>

- При необходимости отредактируйте переменные, такие как `amount_to_approve` и `unlock_time` в скрипте.

### Обратная связь<a name="обратная-связь"></a>
Ваш отзыв для нас очень важен. Вы можете поделиться своим мнением и предложениями в
[Chat](https://t.me/Klondike_Talks) <br>

[Telegram](https://t.me/MyKlondike) <br>

🍩 (EVM): 0xe93081718a75818Be2eB1E1336c8c2AC930e44e0

### Важное замечание

Убедитесь, что ваши приватные ключи хранятся в безопасности и не подвергаются непреднамеренному раскрытию. Скрипт предполагает ответственное использование и обращение с приватными ключами.

### Отказ от ответственности

Этот скрипт включает в себя обработку приватных ключей, которые представляют собой чувствительную информацию. Используйте его ответственно и убедитесь, что вы понимаете последствия действий, выполняемых скриптом. Разработчики не несут ответственности за неправильное использование или потерю средств.

### Лицензия

Этот скрипт выпущен под [лицензией MIT](LICENSE). Вы можете свободно вносить изменения и использовать его по своему усмотрению.
