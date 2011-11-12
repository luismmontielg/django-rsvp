from setuptools import setup, find_packages

setup(
    name='django-rsvp',
    version='0.1.1',
    description='A simple django RSVP app.',
    long_description='',
    keywords='django, rsvp',
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='https://github.com/toastdriven/django-rsvp',
    license='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['django',],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)
