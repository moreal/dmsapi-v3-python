# Python DMS-API

[![Build Status](https://travis-ci.com/dmsapi/python.svg?branch=master)](https://travis-ci.com/dmsapi/python)
[![codecov](https://codecov.io/gh/dmsapi/python/branch/master/graph/badge.svg)](https://codecov.io/gh/dmsapi/python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6e22fb098a854e49b70d5c04516eda79)](https://www.codacy.com/app/dogeonlove0326/python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dmsapi/python&amp;utm_campaign=Badge_Grade)

DSM-DMS api server wrapping library

## Example

```python
# Make user stay :)
from dmsapi import DMSSession
from dmsapi.api.stay import StayType

session = DMSSession('<user-id>', '<user-password>')
session.stay.apply(StayType.STAY)
```

## License

MIT

## Contribution

Welcome!!