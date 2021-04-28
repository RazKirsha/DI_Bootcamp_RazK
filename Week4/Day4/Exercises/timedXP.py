def count_occr (str, letter):
    counter = 0
    for let in str:
        if let == letter:
            counter += 1
    print(counter)

count_occr('Programming is cool!', 'o')