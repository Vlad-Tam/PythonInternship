if __name__ == "__main__":
    test_list = ['Vlad', 'Vladimir', 'Nikita']
    result = map(lambda x: f'Hello {x}', test_list)
    print(list(result))
