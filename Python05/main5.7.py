import random


def main():
    min_num = int(input('Input min value: '))
    max_num = int(input('Input max value: '))
    num_attempts = int(input('Input the number of attempts: '))
    target_number = random.randint(min_num, max_num)

    for attempt in range(num_attempts):
        print(f"Attempt {attempt + 1} of {num_attempts}")
        user_guess = int(input('Input your number: '))
        if user_guess == target_number:
            print('You are winner!')
            return
        elif user_guess < target_number:
            print('The hidden number is greater')
        else:
            print('The hidden number is less')

    print(f'You are loser. Number is: {target_number}')


if __name__ == '__main__':
    main()
