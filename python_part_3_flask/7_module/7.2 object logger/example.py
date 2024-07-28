import logging

root_logger = logging.getLogger()
root_logger.setLevel('DEBUG')
module_logger = logging.getLogger('module_logger')
submodile_logger = logging.getLogger('module_logger.submodule_logger')

def main():
    print(root_logger)
    print(submodile_logger)
    print(submodile_logger.parent)


if __name__ == '__main__':
    main()