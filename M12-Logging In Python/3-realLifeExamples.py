import logging

## create configure setting 
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s / %(name)s / %(levelname)s / %(message)s",
                    datefmt='%Y-%m-%d / %H-%M-%S',
                    handlers=[
                        logging.FileHandler("ArithmaticApp.log"),
                        logging.StreamHandler()
                    ]
)

## create logger for ArithmatioOPeration module
logger = logging.getLogger("ArithmaticOpr")

def add(a,b):
    result = a+b
    logger.debug(f"Adding  {a}+{b} = {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"subtracting  {a}-{b} = {result}")
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"multiplying  {a}*{b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"dividing  {a}/{b} = {result}")
        return result
    except ZeroDivisionError as zde:
        logger.error("divide by Zero Error")
        return None
    

## calling functtions
add(2,5)
subtract(7,5)
multiply(4,5)
divide(9, 0)

