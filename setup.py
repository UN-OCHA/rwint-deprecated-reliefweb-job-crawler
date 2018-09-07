import sys

from setuptools import setup

sys.path.append("/usr/local/lib/python3.5/dist-packages/")
if sys.version_info < (3, 5):
    sys.exit('Sorry, you should run this on Python > 3.5 < 3.7')
if sys.version_info > (3, 6):
    sys.exit('Sorry, you should run this on Python > 3.5 < 3.7')

setup(
    name='reliefweb_job_crawler',
    version='0.1',
    packages=['reliefweb_job_crawler'],
    url='https://github.com/reliefweb/reliefweb-job-crawler/',
    license='ReliefWeb',
    author='Miguel Hernandez',
    author_email='hernandez@reliefweb.int',
    description='ReliefWeb Job Crawler',
    long_description=open('README.md').read(),
    keywords='reliefweb humanitarian updates job articles crawler classification tagging multitagging',
    zip_safe=False,
    install_requires=[
        # see requirements.txt
    ],
    python_requires='>3, <3.7',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Developers',
    ],
)
