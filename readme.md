# CRUD Python Dash App

## Features

### Current:
- Develop multi-file app for clean navigation and development
- Create data uploader
- Allow user deletion of files
- Build callbacks to allow for dropdown and file list to be updated
- Have conditional filter for dropdowns
- Visualize data from dropdown selection

### Future:
- Be able to modify csv
- Be able to validate before data is uploaded:
    - File type
    - File columns and rows 
- Allow users to run a fit and predict method for data
- tie in uploaded data into data visualization


```
.
├── app.py: Dash app instantiates here
├── callbacks.py: Callbacks to interact server and ui
├── download: Folder where downloaded items land
├── index.py: This is main file to run app
├── layouts.py: Application layout and tabs
├── make_data.ipynb: Generate fake data
├── readme.md: This file
├── req.yaml: Requirements File
├── styles.py: Styles for CSS
├── tools.py: Helper functions
└── uploaded: Folder where files are loaded to

```