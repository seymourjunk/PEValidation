### ABOUT
pet-project for learning (and having fun) a PE format

### TO DO
- [ ] add structures with const for translate some hex-values
    - [ ] Machine (IMAGE_FILE_HEADER)
    - [ ] Time Date Stamp (IMAGE_FILE_HEADER)
    - [ ] Characteristics (IMAGE_FILE_HEADER)
    - [ ] OS Ver. (IMAGE_OPTIONAL_HEADER)
    - [ ] Subsystem (IMAGE_OPTIONAL_HEADER)
    - [ ] DLL Characteristics (IMAGE_OPTIONAL_HEADER)
- [ ] indicate of a packed program
    - [ ] warning if program has few imports, and particularly if the only imports are `LoadLibrary` and `GetProcAddress`
    - [ ] the program has abnormal section sizes, such as a `.text` section with a `Size of Raw Data` of 0 and `Virtual Size` of nonzero
    - [ ] entropy calculation
- [ ] imports