msg = input("Приветствие: ").strip().lower()

if msg.startswith("здравствуйте"):
    print("$0")
elif msg.startswith("з"):
    print("$20")
else:
    print("$100")
