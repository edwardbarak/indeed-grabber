# Indeed Grabber
Take a new line delimited text file of URL's from Indeed job postings and convert them into a numbered list of the following format:

#. `Job title` @ `Company`: `URL`

## Usage
`python3 main.py [file with URLs]`
*Note: Make sure that it is 1 URL per line*

## Behavior
1. Script will loop through provided URLs
2. Script will generate a HTML file with formatted links
3. Script will open HTML file in browser
