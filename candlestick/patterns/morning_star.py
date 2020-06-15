from candlestick.patterns.candlestick_finder import CandlestickFinder


class MorningStar(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 3, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]
        b_prev_candle = self.data.iloc[idx + 2 * self.multi_coeff]
        c_prev_candle = self.data.iloc[idx + 3 * self.multi_coeff]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        prev_close = prev_candle[self.close_column]
        prev_open = prev_candle[self.open_column]
        prev_high = prev_candle[self.high_column]
        prev_low = prev_candle[self.low_column]

        b_prev_close = b_prev_candle[self.close_column]
        b_prev_open = b_prev_candle[self.open_column]
        b_prev_high = b_prev_candle[self.high_column]
        b_prev_low = b_prev_candle[self.low_column]
        
        c_prev_close = c_prev_candle[self.close_column]
        c_prev_open = c_prev_candle[self.open_column]
        c_prev_high = c_prev_candle[self.high_column]
        c_prev_low = c_prev_candle[self.low_column]

        return (max(prev_open, prev_close) < b_prev_close < b_prev_open and
                close > open > max(prev_open, prev_close) and 
                c_prev_close < c_prev_open and 
                b_prev_open < c_prev_close)
