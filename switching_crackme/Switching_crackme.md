
## Swithcing crackme writeup

This is a writeup for [Switching crackme](https://crackmes.one/crackme/6784563e4d850ac5f7dc5137) on crackmes.one created by cat_puzzler. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Initial-analysis">Initial analysis</a>
    </li>
    <li>
      <a href="#Ghidra-analysis">Ghidra analysis</a>
    </li>
    <li><a href="#Function-breakdown-(main)">Function breakdown (main)</a></li>
    <li><a href="#Function-breakdown-(check_id_xor)">Function breakdown (check_id_xor)</a></li>
    <li><a href="#Function-breakdown-(check_id_sum)">Function breakdown (check_id_sum)</a></li>
    <li><a href="#Return-to-the-main-function">Return to the main function</a></li>
    <li><a href="#Solution">Solution</a></li>
  </ol>
</details>

### Initial analysis

Trying to run the program gives the following result. It takes the serial key as an argument. 

```
user@user-VirtualBox:~/reverse_engineering/switching_crackme$ ./switching_crackme
Usage: ./crackme <key>
```

Using an incorrect password give the following error. 
```
user@user-VirtualBox:~/reverse_engineering/switching_crackme$ ./switching_crackme hello
Incorrect password

```
### Ghidra analysis

Decompiling the program in Ghidra gives a breakdown of the source code. Let's start by looking at the main function. I've renamed some of the variables based on an initial analysis. 

![image](https://github.com/user-attachments/assets/5d5354f9-f04c-4b3a-b6f0-d642684e0060)


### Function breakdown (main)

The main function performs 2 key tasks for determining if the password is correct:

The first is checking the length of the password entered by the user. The password must be at least 5 characters and must be no more than 254 characters, as shown in the screenshot below. 

![image](https://github.com/user-attachments/assets/f5a7bbb6-451e-4a45-91b5-26df47bfeda6)

Next, the main function checks the user input for characters. Only numbers are permitted in the password. 

![image](https://github.com/user-attachments/assets/613f34a8-f1d8-476d-ab96-d7efe1a00b7b)

This works by by getting the length of the user input using the strlen function, then using the strspn function to get a count of the numbers in the user's input. The values are then compared. The error function is called if they don't match. 

The error function simply writes "Incorrect password" to stdout and exits the program with  a -1.  

![image](https://github.com/user-attachments/assets/930dba9a-f1e9-43b5-bdd1-bfee1af27086)


After passing the password length and character check, two additional functions are called are called on the user's input to determine if the password is correct. 

![image](https://github.com/user-attachments/assets/92238a3d-4883-49f5-89d0-faf0ae045908)


### Function breakdown (check_id_xor)
check_id_xor works by converting the ascii value of a number to a hex value from an ascii char by subracting 0x30 from the value. Then it performs a basic XOR with the first character in the string against the last character of the string. 

![image](https://github.com/user-attachments/assets/e9a48b60-7d80-4a72-a9ee-14b61f4ecda1)

The result is then run through an if statement. If the result of the xor is less than the first character of the string or the last character in the string, the function returns a -1. If not, it returns the result of the XOR. 

![image](https://github.com/user-attachments/assets/ae424bf8-6541-42e4-abf5-e3e59c197442)

### Function breakdown (check_id_sum)
check_id_sum works by iterating through each character in the password, taking the int value of each character, then adding it to a value if it's index is even or subtracting it from the value if it's odd. 

![image](https://github.com/user-attachments/assets/6e56cf49-9f14-4f2a-b8e2-47288b2c3413)

Once this is completed with every character in the string, it then compares it to the XOR value returned from check_id_xor. If the value is equal to the XOR value it returns a 1. If the value is different or a -1 was returned from check_id_xor, the function returns a 0. 

![image](https://github.com/user-attachments/assets/9fe8cfe9-c9e6-438a-afd4-809612303b54)

### Return to the main function
The result of check_id_sum is verified to confirm  if the password is valid. If the returned result is 1, the password is valid, if not, it calls the error function and the password is not valid. 

![image](https://github.com/user-attachments/assets/410f1fce-21d1-4e88-b477-4756c6b55e5b)

### Solution
Based off the analysis of the program above, we can create a program that brute forces numbers that meet the password requirements. I chose to do this by rewriting each of the functions listed above in python and checking to see if the results match the criteria. The python script in this repo contains all of this information. Any number returned by this script will work as a password for the crackme challenge. 

