def sub(a: int, b: int) -> int:
    return a - b

def sum(a: int, b: int) -> int:
    return a + b


def main():
    # docstring
    sub_res: int = sub(12, 8)
    print(sub_res)


if __name__ == '__main__':
    main()
