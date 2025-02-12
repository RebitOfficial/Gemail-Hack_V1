import itertools
import time

# রঙের কোড
RED = "\033[91m"     # লাল রঙ (লোগো + পাসওয়ার্ড ট্রাইয়ের জন্য)
GREEN = "\033[92m"   # সবুজ রঙ (সফল মেসেজের জন্য)
RESET = "\033[0m"    # রঙ রিসেট

# ASCII লোগো (লাল রঙে প্রিন্ট হবে)
logo = RED + """
███╗░░░███╗██████╗░░░░
████╗░████║██╔══██╗░░░
██╔████╔██║██████╔╝░░░
██║╚██╔╝██║██╔══██╗░░░
██║░╚═╝░██║██║░░██║██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝

██████╗░███████╗██████╗░██╗████████╗
██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝
██████╔╝█████╗░░██████╦╝██║░░░██║░░░
██╔══██╗██╔══╝░░██╔══██╗██║░░░██║░░░
██║░░██║███████╗██████╦╝██║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░
""" + RESET

print(logo)  # লোগো প্রিন্ট
print( RED +"""************************************* 
*                                   *
* version    :   1.0.1              *  
*                                   *     
*                                   *
*                                   *
*                                   *
*************************************""")
# ইউজার থেকে Gmail ইনপুট নেওয়া
while True:
    email = input(GREEN + "🔹Enter Your Victim's Gmail: " + RESET)
    
    if email.endswith("@gmail.com"):
        break
    else:
        print(RED+ " Please Enter Correct Gmail.\n" + RESET)

print(GREEN + f"\n[*] Trying passwords for '{email}'...\n" + RESET)

# সঠিক পাসওয়ার্ড (শিক্ষামূলক, তাই এখানে একটি নির্দিষ্ট পাসওয়ার্ড ধরা হয়েছে)
correct_password = "p@ss"  # তুমি চাইলে এটা ইউজারের দেওয়া পাসওয়ার্ড লিস্ট থেকেও নিতে পারো

# সম্ভাব্য পাসওয়ার্ড সেট (সংখ্যা + ছোট হাতের + বড় হাতের অক্ষর + স্পেশাল ক্যারেক্টার)
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"

# পাসওয়ার্ডের দৈর্ঘ্য নির্ধারণ (যেমন: ৪ ক্যারেক্টারের পাসওয়ার্ড অনুমান)
password_length = 8

# সম্ভাব্য সব পাসওয়ার্ড চেক করা
password_found = False  # সঠিক পাসওয়ার্ড মেলানোর জন্য ফ্ল্যাগ

for guess in itertools.product(characters, repeat=password_length):
    guess = "".join(guess)  # অনুমিত পাসওয়ার্ড তৈরি
    
    if guess == correct_password:
        print(GREEN + f"✅ Password Matched: {guess}" + RESET)  # সঠিক পাসওয়ার্ড সবুজ রঙে দেখানো
        password_found = True
        break
    else:
        print(RED + f"[*] Trying: {guess}" + RESET)  # অনুমিত পাসওয়ার্ড লাল রঙে দেখানো
    time.sleep(0.1)  # প্রতিটি ট্রাইয়ের মাঝে সামান্য বিরতি (লোড কমানোর জন্য)

# যদি কোনো পাসওয়ার্ড না মেলে
if not password_found:
    print(RED + "\n❌ Password Not Found!" + RESET)