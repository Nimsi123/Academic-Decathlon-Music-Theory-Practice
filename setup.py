from setuptools import setup

setup(name='Music Theory Tutor for Academic Decathlon',
      version='1.0',
      description='A way to practice music theory for free, forever!',
      url='http://github.com',
      author='Nima Rahmanian',
      author_email='nimarahmanian8@gmail.com',
      packages=["Algorithms_Verification", "Displays",  "Drivers",
                "Extra", "Tabs"],
      zip_safe=False,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"]
        # And include any *.msg files found in the "hello" package, too:
        #"hello": ["*.msg"],
      }
      
      )
