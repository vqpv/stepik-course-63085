def create_file_with_numbers(n):
    with open(f'range_{n}.txt', 'w') as f:
        for num in range(1, n + 1):
            f.write(f'{num}\n')
