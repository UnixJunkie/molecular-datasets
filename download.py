from urllib.request import urlopen
import os


BASE_URL = 'https://datasets-ressources.s3.us-east-2.amazonaws.com/synthetic-molecular-data/binding/descriptors/'
TASKS_URL = 'https://raw.githubusercontent.com/invivoai/molecular-datasets/master/synthetic/tasks.csv'


if __name__ == '__main__':

    print('-' * 60)
    print(' Synthetic Collection Downloader '.center(60, '-'))
    print('-' * 60)

    print()

    print('This script will download the synthetic molecular dataset. '
          'Please make sure that you have enough storage (86GB).')
    print('You may also download a subset of ten (10) tasks for testing purposes.')

    print()

    print('>> Where should the data be located ? [./data/]')
    root = input('   ') or './data/'

    print('>> You can choose to download a limited amount of tasks (10) for testing purposes. Perform test dowload ? yes/[no]')
    test = input('   ').lower() in ['y', 'yes']

    tasks = urlopen(TASKS_URL).read().split('\n')

    if test:
        tasks = tasks[:10]

    os.makedirs(root)

    for task in tasks:
        path = os.path.join(root, f'{task}.csv')
        t = urllib2.urlopen(f'{BASE_URL}/{task}.csv').read()
        with open(f'{path}','w') as output:
          output.write(t)
