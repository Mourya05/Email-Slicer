def extract_email_details():
    email = input("Please enter your Email ID: ").strip()

    if "@" in email and email.count("@") == 1:
        username, domain = email.split('@')
        print(f"The username is: '{username}' and the domain is: '{domain}' for the provided Email ID.")
    else:
        print("Invalid Email ID. Please ensure it includes a single '@' symbol.")

extract_email_details()
