#simple ATM program 
balance = 50000
while True:
   print("\n====ATM MENU====")
   print("1.balance check")
   print("2.deposit")
   print("3.withdraw")
   print("4.Exit")

   choice = input("choose(1-4):")

   try:
      if choice == "1":
        print(" current Balance:", balance)
      elif choice == "2":
         amount = int(input("Depositamount:"))
         if amount <= 0:
            raise ValueError("amount must be greater  tha 0")
         balance += amount
         print("deposit successful")
         print("new balance:", balance)
      elif choice == "3":
         amount = int(input("withdraw amount:"))
         if amount <= 0:
            raise ValueError(" amount must be greaterthan 0")
         if amount > balance:
            raise Exception("Insufficient Balance!")
         balance -= amount
         print("withdrwa successful!")
         print("Remaining balance:", balance)
      elif choice == "4":
         print("thank you for using ATM")
         break
      else:
         print("Invalid choice!")
   except ValueError as e:
      print("Error:", e)
   except Exception as e:
      print("error:", e)
