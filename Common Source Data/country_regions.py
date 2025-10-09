from country_codes import countries

regions = {
    "Andean Latin America": [
        "Bolivia", "Ecuador", "Peru"
    ],
    "Australasia": [
        "Australia", "New Zealand", "American Samoa", "Cook Islands", "Tokelau"
    ],
    "Caribbean": [
        "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Cuba", "Dominica",
        "Dominican Republic", "Grenada", "Guyana", "Haiti", "Jamaica", 
        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
        "Suriname", "Trinidad and Tobago", "Aruba", "Curaçao", "Saint Martin (French part)", 
        "Sint Maarten (Dutch part)", "Turks and Caicos Islands", "Virgin Islands, British", 
        "Virgin Islands, U.S.",'Martinique','Guadeloupe'
    ],
    "Central Asia": [
        "Armenia", "Azerbaijan", "Georgia", "Kazakhstan", "Kyrgyzstan", "Mongolia", 
        "Tajikistan", "Turkmenistan", "Uzbekistan"
    ],
    "Central Europe": [
        "Albania", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czechia", 
        "Hungary", "Kosovo", "Montenegro", "North Macedonia", "Poland", "Romania", 
        "Serbia", "Serbia and Montenegro", "Slovakia", "Slovenia"
    ],
    "Central Latin America": [
        "Colombia", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Mexico", 
        "Nicaragua", "Panama", "Venezuela"
    ],
    "Central Sub-Saharan Africa": [
        "Angola", "Central African Republic", "Congo", "Democratic Republic of the Congo", 
        "Equatorial Guinea", "Gabon"
    ],
    "East Asia": [
        "China", "Democratic People's Republic of Korea", "Taiwan", "Hong Kong", "Macao"
    ],
    "Eastern Europe": [
        "Belarus", "Estonia", "Latvia", "Lithuania", "Republic of Moldova", 
        "Russian Federation", "Ukraine"
    ],
    "Eastern Sub-Saharan Africa": [
        "Burundi", "Comoros", "Djibouti", "Eritrea", "Ethiopia", "Kenya", "Madagascar", 
        "Malawi", "Mozambique", "Rwanda", "Somalia", "South Sudan", "Uganda", 
        "United Republic of Tanzania", "Zambia", "Réunion", "Mayotte"
    ],
    "High-income Asia Pacific": [
        "Brunei Darussalam", "Japan", "Republic of Korea", "Singapore", "Guam", 
        "Northern Mariana Islands"
    ],
    "High-income North America": [
        "Canada", "United States of America", "Bermuda", "Puerto Rico", "Greenland", 
        "Cayman Islands"
    ],
    "North Africa and Middle East": [
        "Afghanistan", "Algeria", "Bahrain", "Egypt", "Iran", "Iraq", "Jordan", 
        "Kuwait", "Lebanon", "Libya", "Morocco", "Oman", "Palestine", "Qatar", 
        "Saudi Arabia", "Sudan", "Syrian Arab Republic", "Tunisia", "Türkiye", 
        "United Arab Emirates", "Yemen", "Israel"
    ],
    "Oceania": [
        "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "Niue", 
        "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", 
        "Tuvalu", "Vanuatu", "New Caledonia", "French Polynesia", "Wallis and Futuna"
    ],
    "Southern Latin America": [
            "Argentina", "Chile", "Uruguay","Falkland Islands","South Georgia and the South Sandwich Islands"
    ],
    "Southern Sub-Saharan Africa": [
        "Botswana", "Eswatini", "Lesotho", "Namibia", "South Africa", "Zimbabwe"
    ],
    "Tropical Latin America": [
        "Brazil", "Paraguay",'French Guiana'
    ],
    "Western Europe": [
        "Andorra", "Austria", "Belgium", "Cyprus", "Denmark", "Finland", "France", 
        "Germany", "Greece", "Guernsey", "Iceland", "Ireland", "Isle of Man",
        "Italy", "Jersey", "Liechtenstein", "Luxembourg", "Malta", "Monaco", 
        "Netherlands", "Norway", "Portugal", "San Marino", "Spain", "Sweden", 
        "Switzerland", "United Kingdom", "Gibraltar", "Faroe Islands"
    ],
    "Southeast Asia":[
    'Cambodia','Indonesia',"Lao People's Democratic Republic",'Malaysia','Maldives',
    'Mauritius','Myanmar','Philippines','Seychelles','Sri Lanka','Thailand','Timor-Leste',
    'Viet Nam'
    ],
    "South Asia":[
    'Bangladesh','Bhutan','India','Nepal','Pakistan'
    ],
    "Western Sub-Saharan Africa": [
        "Benin", "Burkina Faso", "Cabo Verde", "Cameroon", "Chad", "Côte d'Ivoire", 
        "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Liberia", "Mali", "Mauritania", 
        "Niger", "Nigeria", "Sao Tome and Principe", "Senegal", "Sierra Leone", "Togo","Saint Helena, Ascension, Tristan da Cunha"
    ]
}

region_iso3 = {}
for region, country_list in regions.items():
    iso3_list = []
    for country in country_list:
        if country in countries:
            iso3_list.append(countries[country])
        else:
            print(f"Warning: '{country}' not found in countries dict")
    region_iso3[region] = iso3_list
    
iso3_region={iso: region for region, iso_list in region_iso3.items() for iso in iso_list}