if __name__ == "__main__":
    test_list = ['Vlad', 'Vladimir', 'Nikita', 'Kate']
    names_with_k = list(filter(lambda name: 'k' in name.lower(), test_list))
    print(names_with_k)
