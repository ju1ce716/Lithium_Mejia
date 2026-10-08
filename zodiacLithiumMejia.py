#Ask the user to input a year of birth and validate input as real number
year_input = input("Enter your year of birth: ")
try:
    year = int(year_input)
except ValueError:
    print("Invalid input. Please enter a valid year.")
    raise SystemExit
    
#Validate that the year is not earlier than 1900
if year < 1900:
    print("Invalid year. The year of birth must be 1900 or later.")
    raise SystemExit
    
#List chinese zodiac signs starting with Rat in 1900
zodiac_signs = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
]

#Determine the zodiac sign using the 12-year cycle then print result
zodiac_index = (year - 1900) % 12
zodiac_sign = zodiac_signs[zodiac_index]
print(f"Your Chinese zodiac sign is: {zodiac_sign}")
