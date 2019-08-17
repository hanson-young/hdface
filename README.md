### hdface

https://github.com/hanson-young/hdface  
pytorch >= 0.4.1  
python == 3.6

python3 -m pip install --user --upgrade setuptools wheel  

python3 setup.py sdist bdist_wheel  
pip install hdface-0.1.3-py3-none-any.whl  

twine upload dist/*  
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*  


pip install hdface==0.1.3  
pip uninstall hdface  