n: int = 1_000_000 #readable for developer
print(n)

print(f'{n:_}') #prints with _ for 1000s spacing
print(f'{n:,}') #same thing as above except with a comma


varstr: str = 'Var'
print(f'{varstr:>20}') #right justify
print(f'{varstr:<20}') #left justify
print(f'{varstr:^20}') #center
print(f'{varstr:_>20}') #right justify with _
print(f'{varstr:|<20}') #left justify with pipes
print(f'{varstr:8^20}') #center with the number 8


from datetime import datetime
now: datetime = datetime.now()
print(f'{now:%d.%m.%y (%H:%M:%S)}') #used to format date and time.

N: float =1234.6578888
print(f'{N:.2f}') #format decimal to specified precision.
print(f'{N:,.2f}') #format decimal to specified precision and put commas

a: int = 5
b: int = 10
print(f'{a + b = }') #prints the text with calculation