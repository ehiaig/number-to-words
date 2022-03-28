
import argparse 

tens_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
twenties_words = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', "Hundred"]


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("number",type=int)
    args = parser.parse_args()
    print(number_to_word(args.number).lower())

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
        return "One hundred thousand"
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
        return tens_words[hundred] + ' Hundred'
    else:
        rem_res = get_tens(remainder)
        return tens_words[hundred] + ' Hundred and ' + rem_res


def get_thousand(num):
    hundred, remainder = divmod(num, 1000)
    if remainder < 100:
        return get_tens(hundred) + ' Thousand and ' + get_tens(remainder)
    result = get_tens(hundred) + ' Thousand, ' + get_hundred(remainder) 
    return result
    
main()