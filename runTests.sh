rm tests/main.py
cp src/RobotsTools/main.py tests/main.py
echo "copied main.py"
python3 -m unittest tests/testMain.py