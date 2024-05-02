# Definición de las variables del m3u
tvg_name = ""
tvg_logo = ""
group_title = ""

# Creación del diccionario con las claves modificadas
dict_m3u = {
    "tvg-name": tvg_name,
    "tvg-logo": tvg_logo,
    "group-title": group_title
}

ignore_similar_topics = ['adultswim', 'adult swim']
topics_nsfw = ['ADULTS', 'ADULTO', 'xxx', 'sextreme' 'SEX XTREME', 'sexmex', 'porn', 'adult', 'playboy', 'venus', 'ONLYFANS', 'MOFOS', 'VISITX', 'BABES', 'BRAZZERS']

equivalence_country_dict = {
    'Afganistán': 'Afghanistan',
    'Albania': 'Albania',
    'Alemania': 'Germany',
    'Andorra': 'Andorra',
    'Angola': 'Angola',
    'Antigua_y_Barbuda': 'Antigua_and_Barbuda',
    'Arabia_Saudita': 'Saudi_Arabia',
    'Argelia': 'Algeria',
    'Argentina': 'Argentina',
    'Armenia': 'Armenia',
    'Australia': 'Australia',
    'Austria': 'Austria',
    'Azerbaiyán': 'Azerbaijan',
    'Bahamas': 'Bahamas',
    'Bangladés': 'Bangladesh',
    'Barbados': 'Barbados',
    'Baréin': 'Bahrain',
    'Bélgica': 'Belgium',
    'Belice': 'Belize',
    'Benín': 'Benin',
    'Bielorrusia': 'Belarus',
    'Birmania': 'Myanmar',
    'Bolivia': 'Bolivia',
    'Bosnia_y_Herzegovina': 'Bosnia_and_Herzegovina',
    'Botsuana': 'Botswana',
    'Brasil': 'Brazil',
    'Brunéi': 'Brunei',
    'Bulgaria': 'Bulgaria',
    'Burkina_Faso': 'Burkina_Faso',
    'Burundi': 'Burundi',
    'Bután': 'Bhutan',
    'Cabo_Verde': 'Cabo_Verde',
    'Camboya': 'Cambodia',
    'Camerún': 'Cameroon',
    'Canadá': 'Canada',
    'Catar': 'Qatar',
    'Chad': 'Chad',
    'Chile': 'Chile',
    'China': 'China',
    'Chipre': 'Cyprus',
    'Ciudad_del_Vaticano': 'Vatican_City',
    'Colombia': 'Colombia',
    'Comoras': 'Comoros',
    'Corea_del_Norte': 'North_Korea',
    'Corea_del_Sur': 'South_Korea',
    'Costa_de_Marfil': 'Ivory_Coast',
    'Costa_Rica': 'Costa_Rica',
    'Croacia': 'Croatia',
    'Cuba': 'Cuba',
    'Dinamarca': 'Denmark',
    'Dominica': 'Dominica',
    'Ecuador': 'Ecuador',
    'Egipto': 'Egypt',
    'El_Salvador': 'El_Salvador',
    'Emiratos_Árabes_Unidos': 'United_Arab_Emirates',
    'Eritrea': 'Eritrea',
    'Eslovaquia': 'Slovakia',
    'Eslovenia': 'Slovenia',
    'España': 'Spain',
    'Estados_Unidos': 'United_States',
    'Estonia': 'Estonia',
    'Eswatini': 'Eswatini',
    'Etiopía': 'Ethiopia',
    'Filipinas': 'Philippines',
    'Finlandia': 'Finland',
    'Fiyi': 'Fiji',
    'Francia': 'France',
    'Gabón': 'Gabon',
    'Gambia': 'Gambia',
    'Georgia': 'Georgia',
    'Ghana': 'Ghana',
    'Granada': 'Grenada',
    'Grecia': 'Greece',
    'Guatemala': 'Guatemala',
    'Guyana': 'Guyana',
    'Guinea': 'Guinea',
    'Guinea_Ecuatorial': 'Equatorial_Guinea',
    'Guinea_Bisáu': 'Guinea_Bissau',
    'Haití': 'Haiti',
    'Honduras': 'Honduras',
    'Hungría': 'Hungary',
    'India': 'India',
    'Indonesia': 'Indonesia',
    'Irak': 'Iraq',
    'Irán': 'Iran',
    'Irlanda': 'Ireland',
    'Islandia': 'Iceland',
    'Islas_Marshall': 'Marshall_Islands',
    'Islas_Salomón': 'Solomon_Islands',
    'Israel': 'Israel',
    'Italia': 'Italy',
    'Jamaica': 'Jamaica',
    'Japón': 'Japan',
    'Jordania': 'Jordan',
    'Kazajistán': 'Kazakhstan',
    'Kenia': 'Kenya',
    'Kirguistán': 'Kyrgyzstan',
    'Kiribati': 'Kiribati',
    'Kuwait': 'Kuwait',
    'Laos': 'Laos',
    'Lesoto': 'Lesotho',
    'Letonia': 'Latvia',
    'Líbano': 'Lebanon',
    'Liberia': 'Liberia',
    'Libia': 'Libya',
    'Liechtenstein': 'Liechtenstein',
    'Lituania': 'Lithuania',
    'Luxemburgo': 'Luxembourg',
    'Madagascar': 'Madagascar',
    'Malasia': 'Malaysia',
    'Malaui': 'Malawi',
    'Maldivas': 'Maldives',
    'Malí': 'Mali',
    'Malta': 'Malta',
    'Marruecos': 'Morocco',
    'Mauricio': 'Mauritius',
    'Mauritania': 'Mauritania',
    'México': 'Mexico',
    'Micronesia': 'Micronesia',
    'Moldavia': 'Moldova',
    'Mónaco': 'Monaco',
    'Mongolia': 'Mongolia',
    'Montenegro': 'Montenegro',
    'Mozambique': 'Mozambique',
    'Namibia': 'Namibia',
    'Nauru': 'Nauru',
    'Nepal': 'Nepal',
    'Nicaragua': 'Nicaragua',
    'Níger': 'Niger',
    'Nigeria': 'Nigeria',
    'Noruega': 'Norway',
    'Nueva_Zelanda': 'New_Zealand',
    'Omán': 'Oman',
    'Países_Bajos': 'Netherlands',
    'Pakistán': 'Pakistan',
    'Palaos': 'Palau',
    'Panamá': 'Panama',
    'Papúa_Nueva_Guinea': 'Papua_New_Guinea',
    'Paraguay': 'Paraguay',
    'Perú': 'Peru',
    'Polonia': 'Poland',
    'Portugal': 'Portugal',
    'Reino_Unido': 'United_Kingdom',
    'República_Centroafricana': 'Central_African_Republic',
    'República_Checa': 'Czech_Republic',
    'República_del_Congo': 'Republic_of_the_Congo',
    'República_Democrática_del_Congo': 'Democratic_Republic_of_the_Congo',
    'República_Dominicana': 'Dominican_Republic',
    'Ruanda': 'Rwanda',
    'Rumanía': 'Romania',
    'Rusia': 'Russia',
    'Samoa': 'Samoa',
    'San_Cristóbal_y_Nieves': 'Saint_Kitts_and_Nevis',
    'San_Marino': 'San_Marino',
    'San_Vicente_y_las_Granadinas': 'Saint_Vincent_and_the_Grenadines',
    'Santa_Lucía': 'Saint_Lucia',
    'Santo_Tomé_y_Príncipe': 'Sao_Tome_and_Principe',
    'Senegal': 'Senegal',
    'Serbia': 'Serbia',
    'Seychelles': 'Seychelles',
    'Sierra_Leona': 'Sierra_Leone',
    'Singapur': 'Singapore',
    'Siria': 'Syria',
    'Somalia': 'Somalia',
    'Sri_Lanka': 'Sri_Lanka',
    'Suazilandia': 'Swaziland',
    'Sudáfrica': 'South_Africa',
    'Sudán': 'Sudan',
    'Sudán_del_Sur': 'South_Sudan',
    'Suecia': 'Sweden',
    'Suiza': 'Switzerland',
    'Surinam': 'Suriname',
    'Tailandia': 'Thailand',
    'Tanzania': 'Tanzania',
    'Tayikistán': 'Tajikistan',
    'Timor_Oriental': 'East_Timor',
    'Togo': 'Togo',
    'Tonga': 'Tonga',
    'Trinidad_y_Tobago': 'Trinidad_and_Tobago',
    'Túnez': 'Tunisia',
    'Turkmenistán': 'Turkmenistan',
    'Turquía': 'Turkey',
    'Tuvalu': 'Tuvalu',
    'Ucrania': 'Ukraine',
    'Uganda': 'Uganda',
    'Uruguay': 'Uruguay',
    'Uzbekistán': 'Uzbekistan',
    'Vanuatu': 'Vanuatu',
    'Venezuela': 'Venezuela',
    'Vietnam': 'Vietnam',
    'Yemen': 'Yemen',
    'Yibuti': 'Djibouti',
    'Zambia': 'Zambia',
    'Zimbabue': 'Zimbabwe'
}


