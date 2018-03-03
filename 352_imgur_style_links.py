base62_alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base10_to_base62(number, accumulator):
    quotient = number // 62
    remainder = number % 62
    base62_remainder = base62_alphabet[remainder]
    
    if quotient == 0:
        return base62_remainder + accumulator
    else:
        return base10_to_base62(quotient, base62_remainder + accumulator)

    
