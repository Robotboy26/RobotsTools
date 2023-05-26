rm -r tests/RobotsTools
rm -r tests/__pycache__
rm -r tests/RobotsTools/__pycache__
cp src/RobotsTools tests/RobotsTools -r
echo "copied RobotsTools to tests/RobotsTools"
python3 tests/RobotsTools/__init__.py
python3 tests/RobotsTools/PL/__init__.py
#echo "ran python programs without problem"
python3 tests/testMain.py