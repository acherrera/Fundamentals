# Setting up Sphinx


1. Make directory ./docs/ *mkdir docs/*
2. Go into directory *cd docs/*
3. Run *sphinx-quickstart*
4. Pay attention to the first couple questions. Specifically:
    Create seperate soure and build - yes
    Name prefix - enter
    Project Name
    Author name

5. Hit enter (use default) until it sets up the file system
6. edit ./source/conf.py
    Uncomment sys.path.insert(0, os.path/abspath('.'))
    Update the path to look for files:
    Change '.' to '../../' 
    Add extentions as preferred. I usually add 'sphinx.ext.autodoc' and
    'sphinx.ext.napoleon' for bringing in rst documentation from the code and
    adding support for Google Style documentation
7. Run *make html*

