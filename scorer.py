def t_tennis(e_score: int):
    """Table tennis scorer: first to e_score with a two-point advantage."""
    h = 0
    a = 0
    print("Game to", e_score)
    while True:
        p = input("P (h/a): ").strip().lower()
        if p == "h":
            h += 1
        elif p == "a":
            a += 1
        else:
            print("Invalid input  enter 'h' or 'a'")
            continue
        print("Home:" + str(h), "Away:" + str(a))
        if (h >= e_score or a >= e_score) and abs(h - a) >= 2:
            winner = "Home" if h > a else "Away"
            print(winner, "Player wins")
            break


if __name__ == "__main__":
    import sys
    target = 5
    if len(sys.argv) > 1:
        try:
            target = int(sys.argv[1])
        except ValueError:
            print("Invalid target score, using default 5")
    t_tennis(target)
