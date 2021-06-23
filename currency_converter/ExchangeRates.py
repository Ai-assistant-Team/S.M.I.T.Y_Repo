"""
Created on Sat May 8 
@author: Δημήτρης Σούμπασης
"""

from forex_python.converter import CurrencyRates


# c1 = the key the user gives for the currency you are converting from
# c2= the key theuser givesfor the currency you are converting to
# c3= Full name of the currency that the user wants to conver to
# amount= the amount you are converting

currencyMatches = {
    'albania lek'				:		'ALL',
    'afghanistan afghani'		:			'AFN',
    'argentina peso'			:			'ARS',
    'aruba guilder'				:		'AWG',
    'australia dollar'			:		'AUD',
    'azerbaijan manat'			:		'AZN',
    'bahamas dollar'			:			'BSD',
    'barbados dollar'		:				'BBD',
    'belarus ruble'			:			'BYN',
    'belize dollar'			:			'BZD',
    'bermuda dollar'		:				'BMD',
    'bolivia bolíviano'		:			'BOB',
    'bosnia and herzegovina convertible mark'	:	'BAM',
    'botswana pula'				:		'BWP',
    'bulgaria lev'				:		'BGN',
    'brazil real'					:	'BRL',
    'brunei darussalam dollar'		:		'BND',
    'cambodia riel'				:		'KHR',
    'canada dollar'				:		'CAD',
    'cayman islands dollar'		:			'KYD',
    'chile peso'				:		'CLP',
    'china yuan renminbi'		:			'CNY',
    'colombia peso'				:	'COP',
    'costa rica colon'			:		'CRC',
    'croatia kuna'				:		'HRK',
    'cuba peso'					:	'CUP',
    'czech republic koruna'		:			'CZK',
    'denmark krone'				:		'DKK',
    'dominican republic peso'		:			'DOP',
    'east caribbean dollar'			:		'XCD',
    'egypt pound'					:	'EGP',
    'el salvador colon'				:	'SVC',
    'euro member countries'			:		'EUR',
    'falkland islands (malvinas) pound'		:	'FKP',
    'fiji dollar'				:		'FJD',
    'ghana cedi'				:		'GHS',
    'gibraltar pound'			:			'GIP',
    'guatemala quetzal'			:		'GTQ',
    'guernsey pound'			:			'GGP',
    'guyana dollar'				:		'GYD',
    'honduras lempira'			:		'HNL',
    'hong kong dollar'			:		'HKD',
    'hungary forint'			:			'HUF',
    'iceland krona'				:		'ISK',
    'india rupee'			:			'INR',
    'indonesia rupiah'		:			'IDR',
    'iran rial'				:		'IRR',
    'isle of man pound'			:		'IMP',
    'israel shekel'			:			'ILS',
    'jamaica dollar'		:				'JMD',
    'japan yen'				:		'JPY',
    'jersey pound'				:		'JEP',
    'kazakhstan tenge'		:			'KZT',
    'korea (north) won'			:		'KPW',
    'korea (south) won'			:		'KRW',
    'kyrgyzstan som'			:			'KGS',
    'laos kip'					:	'LAK',
    'lebanon pound'				:		'LBP',
    'liberia dollar'			:			'LRD',
    'macedonia denar'			:			'MKD',
    'malaysia ringgit'			:		'MYR',
    'mauritius rupee'			:			'MUR',
    'mexico peso'				:		'MXN',
    'mongolia tughrik'			:		'MNT',
    'mozambique metical'		:			'MZN',
    'namibia dollar'			:			'NAD',
    'nepal rupee	'			:		'NPR',
    'netherlands antilles guilder'		:		'ANG',
    'new zealand dollar'			:		'NZD',
    'nicaragua cordoba'			:		'NIO',
    'nigeria naira'				:		'NGN',
    'norway krone'				:		'NOK',
    'oman rial'				:		'OMR',
    'pakistan rupee'		:				'PKR',
    'panama balboa'			:			'PAB',
    'paraguay guarani'		:			'PYG',
    'peru sol'				:		'PEN',
    'philippines peso'		:			'PHP',
    'poland zloty'			:			'PLN',
    'qatar riyal'			:			'QAR',
    'romania leu'			:			'RON',
    'russia ruble'			:			'RUB',
    'saint helena pound'		:			'SHP',
    'saudi arabia riyal'		:			'SAR',
    'serbia dinar'				:		'RSD',
    'seychelles rupee'			:		'SCR',
    'singapore dollar'		:			'SGD',
    'solomon islands dollar'	:				'SBD',
    'somalia shilling'			:		'SOS',
    'south africa rand'		:			'ZAR',
    'sri lanka rupee'		:			'LKR',
    'sweden krona'			:			'SEK',
    'switzerland franc'		:			'CHF',
    'suriname dollar'		:				'SRD',
    'syria pound	'		:			'SYP',
    'taiwan new dollar'		:			'TWD',
    'thailand baht'			:			'THB',
    'trinidad and tobago dollar'	:			'TTD',
    'turkey lira'			:			'TRY',
    'tuvalu dollar'			:			'TVD',
    'ukraine hryvnia'		:				'UAH',
    'united kingdom pound'	:				'GBP',
    'united states dollar'	:				'USD',
    'uruguay peso'		:				'UYU',
    'uzbekistan som'	:					'UZS',
    'venezuela bolívar'	:				'VEF',
    'viet nam dong'		:				'VND',
    'yemen rial'	:					'YER',
    'zimbabwe dollar'	:					'ZWD'
}


def converter(c1, c2, amount):

    try:
        c = CurrencyRates()
        cc = round(c.convert(currencyMatches[c1], currencyMatches[c2], amount),2)
        return(str(cc) + ' ' + c2)
    except:
        return 1
