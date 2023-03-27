import logging

logging.basicConfig(filename='demo.log', level=logging.DEBUG)


# logging.disable()


def name_check(name):
    try:
        if len(name) < 2:
            # print("checking name fo len")
            logging.debug("checking name for len")
            return "invalid name"
        elif name.isspace():
            # print("checking if name space")
            logging.debug("checking if name is space")
            return "invalid name"
        elif name.isalpha():
            # print("checking name is alphabet")
            logging.debug("checking name is alphabet")
            return 'name is valid'
    except ValueError as v:
        logging.exception(v)

print(name_check('g'))
