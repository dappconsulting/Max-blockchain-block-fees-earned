# To calculate the maximum fees that can possible be earned given a set of 12 transactions for a block.
# I decided to represent the transaction byte size and fee per transaction with a python dictionary.

A = {15440 : 0.0250,29240 : 0.0532,63718 : 0.1147,70820 : 0.1409,77275 : 0.1522,98732 : 0.1856,143807 : 0.2660,40572 : 0.0686,57247 : 0.0887,134928 : 0.2307,139603 : 0.2541,190457 : 0.2933}
A2 = sorted(A.iteritems())
B = []
D = {}
sum_bytes = 0
sum_fees = 0

for tuple_item_index in range(len(A2)):
    B.append((A2[tuple_item_index][0])/(A2[tuple_item_index][1]))
    sum_bytes += A2[tuple_item_index][0]
    sum_fees += A2[tuple_item_index][1]
    D.update({A2[tuple_item_index][0]:(A2[tuple_item_index][0])/(A2[tuple_item_index][1])})

# I use the print output below as reference to sort the bytes/fee ratio from lowest to highest. The max fee needs to be calculated starting from lowest bytes/fee ratio to higher. The theory is that this approach should provide the maximum fee.
# I could eliminate the need for the below 3 print outputs, using shorter with code, but I'm still a python junior.
print ("Bytes:Fee dictionary: " + '\n' + str(A)) + '\n'
print ("BYTES:(bytes/fee) ratio list: " + '\n' + str(sorted(D.iteritems()))) + '\n'
print ("SORTED bytes/fee list: " + '\n' + str(sorted(B))) + '\n'
# adding up the transaction bytes corresponding bytes/fee ratio, starting from lowest bytes/fee ratio, it is clear that transaction of bytes = 190457 should be excluded, to prevent total bytes from exceeding 1000000 bytes
   
# Now I know to exclude transaction of byte length 190457 from below calculations.
print ("Sum of bytes = " + str(sum_bytes-190457) + " bytes")
print ("Total max fees earned = " + str((sum_fees-0.2933)+12.5) + " BTC")