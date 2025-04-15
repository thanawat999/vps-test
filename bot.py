from strategies.news import run_news_strategy
from strategies.signal import run_signal_strategy
from strategies.dca import run_dca_strategy
from strategies.scalping import run_scalping_strategy
from mock_api import place_order

if __name__ == "__main__":
    print("Starting Forex Bot...")
    run_news_strategy()
    run_signal_strategy()
    run_dca_strategy()
    run_scalping_strategy()