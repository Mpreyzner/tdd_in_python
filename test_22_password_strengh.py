# https://github.com/xpepper/PasswordStrengthChecker
# optional, strong password generator

# Iteration 1
#
#     The length of the password must be at least 7 characters in length
#     The password must contain at least 1 letter
#     The password must contain at least 1 digit
#
# Iteration 2
#
# We need to add support for checking admin passwords
#
#     Admin passwords must be at least 10 characters in length
#     Admin passwords must contain at least 1 special character
#
# Iteration 3
#
# We need to provide feedback to the user about the strength of their password
#
#     Provide the user with a list of reasons why their password is 'weak'


def test_is_strong_password():
    assert is_string_password('a') is False
