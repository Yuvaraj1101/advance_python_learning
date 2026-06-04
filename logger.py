# Built-in Module

import logging


# Configure Logging

logging.basicConfig(

    filename="logs/employee.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)