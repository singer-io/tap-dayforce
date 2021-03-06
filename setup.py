from setuptools import find_packages, setup

setup(
    name='tap_dayforce',
    author='David Wallace',
    author_email='david.wallace@goodeggs.com',
    version='0.2.0',
    url='https://github.com/singer-io/tap-dayforce',
    description='Singer.io tap for extracting data from Dayforce REST API v1',
    long_description='',
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords="singer tap python dayforce",
    license='GPLv3',
    packages=find_packages(exclude=['tests']),
    package_data={
        'tap_dayforce': ['schemas/*.json']
    },
    install_requires=[
        'dayforce-client==0.1.0',
        'singer-python==5.9.0',
        'backoff==1.8.0',
        'rollbar==0.14.7'
    ],
    extras_require={
        'dev': [
            'pylint',
            'ipdb',
            'nose',
            'pytest'
        ]
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['tap-dayforce = tap_dayforce:main']
    }
)
