rm -r tests/RobotsTools
rm -r tests/__pycache__
rm -r tests/RobotsTools/__pycache__
cp src/RobotsTools tests/RobotsTools -r
echo "copied RobotsTools to tests/RobotsTools"
python3 -m unittest tests/testMain.py