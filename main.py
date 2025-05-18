import ccxt

exchanges = {
    'binance': ccxt.binance(),
    'kraken': ccxt.kraken(),
    'coinbase': ccxt.coinbasepro(),
}

symbol = 'BTC/USDT'
prices = {}

for name, exchange in exchanges.items():
    try:
        ticker = exchange.fetch_ticker(symbol)
        ask_price = ticker['ask']
        prices[name] = ask_price
        print(f"{name}: {ask_price}")
    except Exception as e:
        print(f"{name} ошибка: {e}")

if prices:
    best_exchange = min(prices, key=prices.get)
    best_price = prices[best_exchange]
    print(f"\n✅ Лучшая цена на BTC/USDT: {best_price} на бирже {best_exchange}")
else:
    print("❌ Не удалось получить данные с бирж.")

