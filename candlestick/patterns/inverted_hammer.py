from candlestick.patterns.candlestick_finder import CandlestickFinder


class InvertedHammer(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]
        
        prev_close = prev_candle[self.close_column]
        prev_open = prev_candle[self.open_column]
        prev_high = prev_candle[self.high_column]
        prev_low = prev_candle[self.low_column]

        return ((abs(high - low) >= 2.8 * abs(open - close)) and
                ((high - close) / (.001 + high - low) > 0.65) and
                ((high - open) / (.001 + high - low) > 0.65) and
                prev_open >= prev_close >= open)