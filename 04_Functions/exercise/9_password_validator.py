def password_validation(pw):
    length_password, minimum_symbols, max_symbols = len(pw), 6, 10
    valid_password = True
    if minimum_symbols > length_password or length_password > max_symbols:
        print("Password must be between 6 and 10 characters")
        valid_password = False
    for checking_for_numbers_and_letters in pw:
        if checking_for_numbers_and_letters.isdigit() or checking_for_numbers_and_letters.isalpha():
            continue
        else:
            valid_password = False
            print("Password must consist only of letters and digits")
            break
    checker_count_digit = len(list(filter(lambda x: x.isdigit(), pw)))
    if checker_count_digit < 2:
        print("Password must have at least 2 digits")
        valid_password = False
    if valid_password:
        print("Password is valid")


password = input()
password_validation(password)