# CRC Error Detection Program

This is a program that implements error detection using the CRC(Cyclic Redundancy Check) algorithm. 

The program generates a message(in the form of a string of k bits) and with the generator polynomial (also in the form of a string of bits), that the user gives, calculates the CRC. Then the message and CRC are transmitted over a wireless channel  with BER(Bit Error Rate) and the recepient receives the corrupted message.
After that the program gives as an output the numbers of the corrupted messages, the messages that have been detected as corrupted and those who have not.

# Usage 

To use the CRC error detection program, simply run the crc.py file with Python, passing in the number of the messages, the bit number of the messages and generator polynomial as arguments:

```python 
Give number of messages 10000
Give number of bits 6
Give generator polynomial 110101
```


The program will output the number of corrupted messages, the messages that have been detected with error or not:

``` python
Corrupted Messages:  101
Error Detected:  101
Messages that has't  been detected 0
```
