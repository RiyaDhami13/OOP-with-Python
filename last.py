# Print numbers from 1 to 30, skipping multiples of 3

def main():
    for num in range(1, 31):
        # Skip numbers divisible by 3
        if num % 3 == 0:
            continue
        print(num)

if __name__ == "__main__":
    main()


