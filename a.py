# Triangular Arbitrage

# Exchange rates
sf_per_usd = 1.5971 
aud_per_usd = 1.8215
aud_per_sf = 1.144


# define Arbitrage class
class Cross_Rate_Arbitrage:

  def __init__(self, B_per_A, C_per_A, C_per_B):
    self.B_per_A = B_per_A 
    self.C_per_A = C_per_A
    self.C_per_B = C_per_B

  def check_arbitrage(self):
    print('1. Checking for arbitrage opportunity')
     
    direct = self.C_per_A 
    indirect = self.B_per_A * self.C_per_B
    print(direct- indirect)
    
    if direct == indirect:
      print("No arbitrage opportunity")
      self.is_arbitrage = False
    else:
      print("Yes, arbitrage opportunity exists")  
      self.is_arbitrage = True

  def arbitrage_steps(self):
    print('2. Steps to make arbitary profit')
    if self.is_arbitrage:
      print('Step 1: Convert his funds to the currency quoted cheaper in indirect rate')
      print('Step 2: Convert that currency to the one quoted higher in direct rate')
      print('Step 3: End up with more funds in original currency after the trades')

  def calculate_profit(self, amount):
    print('3. Culculate arbitary profit')
    if self.is_arbitrage:
      profit_in_C = amount * (self.B_per_A * self.C_per_B - self.C_per_A) 
      profit_in_A = profit_in_C / self.C_per_A
      print(f"Arbitrage profit on $ {amount} is $ {profit_in_A}")
    else:
      print("No profit")

# Answer
arb = Cross_Rate_Arbitrage(sf_per_usd, aud_per_usd, aud_per_sf)  
arb.check_arbitrage()
arb.arbitrage_steps()
arb.calculate_profit(1000000)
