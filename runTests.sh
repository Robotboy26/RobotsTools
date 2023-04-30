rm -r tests/RobotsTools
cp src/RobotsTools tests/RobotsTools -r
echo "copied RobotsTools to tests/RobotsTools"
python3 -m unittest tests/testMain.py