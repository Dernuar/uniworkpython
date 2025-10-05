def main(x, *args):
    amount = x
    return sum(args)

if __name__ == '__main__':
    result = main(3, 2, 1, 3)
    print(f'Summary of numbers: {result}')
