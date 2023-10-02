cd ../..
rm -r tests/RobotsTools
cp src/RobotsTools tests/RobotsTools -r
echo "copied RobotsTools to tests/RobotsTools"
python3 tests/RobotsTools/__init__.py
#echo "ran python programs without problem"
python3 tests/testMain.py
