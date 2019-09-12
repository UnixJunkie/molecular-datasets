import urllib2


BASE_URL = 'https://datasets-ressources.s3.us-east-2.amazonaws.com/synthetic-molecular-data/binding/'


if __name__ == '__main__':

    print(' Synthetic Collection Downloader '.center(60, '-'))

    print('This script will download the synthetic molecular dataset. '
          'Please make sure that you have enough storage (86GB).')
    print('You may also download a subset of ten (10) tasks for testing purposes.')

    print()

    print('>> Where should the data be located (root directory)')
