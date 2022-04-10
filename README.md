# scurri-postcode-lib

#### Repo for second Scurri programming exercise, includes implementation and tests for a python library for the validation and formatting of UK postcodes




This library provides two functions, validate_postcode(str) and format_postcode(str).



---

## Usage


### `scurri_postcode.validate_postcode(postcode: str)`

This function accepts a postcode string as input and returns a boolean value True if its characters correspond to a valid UK postcode (regardless of whitespace, hyphens, and capitalisation), and False if they do not. 

The function removes all whitespace and hyphens, before validating the resulting string against a regular expression (retrieved from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting on 2022-04-10) constructed to validate both standard and special cases (Overseas Territories, PO boxes, etc.) of postcodes. It returns the result of this comparison as a boolean value.


Examples:

```
from scurripostcode import scurri_postcode

> scurri_postcode.validate_postcode('eC1a1  b  B  ')
True
> scurri_postcode.validate_postcode('geC  X')
True
> scurri_postcode.validate_postcode('333 8TH')
False
```

____


### `scurri_postcode.format_postcode(postcode: str)`

This function accepts a postcode string as input and returns the correctly-formatted version of that postcode as a string. 

The function first verifies that the input is a valid postcode by calling validate_postcode(). \
If the input is not a valid postcode, the exception InvalidPostcode is raised.\
If it is valid, the function removes all whitespace and hyphens before performing a series of logical checks to determine in which category of UK postcodes the given code belongs. It then splits and formats the code with the appropriate spacing, punctuation, and capitalisation, and returns the result as a string.

Examples:

```
from scurripostcode import scurri_postcode

> scurri_postcode.format_postcode('eC1a1  b  B  ')
EC1A 1BB
> scurri_postcode.format_postcode('geC  X')
GE CX
> scurri_postcode.format_postcode('vg1140')
VG-1140
```



