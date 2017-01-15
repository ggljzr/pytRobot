from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='pytrobot',
    version='0.1.0',
    description='Application for controlling Raspberry Pi based robot',
    long_description=long_description,
    author='Ondřej Červenka',
    author_email='cerveon3@fit.cvut.cz',
    keywords='Raspberry Pi, cli, web',
    license='MIT',
    url='https://github.com/ggljzr/pytRobot',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3.5',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP',
        'Environment :: Console',
        'Environment :: Web Environment'
    ],
    entry_points={
        'console_scripts': ['pytrobot = pytrobot.pytrobot:main', ],
    },
    install_requires=['Flask>0.10.0', 
                     'click>=6.6', 
                     'Jinja2>=2.8',
                     'MarkupSafe>=0.23', 
                     'requests>=2.11.1',
                     'Werkzeug>=0.11.11',
                     ],
    setup_requires=[
        'pytest-runner',
        ],
    tests_require=[
        'pytest',
        ],
    )
