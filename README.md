# cs279-when2meet

A when2meet-like scheduler app built with React. The code was adapted from an existing React module called [Schedule Selector](https://github.com/bibekg/react-schedule-selector) (demo [here](http://react-schedule-selector.surge.sh/)). To run it locally, first clone the repo and navigate to the root directory: 
```
git clone https://github.com/ZiweiGu/cs279-when2meet.git
cd cs279-when2meet
```
Then, run the following and follow instructions in the terminal:
```
npm start
```

Key feautures of When2meet vs Doodle:
- How to select times: in When2meet, users toggle availability by clicking or dragging time cells; in Doodle, users indicate availability by selecting one of 3 checkboxes for each time slot listed.
- How results are shown: When2meet shows results in a heatmap, while Doodle shows them in a table.
- Synchronization: users' input is instantly saved and displayed in When2meet; by contrast, users need to click a submit button to have their results saved and displayed in Doodle.
- Support for unsure responses : Doodle allows a "maybe" option for availability but When2meet does not.