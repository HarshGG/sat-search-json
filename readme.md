# SAT Scores JSON

Description: The `data.json` file in this project contains information on the SAT scores from schools in New York City in 2012. The program performs data analysis on `data.json`.<br>
Language: Python<br>
Project type: School project, collaborative<br>
Purpose: Explore the vast capabilities of Python in handling and organizing data, use it to analyze data from JSON files<br> 

The data came from [Data.gov](https://catalog.data.gov/dataset/sat-results-e88d7).

### Data format

```javascript
{
	"meta": {}, // Not going to worry about any of this
	"data": [
		[
		  "row-7qpx-gwzc~srii",   // Some identifier
		  "00000000-0000-0000-DBB6-F7DC08685EEE",  // Unknown
		  0,  // Appears to always be zero
		  1425758507,  // Timestamp
		  null,		   // Seems to always be null	
		  1425758507,  // Timestamp
		  null,        // Seems to always be null
		  "{ }",       // Don't know?
		  "01M292",    // ID maybe?
		  "HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES",  // School name
		  "29",  // Number of students tested
		  "355", // Reading score
		  "404", // Math score
		  "363"  // Writing score
		], 
		// more records...
	]
}
```



### Most Tests

The `most_tests` method returns a tuple containing info on the school that gave the most SAT exams in 2012. First element should be the school name. Second element should be the number of exams given.

### Best Score

`best_score` returns a tuple containing school information on the school with the highest total SAT score (all 3 scores). First element should be the school name followed by the total score of all 3 tests.

### Best Score: Small Schools

The `best_score_small` is the same as `best_score`, but should only consider schools with no more than 50 total test takers.

### X Most Tests

`x_most_tests` returns an array of tuples containing the schools with the `x` most tests given in descending order. For example, if `x` is 10 then the method should return a 10 element list with the school giving the most tests in element 0, the school giving the 10th most tests in element 9, and the other going from 2nd to 9th in elements 1 through 8.

### X Highest Score

Same as `x_most_tests`, but this time return a list of the top `x` schools by total test score. 
