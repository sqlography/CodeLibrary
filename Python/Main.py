def bye() -> None:
    print('Bye, World')

def main() -> None:
    bye()
    
if __name__ == '__main__':
    main()
    
def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

