from client import AlgorithmicMarketSignalParserRiskOrderExecutorClient

def main():
    client = AlgorithmicMarketSignalParserRiskOrderExecutorClient()
    market = {"symbol": "ETH-USDT", "volatility_index": 0.32, "spread_bps": 4}
    res = client.evaluate_and_execute_signal(market, {"max_drawdown_limit": 0.02})
    print(f"Signal: {res['trade_signal']}")
    print(f"Position Sizing: {res['position_sizing_pct']}%")
    print(f"Risk Satisfied: {res['risk_constraint_satisfied']}")

if __name__ == "__main__":
    main()
