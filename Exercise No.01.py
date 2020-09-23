#  Constant Values
feet_to_inches=12
inches_to_centimetre=2.54
snowboard_percent=88/100

#  Asking for height
print("Enter your height:")
feet=eval(input("Feet:"))
inches=eval(input("Inches:"))
height=(feet*feet_to_inches+inches)*inches_to_centimetre
snowboard=height*snowboard_percent
print("Your height:",height,"cm")
print("Suggested snowboard size",snowboard,"cm")