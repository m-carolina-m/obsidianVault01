6/2/18, 5:35 AM

open_order=true or false

Current_order='buy', 'sell' or 'hold'

If strategy=1
  If p>kc 
      If  ts>ks & not open_order:
             Current_order=buy
             Open_order=True
     Elif ts=ks & open_order:
             Current_order=sell
             Open_order=false
  Elif p<kc 
      If ts<ks & not open_order:
             Current_order=sell
             Open_order=true
      Elif ts=ks & open_order:
             Current_order=buy 
             Open_order=false
ElIf strategy=2
 If p>kc 
      If  P>Ts & not open_order:
             Current_order=buy
             Open_order=True
             Stop-loss p=Ts
     Elif P<Ts & open_order:
             Current_order=sell
             Open_order=false
  Elif p<kc 
      If P<Ts & not open_order:
             Current_order=sell
             Open_order=true
             Stop-loss P=Ts
      Elif P>Ts & open_order:
             Current_order=buy 
             Open_order=false
ElIf strategy=3
 If p>kc 
      If  P>Sb & not open_order:
             Current_order=buy
             Open_order=True
             Stop-loss p=Sb
     Elif P<Sb & open_order:
             Current_order=sell
             Open_order=false
  Elif p<kc 
      If P<Sb & not open_order:
             Current_order=sell
             Open_order=true
             Stop-loss P=Sb
      Elif P>Sb & open_order:
             Current_order=buy 
             Open_order=false
ElIf strategy=4
 If p>kc 
      If  P<Ks & P>Ts & not open_order:
             Current_order=buy
             Open_order=True
             Stop-loss low before buy
     Elif          open_order:
             Current_order=sell
             Open_order=false
  Elif p<kc 
      If P<Ts & P>Ks & not open_order:
             Current_order=sell
             Open_order=true
             Stop-loss High before sell
      Elif         & open_order:
             Current_order=buy 
             Open_order=false

If current_order=buy:
    Buy
    Stoploss
    Current_order='hold'
Elif current_order=sell:
     Sell
     Stoploss
     Current_order='hold'

[https://youtu.be/LKDJQLrXedg](https://youtu.be/LKDJQLrXedg)


Bullish:
1.Close> TS 
2.TS in increasing slope
3.Close> Ks
4.KS in increasing slope
5.CS>Close-26p
6.CS not going to touch Close-26p to close-21p or 16p
7.CS+-5% or 10% not going to touch Close-26p
8.Close>KC
9.SA+26p>SB+26p
10.SA+26p in increasing slope 
11.Small distance between SA+26p and SB+26p (future cloud thickness, thick means short term trend)

Resistance value:
1.CS peak
2.SB flat
3.SA peak

Strat:
buy...
1.Close>KC
2.TS>KS
3.CS>Close-26p
4.CS not going to touch Close-26p to close-21p or 16p
5.CS+-5% or 10% not going to touch Close-26p
6.Close>Resistance value+50pips
7.SA+26p>SB+26p
8.SA+26p in increasing slope 
9.Close+200pips<TS
10.Close+300pips<KS
11.set stoploss 40pips below TS*
12. TS increasing slope
13. KS increasing slope


Exit...
1. if Close+200pips>TS and TS is flat
2. If profit>300pips and Close<TS-40pips
3. If Close<KS

Adjust...
1. Stoploss daily to TS-40pips
2. Set alarm for CS touching Close-26p
3. Set bearish alarm below SA if future cloud thickness big or below KS if future cloud thickness is small
4. Set bullish alarm above CS highest peak 

