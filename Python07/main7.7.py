from typing import Any


def output_even_key_args(**kwargs: dict[str, Any]) -> None:
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
            print(f'{key}: {value}')


if __name__ == "__main__":
    output_even_key_args(a='4', name='Vlad', word='Hello', value='No', os='Windows')
