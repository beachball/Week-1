# Python Program - Convert Binary to Octal

print("Enter 'x' for exit.");
binary = input("Enter any number in Binary Format: ");
if binary == 'x':
    exit();
else:
    temp = int(binary, 2);
    print(binary,"in Octal =",oct(temp));




    if agroup == "000":
        output = output + "0"
    if agroup == "001":
        output = output + "1"
    if agroup == "010":
        output = output + "2"
    if agroup == "011":
        output = output + "3"
    if agroup == "100":
        output = output + "4"
    if agroup == "110":
        output = output + "5"
    if agroup == "111":
        output = output + "6"
    count = count + 3
