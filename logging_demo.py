import logging

logging.basicConfig(filename="mylog.log",level=logging.WARNING)
logging.critical("critical")
logging.error("Error")
logging.warning("warning")
logging.info("Information")
logging.debug("Debugging")