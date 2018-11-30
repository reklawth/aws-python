from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Thomas Walker',
    author_email='thwalker@vt.edu',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/reklawth/aws-python/tree/master/02-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
