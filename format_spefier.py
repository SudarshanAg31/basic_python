# format specifiers = {:flags} format a value based on what flags are inserted
x=34334554.3545
y=-434442.5253
z=454443.4545
# := = place sign to leftmost position
# :% = percentage format

# .(number)f = round to that many decimal places
print(f"print x: {x:.2f}")
# :(number) = allocate that many spaces
print(f"print y: {y:10}")
# :0(number) = allocate and zero pad that many spaces
print(f"print z: {z:010}")
# :< = left justify(space from right)
print(f"print x: {x:<10}")
# :> = right justify(space form left)
print(f"print x: {x:>30}")
# :^ = center align
print(f"print x: {x:^10}")
# :+ = use a plus sign to indicate positive value
print(f"print x: {x:+}")
print(f"print y: {y:+}")#if value is -ve so it print - sign 
# :  = insert a space before positive numbers
print(f"print x: {x: }")
print(f"print y: {y: }")
# :, = comma separator
print(f"print x: {x:,}")

#example
print(f"print x: {x:+,.2f}")

