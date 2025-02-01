class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


MIN_PASSWORD_LENGTH = 8
SPECIAL_CHARACTERS = ('@', '*', '%', '&')
while True:
    pasw = input()
    if pasw == "Done":
        break

    if len(pasw) < MIN_PASSWORD_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if pasw.isalpha() or pasw.isdigit() or all(c in SPECIAL_CHARACTERS for c in pasw):
        raise PasswordTooCommonError("Password must be a combination of digits,"
                                     " letters, and special characters")

    if not any(c in SPECIAL_CHARACTERS for c in pasw):
        raise PasswordNoSpecialCharactersError("Password must contain at "
                                               "least 1 special character")

    if " " in pasw:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print('\nPassword is valid')
