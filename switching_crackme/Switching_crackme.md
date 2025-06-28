
## Getting Started

This is a writeup for [Switching crackme](https://crackmes.one/crackme/6784563e4d850ac5f7dc5137) on crackmes.one created by cat_puzzler. 

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

![image](https://github.com/user-attachments/assets/34dfc655-20e4-413e-a080-81b4b102fae1)


### Function breakdown (main)

The main function performs 2 key tasks for determining if the password is correct:

The first is checking the length of the password entered by the user. The password must be at least 5 characters and must be no more than 254 characters, as shown in the screenshot below. 
![[Pasted image 20250621095945.png]]

Next, the main function checks the user input for characters. Only numbers are permitted in the password. 

![[Pasted image 20250621101351.png]]

This works by by getting the length of the user input using the strlen function, then using the strspn function to get a count of the numbers in the user's input. The values are then compared. The error function is called if they don't match. 

The error function simply writes "Incorrect password" to stdout and exits the program with  a -1.  

![[Pasted image 20250628102013.png]]


After passing the password length and character check, two additional functions are called are called on the user's input to determine if the password is correct. 

![[Pasted image 20250621102214.png]]

### Function breakdown (check_id_xor)
check_id_xor works by converting the ascii value of a number to a hex value from an ascii char by subracting 0x30 from the value. Then it performs a basic XOR with the first character in the string against the last character of the string. 
![[Pasted image 20250628095006.png]]

The result is then run through an if statement. If the result of the xor is less than the first character of the string or the last character in the string, the function returns a -1. If not, it returns the result of the XOR. 

![[Pasted image 20250628095109.png]]
### Function breakdown (check_id_sum)
check_id_sum works by iterating through each character in the password, taking the int value of each character, then adding it to a value if it's index is even or subtracting it from the value if it's odd. 
![[Pasted image 20250628100513.png]]
Once this is completed with every character in the string, it then compares it to the XOR value returned from check_id_xor. If the value is equal to the XOR value it returns a 1. If the value is different or a -1 was returned from check_id_xor, the function returns a 0. 

### Return to the main function
The result of check_id_sum is verified to confirm  if the password is valid. If the returned result is 1, the password is valid, if not, it calls the error function and the password is not valid. 

![[Pasted image 20250628102102.png]]

### Solution
Based off the analysis of the program above, we can create a program that brute forces numbers that meet the password requirements. I chose to do this by rewriting each of the functions listed above in python and checking to see if the results match the criteria. The python script in this repo contains all of this information. Any number returned by this script will work as a password for the crackme challenge. 



1. 
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
