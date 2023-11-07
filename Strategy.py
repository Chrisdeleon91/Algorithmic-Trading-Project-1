{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8fe166b1-2d3e-45bb-9587-2672123ba4b6",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import backtrader \n",
    "\n",
    "\n",
    "# Create a Stratey\n",
    "class TestStrategy(backtrader.Strategy):\n",
    "\n",
    "    def log(self, txt, dt=None):\n",
    "        ''' Logging function fot this strategy'''\n",
    "        dt = dt or self.datas[0].datetime.date(0)\n",
    "        print('%s, %s' % (dt.isoformat(), txt))\n",
    "\n",
    "    def __init__(self):\n",
    "        # Keep a reference to the \"close\" line in the data[0] dataseries\n",
    "        self.dataclose = self.datas[0].close\n",
    "\n",
    "    def next(self):\n",
    "        # Simply log the closing price of the series from the reference\n",
    "        self.log('Close, %.2f' % self.dataclose[0])\n",
    "\n",
    "        if self.dataclose[0] < self.dataclose[-1]:\n",
    "            # current close less than previous close\n",
    "\n",
    "            if self.dataclose[-1] < self.dataclose[-2]:\n",
    "                # previous close less than the previous close\n",
    "\n",
    "                # BUY, BUY, BUY!!! (with all possible default parameters)\n",
    "                self.log('BUY CREATE, %.2f' % self.dataclose[0])\n",
    "                self.buy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a2eb647-c532-468c-81e8-7eb1802ae0a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
