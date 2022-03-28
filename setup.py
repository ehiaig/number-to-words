import setuptools 

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setuptools.setup( 
    name='numbers-to-words', 
    version='1.0', 
    author='Ehi Aigiomawu', 
    author_email='ehiagheaigg@gmail.com', 
    description='Convert number to words', 
    packages=setuptools.find_packages(),
    install_requires = [requirements],
    entry_points={ 
        'console_scripts': [ 
            'numbers-to-words = numbers_to_words.numbers_to_words:main' 
        ] 
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)