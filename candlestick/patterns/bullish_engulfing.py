from candlestick.patterns.candlestick_finder import CandlestickFinder


class BullishEngulfing(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 2, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]
        b_prev_candle = self.data.iloc[idx + 2 * self.multi_coeff]

        close = candle[self.close_column]
        open = candle[self.open_column]


        prev_close = prev_candle[self.close_column]
        prev_open = prev_candle[self.open_column]

        
        b_prev_close = b_prev_candle[self.close_column]

        return (close >= prev_open > prev_close and
                close > open and
                prev_close >= open and
                close - open > prev_open - prev_close and 
                prev_close < b_prev_close)
