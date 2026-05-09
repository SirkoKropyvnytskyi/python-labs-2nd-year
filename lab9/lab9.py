import re

Slayer_Testament_text = "In the first age, in the first battle, doomslayer@gmail.com when the shadows first lengthened, one stood. Burned by the embers of Armageddon, his soul blistered by the fires of Hell and iconofsin@ukr.net tainted beyond ascension, he chose the path of perpetual torment. In his ravenous hatred he found no peace; and with boiling blood he scoured the Umbral Plains samuelhayden@yahoo.com seeking vengeance against the dark lords who had wronged him. He wore the crown of the Night Sentinels, and those that tasted the bile of his sword named him... the Doom Slayer."

email_found = re.findall(r'[\w\.-]+@[\w\.-]+', Slayer_Testament_text)

print("Found emails:")
for email in email_found:
    print(email)

try:
    with open("emails.txt", "w", encoding="utf-8") as file:
        for email in email_found:
            file.write(email + "\n")
    print("\nResults successfully saved to file 'emails.txt'.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")