import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='autoitobfuscator',

    version='1.0.4',

    description='AutoIt Obfuscator Web API interface can help you to protect your AutoIt script source code against analysis, reverse engineering and decompilation. AutoIt Obfuscator provides advanced AutoIt source code parsing based on AST trees, multiple advanced obfuscation strategies are available.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    keywords = "autoit au3 obfuscator obfuscation obfuscate decompile decompiler decompilation antidebug antivm antisandbox antiemulator",

    url='https://www.pelock.com',

    author='Bartosz Wójcik',
    author_email='support@pelock.com',

    license='Apache-2.0',

    packages=['autoitobfuscator'],

    zip_safe=False,

    classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Natural Language :: English",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
      ],
)