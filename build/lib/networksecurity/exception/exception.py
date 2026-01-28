import sys
from networksecurity.logging_utils.logger import logger



class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception):
        super().__init__(str(error_message))

        exc_type, exc_obj, exc_tb = sys.exc_info()

        self.error_message = error_message
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"at line number [{self.lineno}] "
            f"with error message [{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        logger.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed")
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
        raise NetworkSecurityException(e) from e
    
    
