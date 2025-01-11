<<<<<<< HEAD
def hello():
    print("hi")


def bye():
    print("bye")


print(hello())
import
import numpy as np

def generate_10_random(n_numbers : int):
    return np.random.randint(0, 1000, n_numbers)
    
def return_bigger(numbers : np.ndarray):
    pos_bigger = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[pos_bigger]:
            pos_bigger = i
    return numbers[pos_bigger]

def main():
    numbers = generate_10_random(10)
    print(numbers)
    print(return_bigger(numbers))

if __name__ == "__main__":
    main()
>>>>>>> c6d85ce (Testing github actions!)
