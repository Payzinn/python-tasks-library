import logging

root = logging.getLogger()

sub_1 = logging.getLogger('sub_1')
sub_1.setLevel(logging.DEBUG)

sub_2 = logging.getLogger('sub_2')
sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')

formatter = logging.Formatter('%(name)s | %(levelname)s | %(message)s | %(module)s')

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

sub_1.addHandler(handler)

root_handler = logging.StreamHandler()
root_handler.setFormatter(formatter)
root_handler.setLevel(logging.DEBUG)

root.debug('debug root')
sub_1.debug('debug sub_1')
sub_1.info('info sub_1')
sub_2.debug('debug sub_2')
sub_sub_1.debug('sub_sub_1 debug')

sub_2.propagate = False
sub_1.propagate = True

root.debug('root propagate')
sub_1.debug('sub_1 propagate')
sub_2.debug('sub_2 propagate')
sub_sub_1.debug('sub_sub_1 propagate')