for m in range(1, 4):
  print(f'current iteration: {m}')
  print(f'-' * 30)
  for n in range(1, 5):
    print(f'-' * 15)
    print(f'current loop: {n}')
    print(f'(m = {m}) (n = {n})')
    print(f'{m} x {n} = {m * n}')
  print(f'-' * 15)
    