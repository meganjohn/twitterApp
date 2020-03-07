import twitter

def ask_for_input() -> str:
    pass

def is_valid_input(user_input: str) -> bool:
    is_valid = True
    if user_input == "":
        is_valid = False
    split_input = user_input.split(" ")
    if len(split_input) > 1:
        is_valid = False
    return is_valid



def pick_tweets(all_tweets: list, number: int) -> list:
    pass

def output_tweets(selected_tweets: list) :
    pass


if __name__ == "__main__":
    print ("hi there")