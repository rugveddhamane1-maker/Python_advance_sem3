import logging

# Configure logging
logging.basicConfig(
    filename="experiment14.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Display and record program execution
print("Program Started")

logging.debug("This is a debug message")
logging.info("Program execution started")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# Exception handling
try:
    a = 10
    b = 0

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    logging.exception("Exception occurred during division")

print("Program Completed")

logging.info("Program execution completed")