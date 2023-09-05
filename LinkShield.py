import requests

# Function to check if the URL starts with http:// or https://
def url_checker(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        print("\033[31m[!] Invalid URL. Please use http or https.\033[0m")
        exit(1)

# Function to create a LinkShield URL
def create_linkshield_url(phishing_url, mask, words):
    response = requests.get(f"https://is.gd/create.php?format=simple&url={phishing_url}")
    short = response.text.strip()
    shorter = short.replace("https://", "")

    if not words:
        print("\033[31m[!] No words provided.\033[0m")
        final = f"{mask}@{shorter}"
    elif ' ' in words:
        print("\033[31m[!] Invalid words. Please avoid spaces.\033[0m")
        final = f"{mask}@{shorter}"
    else:
        final = f"{mask}-{words}@{shorter}"

    return final

def main():
    print("\n\u001b[31m  LinkShield - URL Protection Tool  \033[0m")
    print("\nBy smoke-wolf (GitHub: https://github.com/smoke-wolf)\n")

    phish = input("Enter the Phishing URL (with http or https): ")
    url_checker(phish)

    mask = input(
        '\nEnter the Domain to mask the Phishing URL (with http or https, e.g., https://google.com, http://anything.org): ')
    url_checker(mask)

    print('\nEnter social engineering words (e.g., free-money, best-pubg-tricks)')
    print("\033[31mDon't use spaces, use '-' between words.\033[0m")
    words = input("=> ")

    print("\nGenerating LinkShield URL...\n")
    final_url = create_linkshield_url(phish, mask, words)
    print(f"Here is the LinkShield URL: \033[32m{final_url}\033[0m\n")

if __name__ == "__main__":
    main()
