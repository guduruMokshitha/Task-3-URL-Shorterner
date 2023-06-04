import hashlib

# Shorten URL using MD5 hash
def shortenURL(url):
    # Generate MD5 hash of URL
    hash_object = hashlib.md5(url.encode())
    hash_hex = hash_object.hexdigest()

    # Take first 7 characters of hash and append to shortened URL
    shortened_url = hash_hex[:7]

    return shortened_url

# Main function to shorten a URL and display it
def main():
    url = input("Enter the URL to be shortened: ")

    shortened_url = shortenURL(url)

    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()