import sys
tens_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
twenties_words = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', "hundred"]


def main():
    try:
        while True:
            user_input = input()
            if user_input == "exit":
                sys.exit(0)
            print(number_to_word(int(user_input)))
    except SystemExit:
        sys.exit(0)

def number_to_word(number):
    if number == 0:
        return "zero"
    if 1 <= number <= 19: 
        return tens_words[number]
    elif 20 <= number <= 99:
        tens, below_ten = divmod(number, 10) 
        return twenties_words[tens - 2] + '-' + tens_words[below_ten]
    elif 100 <= number <= 999:
        return get_hundred(number)
    elif 1000 <= number <= 99999:
        return get_thousand(number)
    elif number == 100000:
        return "one hundred thousand"
    else:
        print("Number out of range. Only specify between 1-100000")


def get_tens(num):
    if 1 <= num <= 19: 
        return tens_words[num]
    elif 20 <= num <= 99:
        tens, below_ten = divmod(num, 10) 
        return twenties_words[tens - 2] + '-' + tens_words[below_ten]


def get_hundred(num):
    hundred, remainder = divmod(num, 100)
    if remainder == 0:
        return tens_words[hundred] + ' hundred'
    else:
        rem_res = get_tens(remainder)
        return tens_words[hundred] + ' hundred and ' + rem_res


def get_thousand(num):
    hundred, remainder = divmod(num, 1000)
    if remainder < 100:
        return get_tens(hundred) + ' thousand and ' + get_tens(remainder)
    result = get_tens(hundred) + ' thousand, ' + get_hundred(remainder) 
    return result