def play_ground(d1, d2):
    return round((3.141592 * 2 * d2 ) + (2 * d1), 6)


if __name__ == "__main__":
    d1 = int(input())
    d2 = int(input())
    
    print(play_ground(d1, d2))