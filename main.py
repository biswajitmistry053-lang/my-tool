import os, phonenumbers
from phonenumbers import geocoder, carrier, timezone
R="\033[91m";G="\033[92m";Y="\033[93m";W="\033[97m";C="\033[96m"
def banner():
 os.system("clear")
 print(f"{C}=== Biswajit's OSINT Tool ===")
while True:
 banner()
 print(f"{Y}[1]{W} My IP Info")
 print(f"{Y}[3]{W} Phone Info")
 print(f"{Y}[4]{W} Instagram Info")
 print(f"{Y}[0]{W} Exit")
 ch=input(f"\n{C}Choice: {W}")
 if ch=="1":
  os.system("curl -s ipinfo.io")
  input(f"\n{Y}Press Enter...")
 elif ch=="3":
  num=input(f"{W} Phone +91: {C}")
  try:
   if not num.startswith("+"): num="+"+num
   ph=phonenumbers.parse(num)
   print(f"{G} Valid: {W}{phonenumbers.is_valid_number(ph)}")
   print(f"{G} Country: {W}{geocoder.description_for_number(ph,'en')}")
   print(f"{G} Carrier: {W}{carrier.name_for_number(ph,'en')}")
   print(f"{G} TimeZone: {W}{timezone.time_zones_for_number(ph)}")
  except Exception as e: print(f"{R} Error: {e}")
  input(f"\n{Y}Press Enter...")
 elif ch=="4":
  user=input(f"{W} Insta Username: {C}")
  print(f"{Y} Instagram blocking without login. Need login tool.")
  input(f"\n{Y}Press Enter...")
 elif ch=="0": break
