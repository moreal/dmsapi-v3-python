# DMS-API changelog

## Version 0.2.0

- Support Goingout, Info API
- Add cancel method in Extension API
- Drop the automation pypi deploy

## Version 0.1.3

- Automation pypi version by git tag

## Version 0.1.2

- Support direct import
  ```python
  from dmsapi import DMSSession
  ```
- Support to use session without account
  ```python
  from dmsapi import DMSSession
  
  session = DMSSession()
  ```

## Version 0.1.1
- Refactor config structure

## Version 0.1.0
Initial Release with some api

- Support Extension, Meal, Stay API