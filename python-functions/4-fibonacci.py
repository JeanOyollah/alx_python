def fibonacci_sequence(n):
    if n <= 0:
        return

    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence
#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_iseq = [0, 1]
        while len(fib_iseq) < n:
            next_fib = fib_iseq[-1] + fib_iseq[-2]
            fib_iseq.append(next_fib)
        return fib_iseq
