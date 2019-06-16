# DMS-API changelog

## To be release

  - Change return value of Extension#apply [c948eae]

[c948eae]: https://github.com/dmsapi/python/commit/c948eaee4a29484e1db1c4cd7b62de20dc8fb7e5

## Version 0.2.2

  - Add timezone option for cloud runtime environment [81238d0]
  - Remove useless `dmsapi.core.requests` [bd8b93f]
  
[81238d0]: https://github.com/dmsapi/python/commit/81238d045215e4129746cd9689312b9159b4f2b8
[bd8b93f]: https://github.com/dmsapi/python/commit/bd8b93fee8bb5bbf661df2b7cd3bc303d6565bf6

## Version 0.2.1

  - Fix error in Extension#apply [a379f37]
  
[a379f37]: https://github.com/dmsapi/python/commit/a379f3786a96723315c43ae8d85ec7628513fcfb

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