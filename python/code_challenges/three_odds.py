def three_consecutive_odds(input_list):
    if len(input_list) < 3:
        return None

    counts = {}
    consec_count = 0

    for num in input_list:
        if num % 2 == 1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

            consec_count += 1
            if consec_count == 3:
                return True
        else:
            counts = {}
            consec_count = 0

    return False
