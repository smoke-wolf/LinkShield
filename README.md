

LinkShield - URL Protection Tool
================================

LinkShield is a command-line tool for protecting phishing URLs by masking them with a specified domain and optional social engineering words. It generates a LinkShield URL that redirects to the original phishing URL, making it harder to recognize and more appealing to potential victims.

Usage
-----

bashCopy code

`python3 LinkShield.py "phishing_url" "mask" -w "social-engineering-words"`

### Arguments:

-   `"phishing_url"` (required): The phishing URL to be protected. It should start with either `http://` or `https://`.

-   `"mask"` (required): The domain to mask the phishing URL. It should also start with either `http://` or `https://`.

-   `-w, --words` (optional): Social engineering words separated by '-' (e.g., `free-money`, `best-pubg-tricks`). Avoid using spaces.

If any of the required arguments are not provided, the tool will prompt you for input.


# 
## New Build (gui)

    Usage: 1. Enter the phishing URL
    in the 'Phishing URL' field. 
    2. Enter the domain to mask the phishing URL in the 'Domain to mask the Phishing URL' field. 
    3. Optionally, enter social engineering words separated by '-' in the 'Social engineering words separated by '-' field. 
    4. Click the 'Generate LinkShield URL' button to create the  

The link will be printed in the terminal.
