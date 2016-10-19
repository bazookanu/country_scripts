Usage:

'countries.list' should contain the list of all countries in a region (it's Asia here)
I got them from Wikipedia. To clean the Wiki list of countries, country_scripts has a function clean_up_list. It's not perfect- the countries that have spaces in their name will end up with only their first word in the list. These will be ignored by generate_go, and will be missing in its output.

start python in interactive mode

import country_scripts

dt = country.scripts.Dirty()

dt.generate_go('countries.list', 'country.codes')

<will print the country codes>

To clean up countries.list:

dt.clean_up_list('countries.list')

