from distutils.core import setup
setup(
  name = 'ismrpy',         # How you named your package folder (MyLib)
  packages = ['ismrpy'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='gpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Reads ismr files and provides pandas data frame',   # Give a short description about your library
  author = 'Dinil Bose P',                   # Type in your name
  author_email = 'dinilbose@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/dinilbose/ismrpy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['ismr', 'pandas'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Researchers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0 License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
