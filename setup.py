from setuptools import setup
import sys, os

version = '1.0'

setup(name='WebOb',
      version=version,
      description="WSGI request and response object",
      long_description="""\
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

You may install the `in-development version of WebOb
<http://bitbucket.org/ianb/webob/get/tip.gz#egg=WebOb-dev>`_ with
``pip install WebOb==dev`` (or ``easy_install WebOb==dev``).
""",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      keywords='wsgi request web http',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://pythonpaste.org/webob/',
      license='MIT',
      packages=['webob', 'webob.util'],
      zip_safe=True,
      test_suite='nose.collector',
      #test_runner = 'unittest:TextTestRunner',
      tests_require=['Tempita', 'WSGIProxy', 'WebTest', 'dtopt', 'nose',
                     'repoze.profile'],
      )
