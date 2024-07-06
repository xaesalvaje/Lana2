from data_handler import DataHandler
from strategy import Strategy
from backtest import Backtester
from train_bot import BotTrainer
from config_utils import Config

def main():
    # Load configuration
    config = Config.load_config("config.json")
    
    # Initialize components
    data_handler = DataHandler(config)
    strategy = Strategy(config)
    backtester = Backtester(config)
    trainer = BotTrainer(config)
    
    # Example workflow
    data = data_handler.get_data()
    strategy_results = strategy.apply(data)
    backtest_results = backtester.run(strategy_results)
    trainer.train(strategy_results)
    
    # Output results
    print("Backtest Results:", backtest_results)

if __name__ == "__main__":
    main()
