import logging


def main() -> None:
    logging.basicConfig(
        filename="demo1.log", filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    #logging.disable()
    logging.debug("this is debug message.")
    logging.info("this is info message.")
    logging.warning("this warning message.")
    logging.error("this error message.")
    logging.critical("this is critical message.")


if __name__ == '__main__':
    main()
