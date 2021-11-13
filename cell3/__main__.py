from multiprocessing.pool import ThreadPool
from time import sleep


def call(bar, baz):
    print('Calling...')
    sleep(2)
    return 'foo' + baz


def get_call_status(bar, baz):
    print('Checking....')
    return 'foo' + baz


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pool = ThreadPool(processes=1)
    result = pool.apply_async(call, ('world', 'foo'))
    get_call_status('world', 'bar')
    return_val = result.get()
    print('return_val: ' + return_val)
