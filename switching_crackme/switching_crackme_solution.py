'''
This is a solution to the switching crackme found on crackmes.one. This is the algorithm from the crackme written in python. 
The crackme has a wide range of acceptable solutions. The script below generates numbers from 00000 to 99999 and prints thenumbers that correctly solve the crackme. This script generates correct answers that are 5 characters in length. 
This can be changed by editing the code below. The crackme will accept numbers ranging from 5 to 254 characters. Anything out of this range will automatically fail.

'''

def check_id_xor(pw):
    # XOR the value of the first character with the value of the last and return the result.
    passwd = int(pw[0])
    passwd_len = len(pw)
    result = (passwd) ^ (int(pw[passwd_len - 1]))
    # The XOR result cannot be smaller than the value of the first character or smaller than the last.
    if result < passwd or result < (int(pw[passwd_len - 1])):
        return -1
    else:
        return result
    
def check_id_sum(pw, xor_pw):
    # Iterate through each value on the list starting with 1 and procceding the rest of the key length. 
    i = 0
    j = 1
    while(True):
        pw_len = len(pw)
        if pw_len - 1 <= j:
        #if pw_len <= j:
            break
        # If the value is at an even index, subtract it from i, if it's at an odd index, add it to i
        if (j & 1) == 0:
            passwd = -(int(pw[j]))
        else:
            passwd = (int(pw[j]))
        i = i + passwd
        j = j + 1
    # At the end of the loop, compare the value of i to the previous XOR value. Return a value of 1 if it meets the requirements
    if i == xor_pw and xor_pw != -1:
        result = 1
    else:
        result = 0
    return result

def generate_numbers():
    # Iterates from 00000 to 99999. Add zeros to the range and increase the value for zfill by the # of zeros to generate numbers of varying lenths. 
    # Just make sure the numbers match for valid results
    for pin in range(100000):
    # Format the number as a 5-digit string with leading zeros
        pin_str = str(pin).zfill(5)
        xor_num = check_id_xor(pin_str)
        check_result = check_id_sum(pin_str, xor_num)
        # Print the number if it meets the algorithm criteria. 
        if check_result == 1:
            print(pin_str)



if __name__ == "__main__":
    generate_numbers()

