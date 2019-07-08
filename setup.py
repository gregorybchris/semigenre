from setuptools import setup, find_packages


setup(
    name='semigenre',
    description='Music recommendation with genre discovery',
    long_description=open('README.md').read(),
    keywords=['music', 'song', 'genre', 'recommend', 'sound', 'tune'],
    version='0.0.1',
    license='Apache',
    author='Chris Gregory',
    author_email='christopher.b.gregory@gmail.com',
    url='chrisgregory.me',
    install_requires=[
        'python-vlc==3.0.6109'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['tests']),
    download_url=''
)
