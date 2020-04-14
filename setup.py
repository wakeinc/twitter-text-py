from setuptools import setup, find_packages
 
setup(
    name='twitter-text-py',
    version='3.0.0',
    description='Python 3 compatible library for auto-converting URLs, mentions, hashtags, lists, etc. in Twitter text. Also does tweet validation and search term highlighting.',
    author='Michael Perret',
    author_email='michael.t.perret@gmail.com',
    url='http://github.com/wakeinc/twitter-text-py',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    install_requires=['setuptools'],
    license = "BSD"
)
