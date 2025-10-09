
# Jet Anderson
Resume as code

## [Published with JSON Resume CLI](https://jsonresume.org/)
View in the following formats:
 - [JSON](https://github.com/thatsjet/resume/blob/master/resume.json)
 - [PDF](https://github.com/thatsjet/resume/blob/master/Jet-Anderson.pdf)

## Contact

Email: [janderson@miletwo.net](mailto:janderson@miletwo.net)  

Location: Portland, Oregon, USA

## Profiles

[Twitter - @thatsjet](http://twitter.com/thatsjet)  
[LinkedIn - /thatsjet](https://linkedin.com/in/thatsjet)  
[GitHub - /thatsjet](https://github.com/thatsjet)  

## How To Use
*Because I keep forgetting how to between updates*

- `$ npm install resumed`
    - [(based on original `resume-cli` , more actively maintained)]((https://github.com/rbardini/resumed))
- `$ npm install jsonresume-theme-stackoverflow`
    - https://registry.jsonresume.org/thomasdavis?theme=stackoverflow
- `$ resumed`
    - will render as html - just print from preview to save PDF. Could never get PDF export feature to work correctly.
- add override.css file to html output
    - `<link rel="stylesheet" href="override.css">`


***Notes:***

Schema is WRONG! Or... themes don't match schema. Whatever.

- instead of "name" in work item for company use "company"
- instead of "website" as listed in theme github use "url" as indicated in schema