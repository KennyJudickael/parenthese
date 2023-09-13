def generate_parentheses_combinations_score(n, current="", score=0):
    if len(current) == 2 * n:
        if score == 0:
            return [current]
        return []

    combinations = []

    if score < n:
        combinations += generate_parentheses_combinations_score(
            n, current + "(", score + 1
        )

    if score > 0:
        combinations += generate_parentheses_combinations_score(
            n, current + ")", score - 1
        )

    return combinations


def main():
    n = int(input("Entrez la valeur de n : "))
    valid_combinations = generate_parentheses_combinations_score(n // 2)

    print("Combinaisons valides :")
    for combination in valid_combinations:
        print(combination)


if __name__ == "__main__":
    main()
