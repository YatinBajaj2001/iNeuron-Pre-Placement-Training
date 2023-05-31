
def plusOne(digits):
    digitsString = "".join(map(str, digits))
    num = int(digitsString)
    result = list(map(int, str(num+1)))
    return result

if __name__ == "__main__":
    digits = [1,2,3]
    print(f"The output is {plusOne(digits=digits)}")