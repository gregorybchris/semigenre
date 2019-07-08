from setuptools import setup, find_packages


setup(
    name='semigenre',
    description='Music recommendation with genre discovery',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['music', 'song', 'genre', 'recommend', 'sound', 'tune'],
    version='0.0.2',
    license='Apache',
    author='Chris Gregory',
    author_email='christopher.b.gregory@gmail.com',
    url='https://github.com/gregorybchris/semigenre',
    install_requires=[
        'python-vlc==3.0.6109'
    ],
    tests_require=[
        'pytest>=5.0.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['tests'])
)
