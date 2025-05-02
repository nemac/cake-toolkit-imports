# cake-toolkit-imports

## Step by Step
- Download as CSV [CRT + Cake Case Study Transfer](https://docs.google.com/spreadsheets/d/1gCpeyQdPyz8r_Ku6E9gSI355noieKkJQytFXvOzJ3Gs/edit?pli=1&gid=93249297#gid=93249297) as `cake_selected_case_studies.csv`
- Using Content Export Module [Example on CAKE Dev](https://dev-cakex.pantheonsite.io/admin/content/content-export) export all Case Studies as `example_cake_export.csv` but be sure to leave `field_proj_website` and `field_spotlight_link` unchecked due to [this bug](https://www.drupal.org/project/content_export_csv/issues/3454061)
- Delete first row "CAKE's WORKING SPREADSHEET IS HERE! USE THIS SPREADSHEET TO UPDATE & SHARE WITH NEMAC" from `cake_selected_case_studies.csv` or confirm that the first row is the header row
- Run python script to leave only case studies that should be imported to toolkit `python3 filter.py cake_selected_case_studies.csv example_cake_export.csv cake_case_studies_to_import.csv`
- Run python script to translate CAKE taxonomy ids to toolkit taxonomy ids `python3 translate_taxonomies.py cake_case_studies_to_import.csv cake_case_studies_to_import_taxonomies_translated.csv`


# TODOS
- Create a feed on dev toolkit site and map all of the fields correctly using `cake_case_studies_to_import.csv`
- Do a test import on dev toolkit site
- [Export feed config from dev site](https://toolkit.nemac.org/admin/config/development/configuration/full/export)
- Import exported config
- Import case studies on prod
