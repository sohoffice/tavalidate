Publish
=======

1. Compile
   
   ```
   python setup.py sdist
   ```
   
2. Check built artifact
   
   ```
   twine check dist/*
   ```
   
3. Install to test pypi
   
   ```
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```
   
4. Test with test pypi

   ```
   pip install --index-url https://test.pypi.org/simple/ tavalidate==0.0.5
   ```
   
5. Deploy to prod pypi
   
   ```
   twine upload dist/*
   ```
