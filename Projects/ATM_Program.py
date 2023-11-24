import sys
import os
class Bank:
	'''demo bank application of section 2C'''
	bankname='2C Bank'
	def __init__(self,name,balance=0.0):
		
		self.name=name
		
		self.balance=balance
		print("Welcome:",self.name)
	def deposit(self,amt):
		self.balance=self.balance+amt
		print("Dear ",self.name," Your Balance after deposit is:",self.balance)
	def withd(self,amt):
		if amt>self.balance:
			print("Dear ",self.name," Your Balance is not sufficient to be widhdrawn:")
			sys.exit()
		self.balance=self.balance-amt
		print("Dear ",self.name," Your Balance after widhdraw is:",self.balance)
print("Welcome to:",Bank.bankname)
name=input("Enter your name:")
c=Bank(name)
while True:
	print("d: For Deposit\nw: For Withdraw\nb: For Balance\ne: For exit")
	option=input("Choose Your Option:")
	if option.lower()=='d':
		amt=float(input("Enter the amount to be deposited:"))
		c.deposit(amt)
	elif option.lower()=='w':
		amt=float(input("Enter the amount to be withdrawn:"))
		c.withd(amt)
	elif option.lower()=='b':
		print("Your current balance is:",c.balance)
	elif option.lower()=='e':
		print("Thanks for banking with us!!")
		sys.exit()
	else:
		print("Choose correct Option!!")