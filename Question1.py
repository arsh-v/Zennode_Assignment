price = [20.0, 40.0, 50.0]

A = float(input("Enter the Quantity of product A: "))
a1 = input("Do you want to wrap product A as a Gift (Y/N): ")

B = float(input("Enter the Quantity of product B: "))
b1 = input("Do you want to wrap product B as a Gift (Y/N): ")

C = float(input("Enter the Quantity of product C: "))
c1 = input("Do you want to wrap product C as a Gift (Y/N): ")

ten = 10.0
zero = 0.0

cartTotal = A * price[0] + B * price[1] + C * price[2]
giftTotal = (A if a1 == 'Y' else 0) + (B if b1 == 'Y' else 0) + (C if c1 == 'Y' else 0)
shippingCost = int(A + B + C + 9) // 10 * 5

totalItems = A + B + C

flat_10_discount = 0
bulk_5_discount = (price[0] * A * 0.05 if A > 10 else 0) + (price[1] * B * 0.05 if B > 10 else 0) + (price[2] * C * 0.05 if C > 10 else 0)
bulk_10_discount = cartTotal * 0.1 if (A + B + C) > 20 else 0

tiered_50_discount = 0
if (A + B + C) > 30:
    tiered_50_discount += (A - 15) * (price[0] / 2) if A > 15 else 0
    tiered_50_discount += (B - 15) * (price[1] / 2) if B > 15 else 0
    tiered_50_discount += (C - 15) * (price[2] / 2) if C > 15 else 0

mxDiscount = 0
discountType = "None"

if mxDiscount < 10:
    mxDiscount = 10
    discountType = "flat_10_discount"

if mxDiscount < bulk_5_discount:
    mxDiscount = bulk_5_discount
    discountType = "bulk_5_discount"

if mxDiscount < bulk_10_discount:
    mxDiscount = bulk_10_discount
    discountType = "bulk_10_discount"

if mxDiscount < tiered_50_discount:
    mxDiscount = tiered_50_discount
    discountType = "tiered_50_discount"

finalCost = cartTotal - mxDiscount
finalCost += giftTotal
finalCost += shippingCost

print(f"Product Name: A  Quantity : {A}  Cost : {A * price[0]}")
print(f"Product Name: B  Quantity : {B}  Cost : {B * price[1]}")
print(f"Product Name: C  Quantity : {C}  Cost : {C * price[2]}")
print(f"SubTotal : {cartTotal}")
print(f"The discount name applied & the discount amount : {discountType}  {mxDiscount}")
print(f"The shipping fee & the gift wrap fee : {giftTotal + shippingCost}")
print(f"Total Cost: {finalCost}")
