u=(input())
try:
  if "." in u:
         val = float(u)
         print("yes")
  else:
          val = int(u)
          print("yes")
except ValueError:
       print("No")    
       
