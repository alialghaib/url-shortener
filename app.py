from shortener import load_data, shorten, expand

def main():
    data = load_data()
    print("📦 Welcome to CLI URL Shortener")
    while True:
        print("\nOptions:")
        print("1. Shorten URL")
        print("2. Expand short code")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            url = input("Enter the long URL: ")
            code = shorten(url, data)
            print(f"Short code: {code}")

        elif choice == '2':
            code = input("Enter the short code: ")
            url = expand(code, data)
            if url:
                print(f"Original URL: {url}")
            else:
                print("❌ Code not found.")

        elif choice == '3':
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
