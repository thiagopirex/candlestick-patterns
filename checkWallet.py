from yahoo_fin.stock_info import get_data
from datetime import date, timedelta
from candlestick import candlestick


# List of active on https://finance.yahoo.com/cryptocurrencies

has_pattern = False
lastDays = 5
UP = set()
DOWN = set()
UP_dict = dict()
DOWN_dict = dict()
candles_df = ''
today = date.today()
myWallet = {'VALE3', 'PETR4', 'WEGE3', 'LREN3', 'AMAR3', 'ALSO3', 'CRFB3', 'SEER3', 'SQIA3', 'EMBR3', 'POMO4', 'ECOR3', 'AZUL4', 'GOLL4',
            'CNTO3', 'VVAR3', 'ALPA4', 'ITUB4', 'MGLU3', 'BBAS3', 'B3SA3', 'CYRE3', 'HGTX3', 'BBDC4', 'ITSA4', 'ABEV3', 'USIM5', 'GGBR4', 
            'ENEV3', 'CESP6', 'YDUQ3', 'SMTO3', 'FLRY3', 'BRFS3', 'ABCB4', 'RAPT4', 'CSMG3', 'RENT3', 'LAME4', 'BRML3', 'CCRO3', 'TOTS3',
            'TAEE11', 'TIET11', 'KLBN11', 'ALUP11', 
            'LOGN3', 'CSNA3', 'CSAN3', 'RADL3', 'EQTL3', 'BEEF3', 'IRBR3', 'MILS3', 'CIEL3', 'RAIL3', 'COGN3', 'GNDI3', 'EGIE3', 'SHUL4',
            'ARZZ3', 'QUAL3', 'RADL3', 'LIGT3', 'UGPA3', 'EZTC3', 'NTCO3', 'JHSF3', 'PCAR3', 'CAML3', 'MILS3', 'BRDT3', 'BRKM5', 'SUZB3',
            'PCAR3', 'SLCE3', 'BTOW3', 'CCRO3'}



#start date set to today minus ?? days
startDate = date.today() - timedelta(lastDays)

def piercing_pattern():
    target='PiercingPattern'
    check = candlestick.piercing_pattern(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)
def hanging_pattern():
    target='HangingMan'
    check = candlestick.hanging_man(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        DOWN.add(target)
def bullish_engulfing():
    target='BullishEngulfing'
    check = candlestick.bullish_engulfing(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)
def bearish_engulfing():
    target='BearishEngulfing'
    check = candlestick.bearish_engulfing(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        DOWN.add(target)
def hammer():
    target='Hammer'
    check = candlestick.hammer(candles_df)
    df_pattern = check[check[target] == True] 
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)
def eveningStar():
    target='EveningStar'
    check = candlestick.evening_star(candles_df)
    df_pattern = check[check[target] == True] 
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        DOWN.add(target)
def morningStar():
    target='MorningStar'
    check = candlestick.morning_star(candles_df)
    df_pattern = check[check[target] == True] 
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)
def inverted_hammer():
    target='InvertedHammer'
    check = candlestick.inverted_hammer(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)
def shoting_star():
    target='ShootingStar'
    check = candlestick.shooting_star(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        DOWN.add(target)
def bullish_harami():
    target='BullishHarami'
    check = candlestick.bullish_harami(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        UP.add(target)    
def bearish_harami():
    target='BearishHarami'
    check = candlestick.bearish_harami(candles_df)
    df_pattern = check[check[target] == True]
    if (not df_pattern.empty and len(df_pattern) > 0 and last_date.values == df_pattern.tail(1)['date'].values):
        DOWN.add(target)
              
for active in myWallet:
    
    #get values from start date
    candles_df = get_data(active + ".SA", start_date = startDate,  index_as_date = False)
    last_date = candles_df.tail(1)['date']
    print("Checking... " + active)

    #check patterns
    if (len(candles_df) > 1):
        piercing_pattern()
        bullish_engulfing()
        bearish_engulfing()
        bearish_harami()
        hammer()
        eveningStar()
        morningStar()
        inverted_hammer()
        shoting_star()
        bullish_harami()
        hanging_pattern()
    else:
        print("Not enough data for " + active)
        print(candles_df)
    
    if len(UP) > 0:
        has_pattern = True
        UP_dict[active] = UP
        UP = set()
    
    if len(DOWN) > 0:
        has_pattern = True
        DOWN_dict[active] = DOWN
        DOWN = set()
    
print("______________________________________________________________")
if has_pattern:
    
    if UP_dict:
        print("HIGH standard found! This active need your check: ")
        for key, value in UP_dict.items():
            print('  - ' + key, ":", value)

    if DOWN_dict:
        print("BEARISH standard found! This active need your check: ")
        for key, value in DOWN_dict.items():
            print('  - ' + key, ":", value)
else:
    print("No cookies for you today!") 
    

