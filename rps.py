import logging

# 0 = Rock; 1 = Paper; 2 = Scissors #
def rps_check_win(player_1_weapon, player_2_weapon):
    match player_1_weapon:
        case 0:
            match player_2_weapon:
                case 0:
                    return 0
                case 1:
                    return 2
                case 2:
                    return 1
                case _:
                    logging.exception("unknown Value returned from player 2 on RPS case 0")
                    raise ValueError
        case 1:
            match player_2_weapon:
                case 0:
                    return 1
                case 1:
                    return 0
                case 2:
                    return 2
                case _:
                    logging.exception("unknown Value returned from player 2 on RPS case 1")
                    raise ValueError
        case 2:
            match player_2_weapon:
                case 0:
                    return 2
                case 1:
                    return 1
                case 2:
                    return 0
                case _:
                    logging.exception("unknown Value returned from player 2 on RPS case 2")
                    raise ValueError
        case _:
            logging.exception("unknown Value returned from player 1")
            raise ValueError