from candlestick.patterns.candlestick_finder import CandlestickFinder


class BearishEngulfing(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 2, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]

        open = candle[self.open_column]
        close = candle[self.close_column]


        prev_close = prev_candle[self.close_column]
        prev_open = prev_candle[self.open_column]
        
        return (open > prev_close > prev_open and
                open > close and
                prev_open >= close and 
                open - close > prev_close - prev_open)