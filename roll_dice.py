import random
import dice_logger

# Set up the logger
logger = dice_logger.get_logger(__name__)

def dice():
    return random.randint(1, 6)

def roll_dice():
    attempts = 0
    dice_result = []

    logger.info("Starting to roll the dice.")
    
    #Attempt rolling dice into 3 attempts only
    while attempts < 3:
        dice1 = dice()
        dice2 = dice()
        
        logger.debug(f"Rolled dice1: {dice1}, dice2: {dice2}")
        
        dice_result.append([dice1, dice2])

        #If both dice number result other than 1 or 6, it will return the return immediately
        # If either dice number result is not 1 or 6, return immediately
        # If both dice number result are neither 1 nor 6, return immediately
        if (dice1 not in (1, 6)) and (dice2 not in (1, 6)):
            logger.info(f"Rolled neither 1 nor 6: {(dice1, dice2)}")
            return [(dice1, dice2)]
        
        #If both dice result to 6, then it will rerolling again
        elif dice1 == 6 and dice2 == 6:
            logger.info(f"Both dice are 6,  attempt: {attempts + 1}")
            attempts += 1
            continue

        #If both dice result to 1, then it will rerolling again
        elif dice1 == 1 and dice2 == 1:
            logger.info(f"Both dice are 1, attempt: {attempts + 1}")
            attempts += 1
            continue
        
        return [(dice1, dice2)]
    attempts += 1
    logger.info("Exceeded maximum attempts.")
    return []

if __name__ == '__main__':
    roll_dice()
