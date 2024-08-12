# Log Metrics Computation Script

## Description
This project consists of a Python script that reads log entries from the standard input (`stdin`) line by line and computes basic metrics from the logs. The script keeps track of the total file size of all log entries and counts the occurrences of specific HTTP status codes. After processing every 10 lines, the script outputs the current metrics. It also ensures that the metrics are printed when the script is interrupted or finishes processing the input.

## Files

- **log_metrics.py**: The main script that reads from `stdin`, processes the log lines, and computes the metrics.
- **log_generator.py**: A script that generates random log entries to simulate the input for the `log_metrics.py` script. This can be useful for testing the log metrics computation.

## How It Works

1. **Reading Input**: The script reads log entries line by line from `stdin`.
2. **Metrics Calculation**:
   - It extracts the HTTP status code and file size from each log entry.
   - It increments the count for the respective status code.
   - It adds the file size to a running total.
3. **Output**: After every 10 log entries, the script prints:
   - The total file size processed so far.
   - The count of each HTTP status code that has appeared.
4. **Graceful Exit**: If the script is interrupted or finishes processing all input, it will print the final metrics before exiting.

## Example Output

```plaintext
File size: 12345
200: 5
301: 1
400: 2
404: 2

Running the Scripts
log_metrics.py:
This script expects to read from stdin. You can run it directly in a terminal where logs are piped into it:

cat logfile.log | python3 log_metrics.py

log_generator.py:
This script generates log entries and writes them to stdout. You can use it to simulate log input for the log_metrics.py script:

bash
Copy code
python3 log_generator.py | python3 log_metrics.py
Requirements
Python 3.x
The scripts do not require any external libraries and can be run in any environment that supports Python 3.
Use Cases
This project can be used for:

Monitoring and analyzing server logs in real-time.
Testing log processing tools by generating random log data.
Learning about basic log processing and metric computation in Python.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as you wish. See the LICENSE file for more details.

Author
This script was created by [Your Name]. Feel free to reach out if you have any questions or suggestions.

css
Copy code

Each section is properly formatted, and the code blocks are correctly highlighted to ensure readability in Markdown. Replace `[Your Name]` with your actual name for attribution.
